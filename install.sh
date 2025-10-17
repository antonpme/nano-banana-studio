#!/bin/bash
# Nano-Banana Studio - Installation Script (macOS/Linux)

set -e  # Exit on error

echo "🍌 Nano-Banana Studio - Installation Script"
echo "=============================================="
echo ""

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✓ Found Python $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv
echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Please edit .env and add your GEMINI_API_KEY"
    echo ""
else
    echo "✓ .env file already exists"
    echo ""
fi

# Check if API key is set
if [ -f .env ]; then
    if grep -q "your-gemini-api-key-here" .env; then
        echo "⚠️  WARNING: API key not configured in .env file"
        echo "   Please edit .env and replace 'your-gemini-api-key-here' with your actual API key"
        echo "   Get your API key at: https://ai.google.dev/"
        echo ""
    else
        echo "✓ API key appears to be configured"
        echo ""
    fi
fi

echo "=============================================="
echo "✓ Installation complete!"
echo ""
echo "To start Nano-Banana Studio:"
echo "  1. Activate the virtual environment: source .venv/bin/activate"
echo "  2. Make sure your API key is in .env"
echo "  3. Run: python app.py"
echo "  4. Open: http://localhost:5000"
echo ""
echo "For help, visit: https://github.com/yourusername/nano-banana"
echo "=============================================="
