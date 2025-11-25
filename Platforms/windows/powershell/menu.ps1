# Helper function for menu selection
function menu_selection {
    param([string]$prompt)
    Write-Host $prompt -NoNewline
    return Read-Host
}
# Windows Menu Script
# This script provides a menu-driven interface to download and install various development tools on Windows.


. "$PSScriptRoot\tools.ps1"

# Define the path to store downloaded tools
$toolsPath = "$env:USERPROFILE\PublicRepo\MySyS\DevTools"
# Ensure the tools directory exists
if (-Not (Test-Path -Path $toolsPath)) {
    New-Item -ItemType Directory -Path $toolsPath | Out-Null
}

# Display menu and handle user input

function Show-Tool-List {
    Write-Host "Available Development Tools:" -ForegroundColor Green
    for ($i = 0; $i -lt $tools.Count; $i++) {
        $toolUrl = $tools[$i]
        $toolName = ($toolUrl -split "/")[-1]
           Write-Host "$($i + 1). $toolName"
    }
}
function Show-Menu {
    Clear-Host
    Write-Host "==============================" -ForegroundColor Green
    Write-Host " Development Tools Installer " -ForegroundColor Red
    Write-Host "==============================" -ForegroundColor Green
    Write-Host "1. Download All Development Tools"
    Write-Host "2. Pick a tool to install by number:"
    Write-Host "3. Run Full Windows Setup (setup.ps1)"
    Write-Host "4. Exit"
    Write-Host "==============================" -ForegroundColor Green
}
while ($true) {
    Show-Menu
    $choice = menu_selection "Enter your choice (1-4): "
    switch ($choice) {
        "1" {
            Write-Host "Downloading all development tools..." -ForegroundColor Cyan
            foreach ($toolUrl in $tools) {
                $filename = ($toolUrl -split "/")[-1]
                $destinationPath = Join-Path -Path $toolsPath -ChildPath $filename
                if (-Not (Test-Path -Path $destinationPath)) {
                    try {
                        Invoke-WebRequest -Uri $toolUrl -OutFile $destinationPath
                        Write-Host "Downloaded: $filename" -ForegroundColor Green
                    } catch {
                        Write-Host ("Failed to download " + $filename + ": " + $error[0].Exception.Message) -ForegroundColor Red
                    }
                } else {
                    Write-Host "$filename already exists. Skipping download." -ForegroundColor Yellow
                }
            }
            Write-Host "All tools downloaded to $toolsPath" -ForegroundColor Green
            Read-Host "Press Enter to continue..."
        }
        "2" {
            Show-Tool-List
            $toolChoice = menu_selection "Enter the tool number to download (or 'b' to go back): "
            if ($toolChoice -eq 'b') { continue }
            if ($toolChoice -match '^\d+$' -and [int]$toolChoice -ge 1 -and [int]$toolChoice -le $tools.Count) {
                $selectedToolUrl = $tools[[int]$toolChoice - 1]
                $filename = ($selectedToolUrl -split "/")[-1]
                $destinationPath = Join-Path -Path $toolsPath -ChildPath $filename
                if (-Not (Test-Path -Path $destinationPath)) {
                    try {
                        Invoke-WebRequest -Uri $selectedToolUrl -OutFile $destinationPath
                        Write-Host "Tool downloaded to $toolsPath" -ForegroundColor Green
                    } catch {
                        Write-Host ("Failed to download " + $filename + ": " + $error[0].Exception.Message) -ForegroundColor Red
                    }
                } else {
                    Write-Host "$filename already exists. Skipping download." -ForegroundColor Yellow
                }
                Read-Host "Press Enter to continue..."
            } else {
                Write-Host "Invalid selection. Please try again." -ForegroundColor Red
                Read-Host "Press Enter to continue..."
            }
        }
        "3" {
            Write-Host "Running full Windows setup script..." -ForegroundColor Cyan
            $scriptPath = "$PSScriptRoot\setup.ps1"
            if (Test-Path -Path $scriptPath) {
                & $scriptPath
            } else {
                Write-Host "Setup script not found at $scriptPath" -ForegroundColor Red
            }
            Read-Host "Press Enter to continue..."
        }
        "4" {
            Write-Host "Exiting..." -ForegroundColor Cyan
            break
        }   
        Default {
            Write-Host "Invalid choice. Please select a valid option." -ForegroundColor Red
            Read-Host "Press Enter to continue..."
        }
    }
}
