# Nano-Banana Studio - Technical Specifications

## System Architecture

### Overview
Nano-Banana Studio follows a client-server architecture with a Flask backend serving a single-page application (SPA) frontend.

```
+-------------------+       HTTP + JSON        +------------------------+
| Client (Browser)  | <----------------------> | Flask Server (app.py)  |
| - HTML/CSS (SPA)  |                          | - /                    |
| - Vanilla JS      |                          | - /api/health          |
| - Drawer UI       |                          | - /api/generate        |
+-------------------+                          | - /api/download/<id>   |
                                               | - /api/presets         |
                                               | - /api/field-library   |
                                               +-----------+------------+
                                                           |
                                                           | Google SDK
                                                           v
                                               +------------------------+
                                               | Google Gemini 2.5 API  |
                                               +------------------------+

+------------------+
| File Storage     |
| - presets_db.json|
| - field_library  |
+------------------+
```

---

## Backend Specifications

### Technology Stack
- **Runtime:** Python 3.10+
- **Framework:** Flask 3.0.0
- **AI SDK:** google-genai 0.5.0
- **Dependencies:** See `requirements.txt`

### File Structure
```
nano-banana/
├── app.py                    # Flask application entry point
├── presets_db.json          # Preset storage (database)
├── field_library.json       # Field definitions
├── requirements.txt         # Python dependencies
├── templates/
│   └── index.html          # Main SPA template
├── static/                 # Static assets (if any)
└── docs/                   # Documentation
    ├── prd.md
    ├── specs.md
    ├── design.md
    └── tasks.md
```

The Flask service respects the `PRESETS_DB_PATH` and `FIELD_LIBRARY_PATH` environment variables when locating these JSON stores. Default values keep the files alongside `app.py`, while container deployments map `/app/data/presets_db.json` for persistence.


### API Endpoints

#### 1. GET `/`
Serves `templates/index.html` as the single-page application shell.

#### 2. GET `/api/health`
Lightweight health probe used by Docker/Compose. Returns `{ "status": "ok" }` with diagnostic metadata when presets storage loads successfully.

#### 3. POST `/api/generate`
Unified image workflow endpoint. Accepts JSON payload:
```json
{
  "prompt": "string",
  "aspect_ratio": "1:1|16:9|9:16|3:2|2:3",
  "mode": "text-to-image|image-edit|multi-image-compose",
  "uploaded_images": ["data-uri base64 strings"],
  "session_id": "uuid"
}
```
- Uploaded images must be supplied for `image-edit` (>=1) and `multi-image-compose` (2-4) modes.
- Streams Gemini responses; returns consolidated payload with `image_base64`, `mime_type`, optional generated text, and `image_id` for later download.
- Uses in-memory cache keyed by `image_id` to support `/api/download`.

#### 4. GET `/api/download/<image_id>`
Delivers the previously generated binary image using the cached payload from `/api/generate`. Returns 404 if `image_id` is unknown or expired.

#### 5. GET `/api/field-library`
Serves `field_library.json` so the frontend drawer system can render preset field definitions dynamically.

#### 6. Preset CRUD `/api/presets`
- `GET /api/presets` ? returns the full list of saved presets.
- `POST /api/presets` ? creates a preset, assigning UUID and timestamps server-side.
- `PUT /api/presets/<id>` ? updates an existing preset and refreshes `updatedAt`.
- `DELETE /api/presets/<id>` ? removes a preset by id.

#### 7. Static Files
All other assets are served through Flask's templating system; no additional static endpoints are exposed.
## Frontend Specifications

### Technology Stack
- **Core:** Vanilla JavaScript (ES6+)
- **Styling:** Native CSS (no preprocessors)
- **Fonts:** Inter (Google Fonts)
- **Icons:** SVG (inline)

### Component Architecture

