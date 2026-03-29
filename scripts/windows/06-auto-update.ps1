Write-Host "🔄 Checking for updates..."

if (!(Test-Path ".git")) {
    Write-Host "❌ Not a git repo"
    exit
}

git fetch origin

$local = git rev-parse HEAD
$remote = git rev-parse origin/main

if ($local -ne $remote) {
    Write-Host "🚀 Updating system..."

    git pull origin main

    Write-Host "📦 Reinstalling dependencies..."
    if (Test-Path "package.json") { npm install }
    if (Test-Path "requirements.txt") { pip install -r requirements.txt }

    Write-Host "🐳 Restarting containers..."
    docker compose down
    docker compose up -d

    Write-Host "✅ System updated"
} else {
    Write-Host "✔ Already up to date"
}
