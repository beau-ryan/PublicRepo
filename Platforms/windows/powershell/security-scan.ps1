# Antivirus Script
# for real time antivirus scanning
# and other system utilities
# Windows System Operations Menu (PowerShell)
function Show-Menu {
    
    Write-Host "==============================================="
    Write-Host "   _      _             _         _           "
    Write-Host "  | |    (_)           | |       | |          "
    Write-Host "  | |     _ _ __   __ _| |__  ___| |__   ___  "
    Write-Host "  | |    | | '_ \ / _` | '_ \/ __| '_ \ / _ \ "
    Write-Host "  | |____| | | | | (_| | | | \__ \ | | |  __/ "
    Write-Host "  |______|_|_| |_|\__, |_| |_|___/_| |_|\___| "
    Write-Host "                   __/ |                      "
    Write-Host "                  |___/                       "
    Write-Host "==============================================="
    Write-Host "      Virus Operations Menu           "
    Write-Host "==============================================="
    Write-Host "`n=== Virus Operations Menu ==="
    Write-Host "1. Scan for viruses"
    Write-Host "2. Deep scan (custom path or all drives)"
    Write-Host "3. Update virus definitions"
    Write-Host "4. Schedule regular scans"
    Write-Host "5. Show quarantine"
    Write-Host "6. View scan logs"
    Write-Host "7. Deep scan network (ports/devices)"
    Write-Host "8. Email latest scan log"
    Write-Host "9. Exit"
    Write-Host "10. Run advanced threat detection"
    Write-Host "11. scan for code injections"
    Write-Host "12. Copy flagged files for VirusTotal upload"
    Write-Host "13. Exit"
    Write-Host "==============================================="
}