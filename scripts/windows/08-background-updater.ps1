Write-Host "🤖 Starting background updater..."

while ($true) {
    Write-Host "Checking updates..."
    powershell -ExecutionPolicy Bypass -File .\06-auto-update.ps1

    Write-Host "Sleeping 10 minutes..."
    Start-Sleep -Seconds 600
}
