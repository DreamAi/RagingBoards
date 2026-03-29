Write-Host "💿 Building ISO..."

$source = "C:\Projects\RagingBoards"
$iso = "C:\Projects\RagingBoards.iso"

if (!(Get-Command oscdimg -ErrorAction SilentlyContinue)) {
    Write-Host "Install Windows ADK for oscdimg"
    exit
}

oscdimg -o -m $source $iso

Write-Host "✅ ISO created at $iso"