#### 1. Main Application Layout
```html
<body>
  <!-- Header -->
  <header id="app-header">
    <!-- Title, mode tabs -->
  </header>
  
  <!-- Main Content Area -->
  <main id="app-main">
    <!-- Form sections for each mode -->
    <section class="form-section generate active">
      <!-- Text-to-image form -->
    </section>
    <section class="form-section edit">
      <!-- Image edit form -->
    </section>
    <section class="form-section compose">
      <!-- Multi-image compose form -->
    </section>
    
    <!-- Results display -->
    <div id="results">
      <!-- Generated images -->
    </div>
  </main>
  
  <!-- Drawer System -->
  <div id="preset-drawer">
    <!-- Level 1: Preset List -->
  </div>
  <div id="preset-editor-drawer">
    <!-- Level 2: Preset Editor -->
  </div>
  <div id="field-editor-drawer">
    <!-- Level 3: Field Editor -->
  </div>
  <div id="field-browser-drawer">
    <!-- Level 4: Field Browser -->
  </div>
  <div id="drawer-backdrop">
    <!-- Backdrop overlay -->
  </div>
</body>
```

#### 2. Drawer System Structure

**Level 1: Preset List**
```javascript
// Structure
{
  header: {
    closeButton: SVG icon,
    title: "Style Presets",
    newButton: SVG icon + "New"
  },
  content: {
    presetCards: [
      {
        id: "uuid",
        name: "Preset Name",
        type: "badge",
        outputFormat: "text",
        tags: ["tag1", "tag2"],
        onClick: openPresetEditor(id)
      }
    ]
  }
}
```

**Level 2: Preset Editor**
```javascript
// Form Fields
{
  presetType: <select>,
  presetName: <input>,
  outputFormat: <radio buttons>,
  promptFields: {
    addButton: openFieldBrowser(),
    fieldsList: [
      {
        field: chip component,
        editButton: openFieldEditor(id),
        deleteButton: removeField(id)
      }
    ]
  },
  promptPreview: <textarea readonly>,
  backgroundColor: <input color>,
  backgroundTransparent: <checkbox>,
  aspectRatio: <select>,
  tags: <input>,
  referenceImage: <file upload>
}
```

**Level 3: Field Editor**
```javascript
// Form Fields
{
  fieldName: <input readonly>,
  fieldValue: <textarea>,
  fieldType: <input readonly>,
  fieldRequired: <checkbox>
}
```

**Level 4: Field Browser**
```javascript
// Content
{
  searchInput: <input>,
  fieldChips: [
    {
      name: "Field Name",
      description: "Description",
      type: "text",
      added: boolean,
      onClick: addFieldFromBrowser(id)
    }
  ]
}
```

### State Management

#### Global State Variables
```javascript
// Mode and iteration
let currentMode = 'text-to-image';
let iterationCount = 0;

// Image uploads
let uploadedImages = {
  'text-to-image': [],
  'image-edit': [],
  'multi-image-compose': []
};

// Preset management
let allPresets = [];
let currentPresetType = 'photorealistic';
let promptFields = [];
let currentEditingPresetId = null;
let currentEditingFieldId = null;

// Field library
let fieldLibraryData = null;

// Reference images
let presetImageData = null;
```

### Key Functions

#### Image Generation
```javascript
async function generateImage() {
  const prompt = document.getElementById('prompt-generate').value;
  const aspectRatio = document.getElementById('aspect-ratio-generate').value;
  
  // Build request
  const requestData = {
    prompt: prompt,
    aspectRatio: aspectRatio,
    referenceImage: uploadedImages['text-to-image'][0] || null
  };
  
  // Call API
  const response = await fetch('/api/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(requestData)
  });
  
  // Handle response
  const data = await response.json();
  displayImage(data.image);
}
```

