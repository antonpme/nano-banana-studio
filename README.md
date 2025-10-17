# 🍌 Nano-Banana Studio

**A professional, self-hosted control panel for Google's Gemini 2.5 Flash image generation model.**

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10+-blue)

Transform text into stunning images with an intuitive, feature-rich interface. Create reusable presets, manage complex prompts with field-based templates, and streamline your AI image generation workflow.

## ✨ Features

### 🎨 Three Generation Modes
- **Text-to-Image** - Generate images from text descriptions
- **Image Editing** - Modify existing images with natural language instructions
- **Multi-Image Composition** - Combine 2-4 images into cohesive compositions

### 📋 Advanced Preset System
- **Field-Based Prompt Builder** - Dynamic form builder with predefined field library
- **5 Preset Types** - Photorealistic, Artistic Styles, Icons, Logos, Custom templates
- **JSON/Text Output** - Generate structured or plain text prompts
- **Reusable Templates** - Save and reuse successful configurations
- **Tag System** - Organize presets with searchable keywords

### 🎯 Professional UI
- **4-Level Drawer System** - Hierarchical navigation for complex workflows
- **Modern Design** - Clean, dark interface with Inter typography
- **Fully Responsive** - Works on desktop, tablet, and mobile
- **Accessibility First** - WCAG AA compliant, keyboard navigation

