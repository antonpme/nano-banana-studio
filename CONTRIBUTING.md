# Contributing to Nano-Banana Studio

First off, thank you for considering contributing to Nano-Banana Studio! It's people like you that make this tool better for everyone.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (screenshots, error messages, etc.)
- **Describe the behavior you observed** and what you expected
- **Include your environment details** (OS, Python version, browser)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the proposed functionality
- **Explain why this enhancement would be useful**
- **List any alternative solutions** you've considered

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write clear commit messages**
6. **Submit a pull request** with a comprehensive description

## Development Setup

### Prerequisites
- Python 3.10+
- Git
- Google Gemini API key

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/nano-banana.git
cd nano-banana

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Run the app
python app.py
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_presets.py
```

## Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some exceptions:

- **Line length**: 100 characters maximum (not 79)
- **Imports**: Organize as stdlib, third-party, local (separated by blank lines)
- **Docstrings**: Use Google-style docstrings
- **Type hints**: Use type hints for function parameters and return values

### Example Code

```python
from typing import Dict, List, Optional
import os

from flask import Flask, request, jsonify
import google.generativeai as genai


def generate_image(prompt: str, aspect_ratio: str = "1:1") -> Dict[str, str]:
    """Generate an image using Gemini API.
    
    Args:
        prompt: The text description for image generation
        aspect_ratio: Image aspect ratio (default: "1:1")
        
    Returns:
        Dictionary containing image_url and generation_time
        
    Raises:
        ValueError: If prompt is empty or aspect_ratio is invalid
    """
    if not prompt:
        raise ValueError("Prompt cannot be empty")
    
    # Implementation here
    return {"image_url": url, "generation_time": time}
```

### Frontend Style Guide

- **HTML**: Use semantic HTML5 elements
- **CSS**: Follow BEM naming convention for classes
- **JavaScript**: Use ES6+ features, avoid jQuery
- **Accessibility**: Ensure WCAG AA compliance

### Commit Message Format

```
type(scope): subject

body (optional)

footer (optional)
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Example:**
```
feat(presets): add preset duplication feature

Allow users to duplicate existing presets with a single click.
Duplicated presets get " (Copy)" suffix automatically.

Closes #42
```

## Project Structure

```
nano-banana/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # SPA frontend
├── tests/                # Test files
│   ├── test_api.py
│   ├── test_presets.py
│   └── test_fields.py
├── docs/                 # Documentation
├── requirements.txt      # Python dependencies
└── README.md
```

## Testing Guidelines

### What to Test

1. **API Endpoints**: All request/response scenarios
2. **Preset Management**: CRUD operations, validation
3. **Field Operations**: Add, edit, delete fields
4. **Error Handling**: Invalid inputs, API failures
5. **Edge Cases**: Empty data, large files, special characters

### Writing Tests

```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_preset(client):
    """Test preset creation endpoint."""
    response = client.post('/api/presets', json={
        'preset_type': 'photorealistic',
        'preset_name': 'Test Preset',
        'prompt_fields': []
    })
    assert response.status_code == 200
    assert 'preset_id' in response.json
```

## Documentation

When adding features, update relevant documentation:

- **README.md**: User-facing features
- **docs/specs.md**: API changes
- **docs/design.md**: UI component changes
- **Inline comments**: Complex logic explanations

## Review Process

All submissions require review. We use GitHub pull requests for this purpose:

1. **Automated checks** must pass (tests, linting)
2. **Code review** by at least one maintainer
3. **Documentation review** if docs are changed
4. **Testing** in local environment

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

## Questions?

Feel free to:
- Open an issue with the `question` label
- Join our discussions on GitHub
- Email the maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
