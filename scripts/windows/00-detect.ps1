Write-Host "🔍 Detecting system..."

function Check-Command($name) {
    if (Get-Command $name -ErrorAction SilentlyContinue) {
        Write-Host "✅ $name installed"
        return $true
    } else {
        Write-Host "❌ $name missing"
        return $false
    }
}

$python = Check-Command "python"
$pip = Check-Command "pip"
$node = Check-Command "node"
$npm = Check-Command "npm"
$docker = Check-Command "docker"
$git = Check-Command "git"

Write-Host "Detection complete"
