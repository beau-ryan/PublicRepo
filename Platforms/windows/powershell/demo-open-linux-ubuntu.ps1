$Warning = @'
###############################################################
# DEMO VERSION NOTICE
# This script is a demo. To make it run, you must update the
# $linuxPath, $ubuntuPath, $ubuntu22Path, and $kaliPath variables
# below with the actual paths to your installed WSL distributions.
# Example: $ubuntuPath = "$env:LOCALAPPDATA\Microsoft\WindowsApps\ubuntu.exe"
###############################################################
'@
Write-Host $Warning -ForegroundColor Yellow
# Open Linux, Ubuntu, Ubuntu 22.04, or Kali Linux Terminal Menu
$esc = [char]27
$yellow = "$esc[33m"
$green = "$esc[32m"
$blue = "$esc[34m"
$red = "$esc[31m"
$reset = "$esc[0m"

while ($true) {
    Write-Host "${yellow}=====================================" -NoNewline; Write-Host $reset
    Write-Host "${green}   Open Linux/Ubuntu/Kali Terminal     " -NoNewline; Write-Host $reset
    Write-Host "${yellow}=====================================" -NoNewline; Write-Host $reset

    $linuxPath = "$env:LOCALAPPDATA\path\to\your\custom\linux.exe"  # Change this to your custom Linux executable path if any
    # Common WSL distributions
    $ubuntuPath = "$env:LOCALAPPDATA\path\to\your\custom\ubuntu.exe"  # Change this to your custom Ubuntu executable path if any
    $ubuntu22Path = "$env:LOCALAPPDATA\path\to\your\custom\ubuntu2204.exe"  # Change this to your custom Ubuntu 22.04 executable path if any
    $kaliPath = "$env:LOCALAPPDATA\path\to\your\custom\kali.exe"  # Change this to your custom Kali Linux executable path if any

    $linuxExists = Test-Path $linuxPath
    $ubuntuExists = Test-Path $ubuntuPath
    $ubuntu22Exists = Test-Path $ubuntu22Path
    $kaliExists = Test-Path $kaliPath

    $option = 1
    $optMap = @{
    }
    if ($linuxExists) {
        Write-Host "${blue}$option. Open Linux Terminal$reset"
        $optMap[$option] = @{cmd=$linuxPath; fallback="Ubuntu"}
        $option++
    } else {
        Write-Host "${blue}$option. Open Linux Terminal (fallback)$reset"
        $optMap[$option] = @{cmd=$null; fallback="Ubuntu"}
        $option++
    }
    if ($ubuntuExists) {
        Write-Host "${blue}$option. Open Ubuntu 18.04 Terminal$reset"
        $optMap[$option] = @{cmd=$ubuntuPath}
        $option++
    }
    if ($ubuntu22Exists) {
        Write-Host "${blue}$option. Open Ubuntu 22.04 Terminal$reset"
        $optMap[$option] = @{cmd=$ubuntu22Path}
        $option++
    }
    if ($kaliExists) {
        Write-Host "${blue}$option. Open Kali Linux Terminal$reset"
        $optMap[$option] = @{cmd=$kaliPath; fallback="kali-linux"}
        $option++
    } else {
        Write-Host "${blue}$option. Open Kali Linux Terminal (fallback)$reset"
        $optMap[$option] = @{cmd=$null; fallback="kali-linux"}
        $option++
    }
    Write-Host "${yellow}$option. Exit$reset"
    Write-Host "${yellow}=====================================${reset}"
    Write-Host "${green}Select an option (1-$option):${reset}"
    Write-Host "${yellow}Type the number to launch, or select Exit to cancel.${reset}"

    $choice = Read-Host "${blue}Select an option${reset}"
    $choiceNum = [int]$choice
    if ($choiceNum -eq $option) {
        Write-Host "${green}Exiting...${reset}"
        break
    } elseif ($optMap.ContainsKey($choiceNum)) {
        $entry = $optMap[$choiceNum]
        if ($entry.cmd) {
            Write-Host "${green}Launching...${reset}"
            Start-Process $entry.cmd
        } elseif ($entry.fallback) {
            Write-Host "${green}Launching (fallback)...${reset}"
            Start-Process "wsl.exe" -ArgumentList "-d $($entry.fallback)"
        } else {
            Write-Host "${red}Invalid option or executable not found.${reset}"
        }
        continue
    }
    Write-Host "${red}Invalid option or executable not found.${reset}"
}