#### Drawer Navigation
```javascript
// Open drawer functions
function openPresetDrawer() {
  document.getElementById('drawer-backdrop').style.display = 'block';
  document.getElementById('preset-drawer').style.right = '0';
  renderPresetList();
}

function openPresetEditor(presetId) {
  if (presetId) {
    loadPresetForEditing(presetId);
  } else {
    resetPresetForm();
  }
  document.getElementById('preset-editor-drawer').style.right = '0';
}

function openFieldEditor(fieldId) {
  loadFieldForEditing(fieldId);
  document.getElementById('field-editor-drawer').style.right = '0';
}

function openFieldBrowser() {
  const presetType = document.getElementById('preset-type').value;
  renderFieldBrowserContent(presetType);
  document.getElementById('field-browser-drawer').style.right = '0';
}

// Close drawer functions
function closePresetDrawer() {
  document.getElementById('preset-drawer').style.right = '-650px';
  setTimeout(() => {
    document.getElementById('drawer-backdrop').style.display = 'none';
  }, 300);
}

function closeAllDrawers() {
  closeFieldBrowser();
  closeFieldEditor();
  closePresetEditor();
  closePresetDrawer();
}
```

#### Preset CRUD
```javascript
// Create/Update
async function saveCurrentPreset() {
  const preset = buildPresetObject();
  
  const url = currentEditingPresetId 
    ? `/api/presets/${currentEditingPresetId}`
    : '/api/presets';
  
  const method = currentEditingPresetId ? 'PUT' : 'POST';
  
  const response = await fetch(url, {
    method: method,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(preset)
  });
  
  const data = await response.json();
  
  if (data.success) {
    await loadAllPresets();
    closePresetEditor();
    showSuccess('Preset saved successfully');
  }
}

// Read
async function loadAllPresets() {
  const response = await fetch('/api/presets');
  const data = await response.json();
  allPresets = data.presets || [];
}

// Delete
async function deletePreset(presetId) {
  if (!confirm('Delete this preset?')) return;
  
  const response = await fetch(`/api/presets/${presetId}`, {
    method: 'DELETE'
  });
  
  const data = await response.json();
  
  if (data.success) {
    await loadAllPresets();
    renderPresetList();
    showSuccess('Preset deleted');
  }
}
```

---

## Data Models

### Preset Schema
```typescript
interface Preset {
  id: string;                    // UUID v4
  name: string;                  // User-defined name
  presetType: PresetType;        // Type category
  outputFormat: 'text' | 'json'; // Prompt format
  promptFields: PromptField[];   // Array of fields
  backgroundColor: string;        // Hex color, 'transparent', or 'auto'
  aspectRatio: AspectRatio;      // Image dimensions
  tags: string[];                // Searchable keywords
  referenceImage: string | null; // Base64 image or null
  createdAt: string;             // ISO-8601 timestamp
  updatedAt: string;             // ISO-8601 timestamp
}

type PresetType = 
  | 'photorealistic'
  | 'art_styles'
  | 'icon_generation'
  | 'logo_generation'
  | 'custom';

type AspectRatio = '1:1' | '16:9' | '9:16' | '4:3' | '3:4';

interface PromptField {
  id: string;          // Unique identifier
  name: string;        // Field name (e.g., "subject", "style")
  type: FieldType;     // Input type
  value: string;       // Current value
  required: boolean;   // Is field required
}

type FieldType = 'text' | 'textarea' | 'select' | 'number';
```

### Field Library Schema
```typescript
interface FieldLibrary {
  version: string;
  presetTypes: {
    [key in PresetType]: PresetTypeDefinition;
  };
}

interface PresetTypeDefinition {
  name: string;
  description: string;
  suggestedFields: string[];     // Recommended field IDs
  fieldDefinitions: FieldDefinition[];
}

interface FieldDefinition {
  id: string;
  name: string;
  type: FieldType;
  description: string;
  defaultValue: string;
  required: boolean;
  options?: string[];            // For select type
  placeholder?: string;
  min?: number;                  // For number type
  max?: number;                  // For number type
}
```

---

## Design Tokens

### Spacing
```css
--spacing-xs: 4px;
--spacing-sm: 8px;
--spacing-md: 12px;
--spacing-lg: 16px;
--spacing-xl: 20px;
--spacing-xxl: 24px;
```

### Border Radius
```css
--radius-none: 0px;       /* Drawers */
--radius-sm: 4px;         /* Buttons, inputs */
--radius-md: 6px;         /* Cards, chips */
--radius-lg: 8px;         /* (not used) */
```

