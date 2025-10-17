# Nano-Banana Studio - Installation Script (Windows)

Write-Host "🍌 Nano-Banana Studio - Installation Script" -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Green
Write-Host ""

# Check Python version
Write-Host "Checking Python version..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python 3 is not installed. Please install Python 3.10 or higher." -ForegroundColor Red
    exit 1
}
Write-Host ""

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv .venv
Write-Host "✓ Virtual environment created" -ForegroundColor Green
Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\.venv\Scripts\Activate.ps1
Write-Host "✓ Virtual environment activated" -ForegroundColor Green
Write-Host ""

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
python -m pip install --upgrade pip
pip install -r requirements.txt
Write-Host "✓ Dependencies installed" -ForegroundColor Green
Write-Host ""

# Create .env file if it doesn't exist
if (-Not (Test-Path .env)) {
    Write-Host "Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "✓ .env file created" -ForegroundColor Green
    Write-Host ""
    Write-Host "⚠️  IMPORTANT: Please edit .env and add your GEMINI_API_KEY" -ForegroundColor Yellow
    Write-Host ""
} else {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
    Write-Host ""
}

# Check if API key is set
if (Test-Path .env) {
    $envContent = Get-Content .env -Raw
    if ($envContent -match "your-gemini-api-key-here") {
        Write-Host "⚠️  WARNING: API key not configured in .env file" -ForegroundColor Yellow
        Write-Host "   Please edit .env and replace 'your-gemini-api-key-here' with your actual API key" -ForegroundColor Yellow
        Write-Host "   Get your API key at: https://ai.google.dev/" -ForegroundColor Cyan
        Write-Host ""
    } else {
        Write-Host "✓ API key appears to be configured" -ForegroundColor Green
        Write-Host ""
    }
}

Write-Host "==============================================" -ForegroundColor Green
Write-Host "✓ Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "To start Nano-Banana Studio:" -ForegroundColor Cyan
Write-Host "  1. Activate the virtual environment: .\.venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "  2. Make sure your API key is in .env" -ForegroundColor White
Write-Host "  3. Run: python app.py" -ForegroundColor White
Write-Host "  4. Open: http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "For help, visit: https://github.com/yourusername/nano-banana" -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Green
