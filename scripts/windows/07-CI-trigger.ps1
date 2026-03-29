Write-Host "🚀 Triggering CI/CD..."

git add .
git commit -m "Auto update commit"
git push origin main

Write-Host "✅ CI/CD Pipeline Triggered (GitHub Actions)"
