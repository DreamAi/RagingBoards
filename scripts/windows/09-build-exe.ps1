Write-Host "🖥️ Building EXE installer..."

Install-Module -Name ps2exe -Force -Scope CurrentUser

Invoke-ps2exe `
    -inputFile ".\installer\raging-installer.ps1" `
    -outputFile ".\installer\RagingBoardsInstaller.exe" `
    -noConsole

Write-Host "✅ EXE created: installer\RagingBoardsInstaller.exe"
