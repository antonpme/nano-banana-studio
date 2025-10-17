# 🎉 Nano-Banana Studio v1.0.0-beta

**The first open-source release of Nano-Banana Studio!**

A professional, self-hosted control panel for Google's Gemini 2.5 Flash image generation model. Create stunning images with an intuitive interface, reusable presets, and field-based prompt templates.

---

## ✨ What's Included

### Core Features
- **🎨 Three Generation Modes**: Text-to-image, image editing, and multi-image composition
- **📋 Advanced Preset System**: Field-based prompt builder with 5 preset types
- **🎯 Professional UI**: 4-level drawer system with modern dark theme
- **🔧 Self-Hosted**: Complete control over your data and images

### Technical Highlights
- **Flask Backend** - RESTful API with Gemini integration
- **Modern Frontend** - Vanilla JavaScript with Inter typography
- **Docker Support** - One-command deployment with docker-compose
- **Comprehensive Docs** - PRD, Technical Specs, Design System, Task Tracking

---

## 📦 Installation

### Quick Start (Docker)
```bash
git clone https://github.com/antonpme/nano-banana.git
cd nano-banana
echo "GEMINI_API_KEY=your-key-here" > .env
docker-compose up -d
```

### Manual Installation
```bash
# Clone repository
git clone https://github.com/antonpme/nano-banana.git
cd nano-banana

# Use automated installation script
# On Windows:
.\install.ps1

# On macOS/Linux:
chmod +x install.sh
./install.sh
```

---

## 🎯 Current Status

### ✅ Complete (100%)
- Core image generation (text-to-image, edit, compose)
- Preset management system (CRUD operations)
- Field-based prompt builder
- 4-level drawer UI with professional design
- Docker deployment support
- Comprehensive documentation

### 🔄 In Progress (70-85%)
- Field editor integration
- Apply preset to main form
- Parent dimming effects
- Keyboard navigation

### ⏳ Planned for v1.1
- **Settings UI** for API key configuration (currently uses .env)
- **Health check endpoint** to test API connection
- **First-run wizard** for guided setup
- API key encryption and secure storage
- Rate limiting
- Preset import/export

---

## 🐛 Known Issues

- Field Browser may require page refresh after first preset creation
- API key must be configured via `.env` file (no UI yet)
- Preset list search/filter not yet implemented
- No preset duplication feature

See [Issue #1](https://github.com/antonpme/nano-banana/issues/1) for the complete roadmap.

---

## 📚 Documentation

- **[README](./README.md)** - Installation and usage guide
- **[CONTRIBUTING](./CONTRIBUTING.md)** - Development guidelines
- **[Product Requirements](./docs/prd.md)** - Feature specifications
- **[Technical Specs](./docs/specs.md)** - API documentation
- **[Design System](./docs/design.md)** - UI guidelines
- **[Task Tracking](./docs/tasks.md)** - Development progress

---

## 🙏 Acknowledgments

- **Google Gemini Team** - For the amazing Gemini 2.5 Flash image model
- **Flask Community** - For the excellent web framework
- **Rasmus Andersson** - For the Inter font

---

## 🤝 Contributing

This is an open-source project and contributions are welcome! Whether it's:
- Bug fixes
- New features
- Documentation improvements
- Translations

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License - see [LICENSE](./LICENSE) for details.

---

## 🔗 Links

- **Repository**: https://github.com/antonpme/nano-banana
- **Issues**: https://github.com/antonpme/nano-banana/issues
- **Discussions**: https://github.com/antonpme/nano-banana/discussions

---

**Made with ❤️ by Anton P. and the Nano-Banana community**

Get your Gemini API key at: https://ai.google.dev/
