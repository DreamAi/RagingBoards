Write-Host "📦 Installing project dependencies..."

if (Test-Path "package.json") {
    npm install
}

if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
}

Write-Host "✅ Installation complete"
