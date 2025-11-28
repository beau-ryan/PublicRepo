# PowerShell Menu Color Guide

## Quick Reference - Color Codes Used

### ANSI Color Escape Codes for PowerShell

```powershell
$esc = [char]27

# Basic Colors (Standard)
$reset     = "$esc[0m"     # Reset all formatting
$bold      = "$esc[1m"     # Bold/Bright text
$red       = "$esc[31m"    # Red
$green     = "$esc[32m"    # Green
$yellow    = "$esc[33m"    # Yellow
$blue      = "$esc[34m"    # Blue
$magenta   = "$esc[35m"    # Magenta/Purple
$cyan      = "$esc[36m"    # Cyan
$white     = "$esc[37m"    # White

# Bright Colors (Enhanced)
$brightRed    = "$esc[91m" # Bright Red
$brightGreen  = "$esc[92m" # Bright Green
$brightYellow = "$esc[93m" # Bright Yellow
$brightBlue   = "$esc[94m" # Bright Blue
$brightMagenta= "$esc[95m" # Bright Magenta
$brightCyan   = "$esc[96m" # Bright Cyan
$brightWhite  = "$esc[97m" # Bright White
```

## Color Usage in the Menu

| Element | Color | Purpose |
|---------|-------|---------|
| Menu Numbers (1-8) | `$green` | Standard operations |
| Menu Numbers (9-13) | `$yellow` | Important/Advanced operations |
| Menu Numbers (14-17) | `$cyan` | Analysis/Audit operations |
| Exit Option (0) | `$brightRed` | Critical action (exit) |
| Separators/Headers | `$brightCyan` + `$bold` | Visual hierarchy |
| Text Output | Various | Status/Information display |

## Implementation Example

```powershell
# Simple colored text
Write-Host "$green[1]$reset  Menu Option"

# Combine bold + color
Write-Host "$bold$cyan==================$reset"

# With dynamic content
Write-Host "$yellow[*] Processing: $item$reset"
```

## How to Test

Run the script in PowerShell:

```powershell
. 'F:\My local Repo\PublicRepo\Platforms\windows\powershell\security-scan.ps1'
```

You should see:

- ✅ Clean menu with proper line breaks
- ✅ Green numbered options (1-8)
- ✅ Yellow numbered options (9-13)
- ✅ Cyan numbered options (14-17)
- ✅ Bright red EXIT option
- ✅ Cyan borders and headers

## Troubleshooting

If colors don't display:

1. Ensure you're using PowerShell 7.0+ or Windows PowerShell with ANSI support enabled
2. Check that `$esc = [char]27` is defined at the top of the script
3. Use backticks for escape sequences in some terminals: `` `e[31m ``

## Color Codes Reference Chart

```plaintext
Standard Colors:        Bright Colors:
30 = Black              90 = Bright Black
31 = Red                91 = Bright Red
32 = Green              92 = Bright Green
33 = Yellow             93 = Bright Yellow
34 = Blue               94 = Bright Blue
35 = Magenta            95 = Bright Magenta
36 = Cyan               96 = Bright Cyan
37 = White              97 = Bright White

Modifiers:
0 = Reset/Normal
1 = Bold/Bright
4 = Underline
7 = Reverse/Invert
```

Format: `$esc[MODIFIERmTEXT$esc[0m`
Example: `$esc[1;32m` = Bold Green
