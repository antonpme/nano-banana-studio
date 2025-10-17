from flask import Flask, render_template, request, jsonify, send_file
import base64
import mimetypes
import os
from google import genai
from google.genai import types
from io import BytesIO
import uuid
from PIL import Image
import time
import json
from datetime import datetime

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# Initialize Gemini client
client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

# Store generated images and conversation state
generated_images = {}
conversation_state = {}

# Simple rate limiting tracker
last_request_time = 0
MIN_REQUEST_INTERVAL = 3  # seconds between requests

# Paths to JSON databases
FIELD_LIBRARY_PATH = os.environ.get('FIELD_LIBRARY_PATH', 'field_library.json')
PRESETS_DB_PATH = os.environ.get('PRESETS_DB_PATH', 'presets_db.json')


DEFAULT_PRESETS_DB = {
    "presets": [],
    "version": "1.0.0",
    "lastModified": None
}


def ensure_presets_db():
    """Ensure the presets database exists and has a valid structure."""
    path_dir = os.path.dirname(PRESETS_DB_PATH)
    if path_dir:
        os.makedirs(path_dir, exist_ok=True)

    if not os.path.exists(PRESETS_DB_PATH):
        with open(PRESETS_DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(
                {**DEFAULT_PRESETS_DB, "lastModified": datetime.now().isoformat()},
                f,
                indent=2,
                ensure_ascii=False,
            )
        return

    try:
        with open(PRESETS_DB_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict) or 'presets' not in data:
            raise ValueError("Invalid presets database format")
    except Exception:
        with open(PRESETS_DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(
                {**DEFAULT_PRESETS_DB, "lastModified": datetime.now().isoformat()},
                f,
                indent=2,
                ensure_ascii=False,
            )


def load_presets_db():
    ensure_presets_db()
    with open(PRESETS_DB_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_presets_db(db):
    path_dir = os.path.dirname(PRESETS_DB_PATH)
    if path_dir:
        os.makedirs(path_dir, exist_ok=True)
    with open(PRESETS_DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Basic health check endpoint for container orchestration."""
    status = {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "presetsDbPath": os.path.abspath(PRESETS_DB_PATH),
        "fieldLibraryPath": os.path.abspath(FIELD_LIBRARY_PATH),
    }
    try:
        load_presets_db()
        status["presetsDbLoaded"] = True
    except Exception as exc:
        status["presetsDbLoaded"] = False
        status["error"] = str(exc)
        return jsonify(status), 500
    return jsonify(status)


@app.route('/api/generate', methods=['POST'])
def generate_image():
    global last_request_time
    
    try:
        # Simple rate limiting
        current_time = time.time()
        time_since_last = current_time - last_request_time
        if time_since_last < MIN_REQUEST_INTERVAL:
            wait_time = MIN_REQUEST_INTERVAL - time_since_last
            return jsonify({
                'error': f'Please wait {wait_time:.1f} seconds before next request',
                'wait_time': wait_time
            }), 429
        
        data = request.json
        prompt = data.get('prompt', '')
        aspect_ratio = data.get('aspect_ratio', '1:1')
        mode = data.get('mode', 'text-to-image')
        uploaded_images = data.get('uploaded_images', [])
        session_id = data.get('session_id', str(uuid.uuid4()))
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        # Update last request time
        last_request_time = current_time
        
        model = "gemini-2.5-flash-image"
        
        # Build contents based on mode
        # IMPORTANT: For image editing/composition, images must come BEFORE the text instruction
        parts = []
        
        # Add uploaded images first (if in edit or compose mode)
        if mode in ['image-edit', 'multi-image-compose'] and uploaded_images:
            for img_data in uploaded_images:
                try:
                    # Remove data URI prefix if present
                    if ',' in img_data:
                        img_data = img_data.split(',')[1]
                    
                    image_bytes = base64.b64decode(img_data)
                    mime_type = mimetypes.guess_type("image.png")[0] or "image/png"
                    
                    # Infer actual mime type from image data if possible
                    if image_bytes.startswith(b'\x89PNG'):
                        mime_type = "image/png"
                    elif image_bytes.startswith(b'\xff\xd8\xff'):
                        mime_type = "image/jpeg"
                    elif image_bytes.startswith(b'GIF8'):
                        mime_type = "image/gif"
                    
                    # Create Part from image bytes
                    parts.append(types.Part.from_bytes(
                        data=image_bytes,
                        mime_type=mime_type
                    ))
                except Exception as e:
                    print(f"Error processing image: {e}")
        
        # Add text prompt AFTER images
        parts.append(types.Part.from_text(text=prompt))
        
        contents = [
            types.Content(
                role="user",
                parts=parts,
            ),
        ]
        
        # Configure generation settings with aspect ratio
        generate_image_config = types.GenerateImageConfig(
            aspect_ratio=aspect_ratio,
        )
        
        response_text = ""
        image_data = None
        image_mime_type = None
        
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_image_config,
        ):
            if (
                chunk.candidates is None
                or chunk.candidates[0].content is None
                or chunk.candidates[0].content.parts is None
            ):
                continue
            
            if chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data:
                inline_data = chunk.candidates[0].content.parts[0].inline_data
                image_data = inline_data.data
                image_mime_type = inline_data.mime_type
            else:
                if chunk.text:
                    response_text += chunk.text
        
        if image_data:
            # Create a unique ID for this image
            image_id = str(uuid.uuid4())
            generated_images[image_id] = {
                'data': image_data,
                'mime_type': image_mime_type,
                'session_id': session_id
            }
            
            # Store session for multi-turn editing
            if session_id not in conversation_state:
                conversation_state[session_id] = []
            
            conversation_state[session_id].append({
                'prompt': prompt,
                'image_id': image_id
            })
            
            # Convert to base64 for display
            b64_image = base64.b64encode(image_data).decode('utf-8')
            
            return jsonify({
                'success': True,
                'image_id': image_id,
                'image_base64': b64_image,
                'mime_type': image_mime_type,
                'text': response_text,
                'session_id': session_id
            })
        else:
            return jsonify({
                'success': True,
                'text': response_text,
                'error': 'No image generated'
            })
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        error_str = str(e)
        
        print(f"Error in generate_image: {error_details}")
        
        # Check if it's a rate limit error
        if '429' in error_str or 'quota' in error_str.lower() or 'rate limit' in error_str.lower():
            return jsonify({
                'error': 'Rate limit exceeded. Please wait a few seconds and try again.',
                'type': 'rate_limit'
            }), 429
        
        # Check if it's a 500 internal error from Google
        if '500' in error_str or 'INTERNAL' in error_str:
            return jsonify({
                'error': 'Google API temporary error. Please wait a moment and try again.',
                'type': 'api_internal',
                'details': error_str
            }), 503
        
        return jsonify({'error': error_str, 'details': error_details}), 500


@app.route('/api/download/<image_id>')
def download_image(image_id):
    try:
        if image_id not in generated_images:
            return jsonify({'error': 'Image not found'}), 404
        
        image_info = generated_images[image_id]
        image_data = image_info['data']
        mime_type = image_info['mime_type']
        
        # Guess file extension
        file_extension = mimetypes.guess_extension(mime_type)
        filename = f"generated_image_{image_id}{file_extension}"
        
        return send_file(
            BytesIO(image_data),
            mimetype=mime_type,
            as_attachment=True,
            download_name=filename
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== PRESET & FIELD LIBRARY ENDPOINTS ====================

@app.route('/api/field-library', methods=['GET'])
def get_field_library():
    """Get the complete field library definitions"""
    try:
        with open(FIELD_LIBRARY_PATH, 'r', encoding='utf-8') as f:
            field_library = json.load(f)
        return jsonify(field_library)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/presets', methods=['GET'])
def get_presets():
    """Get all saved presets"""
    try:
        db = load_presets_db()
        return jsonify(db['presets'])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/presets', methods=['POST'])
def create_preset():
    """Create a new preset"""
    try:
        preset_data = request.json
        preset_data['id'] = str(uuid.uuid4())
        preset_data['createdAt'] = datetime.now().isoformat()
        preset_data['updatedAt'] = datetime.now().isoformat()

        db = load_presets_db()
        db['presets'].append(preset_data)
        db['lastModified'] = datetime.now().isoformat()

        save_presets_db(db)
        
        return jsonify(preset_data), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/presets/<preset_id>', methods=['PUT'])
def update_preset(preset_id):
    """Update an existing preset"""
    try:
        preset_data = request.json

        db = load_presets_db()

        # Find and update preset
        for i, preset in enumerate(db['presets']):
            if preset.get('id') == preset_id:
                preset_data['id'] = preset_id
                preset_data['createdAt'] = preset.get('createdAt')
                preset_data['updatedAt'] = datetime.now().isoformat()
                db['presets'][i] = preset_data
                db['lastModified'] = datetime.now().isoformat()

                save_presets_db(db)
                
                return jsonify(preset_data)
        
        return jsonify({'error': 'Preset not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/presets/<preset_id>', methods=['DELETE'])
def delete_preset(preset_id):
    """Delete a preset"""
    try:
        db = load_presets_db()
        
        # Filter out the preset
        original_count = len(db['presets'])
        db['presets'] = [p for p in db['presets'] if p.get('id') != preset_id]
        
        if len(db['presets']) == original_count:
            return jsonify({'error': 'Preset not found'}), 404
        
        db['lastModified'] = datetime.now().isoformat()

        save_presets_db(db)
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
