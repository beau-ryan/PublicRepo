###############################################################
# DEMO VERSION NOTICE
# This script is a demo. For real use, customize the menu and
# add project file paths or automation as needed.
# Example: Add more options for specific projects, scripts, or tools.
###############################################################
Write-Host "\n[DEMO VERSION] This menu is for demonstration only."
# PowerShell Project Runner Menu

function Show-Menu {
    Write-Host "`n=== Project Runner Menu (Demo) ==="
    Write-Host "1. Run a Project File (manual path)"
    Write-Host "2. Exit"
}

while ($true) {
    Show-Menu
    $choice = Read-Host "Select an option (1-2)"
    switch ($choice) {
        "1" {
            $filePath = Read-Host "Enter the full path to the project file you want to run (demo: manual entry)"
            if (Test-Path $filePath) {
                Write-Host "[DEMO] Running file: $filePath"
                try {
                    & $filePath
                } catch {
                    Write-Host "Error running file: $_"
                }
            } else {
                Write-Host "File not found: $filePath"
            }
        }
    "2" { Write-Host "Exiting Project Runner Menu (Demo)."; exit }
    default { Write-Host "Invalid option. Please select 1 or 2." }
    }
}
Write-Host "Exiting Project Runner Menu (Demo)."