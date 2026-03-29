Write-Host "🚀 Launching app..."

Start-Process powershell -ArgumentList "uvicorn backend.main_api:app --reload"

Start-Sleep -Seconds 5
Start-Process "http://127.0.0.1:8000/docs"
