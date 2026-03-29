Write-Host "🏗️ Building repo structure..."

mkdir backend -Force
mkdir apps\web -Force

New-Item backend\__init__.py -ItemType File -Force

@"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API running"}
"@ | Out-File backend\main_api.py

Write-Host "✅ Repo structure created"