### 🔧 Self-Hosted & Flexible
- **Your Data, Your Server** - Complete control over your presets and images
- **No Tracking** - No analytics, no third-party services
- **Open Source** - MIT licensed, community-driven

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Google Gemini API key ([Get one here](https://ai.google.dev/))
- Git (for cloning the repository)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/antonpme/nano-banana.git
cd nano-banana
```

**2. Create virtual environment**
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment**
```bash
# Copy example file
cp .env.example .env

# Edit .env and add your API key
```

**5. Run the application**
```bash
python app.py
```

**6. Open in browser**
```
http://localhost:5000
```

---

## 🐳 Docker Deployment

```bash
# Build the image
docker build -t nano-banana .

# Run the container
docker run -p 5000:5000 -e GEMINI_API_KEY=your-api-key-here nano-banana
```

With Docker Compose:
```bash
# Create .env file with your API key
echo "GEMINI_API_KEY=your-key-here" > .env

# Start the container
docker-compose up -d
```

- The container exposes `/api/health` for orchestration health checks.
- Presets persist under the mounted `./data` directory via `PRESETS_DB_PATH`.

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GEMINI_API_KEY` | Your Google Gemini API key | Required |
| `PORT` | Server port | `5000` |
| `FLASK_ENV` | Environment (development/production) | `development` |
| `PRESETS_DB_PATH` | Path to presets database | `./presets_db.json` |
| `FIELD_LIBRARY_PATH` | Path to field library | `./field_library.json` |

---

## 📖 Usage Guide

### Creating Your First Preset

1. Click **⚙️ Manage** next to the preset selector
2. Click **+ New** in the preset drawer
3. Select a **Preset Type** (e.g., Photorealistic Images)
4. Enter a **Preset Name** (e.g., "Cinematic Portrait")
5. Click **+ Add Field** to browse available fields
6. Select fields like "subject", "style", "lighting"
7. Fill in default values for each field
8. Preview your prompt template
9. Click **Save**

### Generating Images

1. Select your preset from the dropdown
2. The form will populate with your preset fields
3. Add a style reference image (optional)
4. Choose aspect ratio
5. Click **🎨 Generate**
6. Download your image

### Editing Images

1. Switch to **✏️ Edit** tab
2. Upload an image
3. Describe your desired changes
4. Click **Generate**

### Composing Multiple Images

1. Switch to **🖼️ Compose** tab
2. Upload 2-4 images
3. Describe how to combine them
4. Click **Generate**

---

## 🏗️ Project Structure

```
nano-banana/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── presets_db.json          # User presets database
├── field_library.json       # Field definitions
├── templates/
│   └── index.html           # Main SPA
├── docs/                    # Documentation
│   ├── prd.md              # Product requirements
│   ├── specs.md            # Technical specifications
│   ├── design.md           # Design system guide
│   └── tasks.md            # Development tasks
├── .env.example            # Example environment file
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose setup
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contributing guidelines
└── README.md              # This file
```

---

## 🤝 Contributing

We welcome contributions! Whether it's bug fixes, new features, or documentation improvements.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

---

## 📚 Documentation

- **[Product Requirements](./docs/prd.md)** - Feature specifications and roadmap
- **[Technical Specs](./docs/specs.md)** - API documentation and architecture
- **[Design System](./docs/design.md)** - UI guidelines and components
- **[Task Tracking](./docs/tasks.md)** - Development progress

---

## 🗺️ Roadmap

### v1.0 (Current - Beta)
- [x] Core image generation (text-to-image, edit, compose)
- [x] Preset management system
- [x] Field-based prompt builder
- [x] 4-level drawer UI
- [ ] In-app API key configuration
- [ ] Settings panel

### v1.1 (Next)
- [ ] Preset import/export
- [ ] Batch image generation
- [ ] Preset marketplace/sharing
- [ ] Advanced image editing tools
- [ ] Usage analytics dashboard

### v2.0 (Future)
- [ ] Multi-user support with authentication
- [ ] Collaborative preset editing
- [ ] API webhooks
- [ ] Plugin system
- [ ] Mobile apps (iOS, Android)

See [docs/tasks.md](./docs/tasks.md) for detailed progress.

---

## 🐛 Known Issues

- Field Browser may require page refresh after first preset creation
- Preset list search/filter not yet implemented
- No preset duplication feature yet

See [GitHub Issues](https://github.com/antonpme/nano-banana/issues) for full list.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Google Gemini Team** - For the amazing Gemini 2.5 Flash image model
- **Flask Community** - For the excellent web framework
- **Inter Font** - By Rasmus Andersson
- **All Contributors** - Thank you for making this project better!

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/antonpme/nano-banana/issues)
- **Discussions**: [GitHub Discussions](https://github.com/antonpme/nano-banana/discussions)

---

Made with ❤️ by the Nano-Banana community
- Mention camera settings for photorealistic images
- Example: "A photorealistic close-up of a vintage camera on a wooden desk, shot with an 85mm lens, golden hour lighting, shallow depth of field"

### Image Editing
- Be specific about what you want to change
- Reference elements by name (e.g., "the sky", "the person's hair")
- Describe the style or mood you want
- Example: "Change the sky to a dramatic sunset with orange and purple tones"

### Multi-Image Composition
- Clearly describe the layout and positioning
- Specify how to blend or merge the images
- Mention style transfer if desired
- Example: "Merge image 1 (landscape) and image 2 (person) to show the person standing in the landscape"

### Iterative Refinement
- Start with broad strokes, refine details
- Make small adjustments at each step
- Build up complexity gradually
- Example: First generate a scene, then refine lighting, then add details

### High-Fidelity Text in Images
The model excels at rendering readable text. Use it for:
- Logos with text
- Diagrams and posters
- Social media graphics
- UI mockups
- Example: "Create a minimalist coffee shop logo with 'The Daily Grind' in bold sans-serif font"

## Troubleshooting

### "API Key not found" error
Make sure your `GEMINI_API_KEY` environment variable is properly set.

### "ModuleNotFoundError" for Flask or google-genai
Run `pip install -r requirements.txt` again to ensure all dependencies are installed.

### Images not generating
Check that your API key is valid and you have quota remaining in your Google Cloud account.

## License

This project uses Google's Gemini API. Ensure you comply with Google's terms of service.

## Learn More

- [Google Gemini API Documentation](https://ai.google.dev/)
- [Image Generation Guide](https://ai.google.dev/gemini-api/docs/image-generation)
- [Get a Free API Key](https://ai.google.dev/aistudio)