### Transitions
```css
--transition-fast: 0.15s ease;
--transition-normal: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
--transition-slow: 0.5s ease;
```

### Z-Index Layers
```css
--z-backdrop: 1999;
--z-drawer-1: 2000;
--z-drawer-2: 2001;
--z-drawer-3: 2002;
--z-drawer-4: 2003;
--z-modal: 3000;
--z-toast: 10000;
```

### Typography Scale
```css
--font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

--text-xs: 0.75em;
--text-sm: 0.85em;
--text-base: 0.95em;
--text-lg: 1.1em;
--text-xl: 1.2em;

--weight-normal: 400;
--weight-medium: 500;
--weight-semibold: 600;
--weight-bold: 700;
```

---

## Performance Considerations

### Frontend Optimization
1. **Lazy Loading:**
   - Drawer content rendered on open (not on page load)
   - Field browser loads only when preset type selected

2. **Debouncing:**
   - Search input debounced (300ms)
   - Preview updates debounced (200ms)

3. **Efficient Rendering:**
   - Use DocumentFragment for batch DOM updates
   - Minimize reflows with transform/opacity animations
   - Virtual scrolling for 100+ presets (future)

### Backend Optimization
1. **Caching:**
   - Field library cached in memory (rarely changes)
   - Preset list cached, invalidated on write

2. **Request Validation:**
   - Validate all inputs before API call
   - Return early on validation failures

3. **Error Handling:**
   - Catch and log all exceptions
   - Return user-friendly error messages
   - Retry logic for transient failures

---

## Security Considerations

### Input Validation
- **Client-side:** Immediate feedback, UX enhancement
- **Server-side:** Actual security, never trust client

### File Upload Security
1. Validate MIME types (whitelist)
2. Enforce size limits
3. Scan for malicious content (future)
4. Store uploaded files securely

### API Key Protection
- Never expose in client code
- Store in environment variables
- Rotate keys periodically

### XSS Prevention
- Sanitize all user inputs
- Use textContent instead of innerHTML where possible
- Escape HTML in dynamic content

---

## Testing Strategy

### Unit Tests
- Preset CRUD operations
- Field validation logic
- Prompt template generation
- Data serialization/deserialization

### Integration Tests
- API endpoint responses
- Database operations
- Gemini API integration

### E2E Tests
- Complete preset creation workflow
- Image generation flow
- Drawer navigation
- Error handling scenarios

### Manual Testing Checklist
- [ ] Create preset with all field types
- [ ] Edit existing preset
- [ ] Delete preset
- [ ] Generate image with preset
- [ ] Upload reference image
- [ ] Navigate all drawer levels
- [ ] Search/filter presets
- [ ] Export/import presets
- [ ] Error states (API failure, validation errors)

---

## Deployment

### Environment Variables
```bash
GEMINI_API_KEY=your_api_key_here
FLASK_ENV=production
PORT=5000
PRESETS_DB_PATH=/app/data/presets_db.json
FIELD_LIBRARY_PATH=/app/field_library.json
```

### Production Checklist
- [ ] Set `FLASK_ENV=production`
- [ ] Configure proper logging
- [ ] Set up error monitoring (Sentry, etc.)
- [ ] Configure CORS if needed
- [ ] Set up SSL/HTTPS
- [ ] Configure CDN for static assets
- [ ] Database backups automated
- [ ] Rate limiting configured

### Monitoring
- API response times
- Error rates by endpoint
- Gemini API usage/costs
- User engagement metrics
- Server resource usage

---

## Appendix

### File Size Limits
- Single image upload: 20MB
- Reference image: 10MB
- Multi-image total: 40MB
- Preset JSON: 1MB

### Rate Limits (Gemini API)
- Requests per minute: 60
- Requests per day: 1500
- (Check current Google quotas)

### Browser Storage
- LocalStorage: Not used (server-side storage only)
- SessionStorage: Not used
- Cookies: Not used

### Logging Levels
- ERROR: API failures, exceptions
- WARN: Validation failures, deprecated features
- INFO: Request/response, preset CRUD
- DEBUG: Detailed execution flow
