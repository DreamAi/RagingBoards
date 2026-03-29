Add-Type -AssemblyName System.Windows.Forms

[System.Windows.Forms.MessageBox]::Show("Installing Raging Boards...")

# Run setup
Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File scripts\windows\ps\01-setup.ps1" -Wait

# Build repo
Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File scripts\windows\ps\03-build-repo.ps1" -Wait

# Install deps
Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File scripts\windows\ps\02-install.ps1" -Wait

# Deploy
Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File scripts\windows\ps\05-deploy.ps1" -Wait

# Launch
Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File scripts\windows\ps\04-launch.ps1"

[System.Windows.Forms.MessageBox]::Show("Raging Boards Installed Successfully!")
