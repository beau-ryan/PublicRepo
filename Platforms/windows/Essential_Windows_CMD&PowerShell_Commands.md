# Essential Windows CMD and PowerShell Commands

## Getting Started

Windows has two main command-line interfaces

- **CMD (Command Prompt)**: Classic Windows shell for basic commands and scripting.
- **PowerShell**: Advanced shell for automation, scripting, and system management.

---

## Common CMD Commands

### Navigation & File Management

- `dir` — List files and folders
- `cd <folder>` — Change directory
- `cls` — Clear the screen
- `copy <src> <dest>` — Copy files
- `move <src> <dest>` — Move/rename files
- `del <file>` — Delete files
- `mkdir <folder>` — Create directory
- `rmdir <folder>` — Remove directory
- `type <file>` — View file contents
- `ren <old> <new>` — Rename file

### System Info & Management

- `systeminfo` — Show system information
- `hostname` — Show computer name
- `ver` — Show Windows version
- `echo %USERNAME%` — Show current user
- `tasklist` — List running processes
- `taskkill /PID <pid> /F` — Kill process by PID
- `chkdsk` — Check disk for errors
- `ipconfig` — Show network info
- `ping <host>` — Test network connection
- `netstat -an` — Show open ports
- `shutdown /r /t 0` — Restart computer
- `shutdown /s /t 0` — Shutdown computer

### Networking
- `arp -a` — Show ARP table
- `nslookup <host>` — DNS lookup
- `tracert <host>` — Trace route
- `net use` — List network shares
- `net user` — List user accounts
- `net localgroup` — List local groups

### Disk & File Utilities
- `diskpart` — Disk partition tool
- `format <drive>` — Format drive
- `sfc /scannow` — System file checker
- `attrib <file>` — Change file attributes

---

## Common PowerShell Commands

### Navigation & File Management
- `Get-ChildItem` — List files and folders (alias: `ls`)
- `Set-Location <folder>` — Change directory (alias: `cd`)
- `Clear-Host` — Clear the screen (alias: `cls`)
- `Copy-Item <src> <dest>` — Copy files
- `Move-Item <src> <dest>` — Move/rename files
- `Remove-Item <file>` — Delete files
- `New-Item -ItemType Directory -Path <folder>` — Create directory
- `Get-Content <file>` — View file contents
- `Rename-Item <old> <new>` — Rename file

### System Info & Management
- `Get-ComputerInfo` — Show system information
- `Get-Process` — List running processes
- `Stop-Process -Id <pid>` — Kill process by PID
- `Get-Service` — List services
- `Start-Service <name>` — Start service
- `Stop-Service <name>` — Stop service
- `Restart-Computer` — Restart computer
- `Get-EventLog -LogName System -Newest 20` — View system logs
- `Get-LocalUser` — List local users
- `Get-LocalGroup` — List local groups
- `Get-Date` — Show current date/time
- `Get-Host` — Show PowerShell version

### Networking
- `Test-Connection <host>` — Ping (like `ping` in CMD)
- `Get-NetIPAddress` — Show IP addresses
- `Get-NetTCPConnection` — Show open TCP connections
- `Resolve-DnsName <host>` — DNS lookup
- `Get-NetAdapter` — Show network adapters
- `Get-NetRoute` — Show network routes

### Disk & File Utilities
- `Get-Volume` — List disk volumes
- `Get-Partition` — List disk partitions
- `Format-Volume -DriveLetter <drive>` — Format drive
- `Repair-Volume -DriveLetter <drive>` — Repair disk
- `Get-ItemProperty <file>` — Show file properties
- `Set-ItemProperty <file> -Name IsReadOnly -Value $true` — Set file as read-only

### Scripting & Automation
- `Get-Help <command>` — Show help for a command
- `Get-Command` — List all available commands
- `Start-Job` — Run background jobs
- `Invoke-WebRequest <url>` — Download web content
- `ForEach-Object { ... }` — Loop over items
- `Where-Object { ... }` — Filter items

---

## Advanced CMD and PowerShell Options

### CMD Advanced
- `for /f "tokens=*" %i in (file.txt) do echo %i` — Loop through lines in a file
- `set VAR=value` — Set environment variable
- `call :label` — Call a subroutine in a batch file
- `start <program>` — Launch a program or script
- `schtasks /create ...` — Schedule tasks
- `reg query <key>` — Query Windows registry
- `wmic process list brief` — Query system info with WMI
- `xcopy <src> <dest> /E /H /C /I` — Advanced file copy
- `robocopy <src> <dest> /MIR` — Robust file copy and sync

### PowerShell Advanced
- `Invoke-Command -ComputerName <host> -ScriptBlock { ... }` — Run commands remotely
- `Enter-PSSession <host>` — Start interactive remote session
- `New-ScheduledTaskTrigger` — Create scheduled tasks
- `Register-ScheduledTask` — Register scheduled tasks
- `Get-WmiObject -Class Win32_OperatingSystem` — Query WMI objects
- `Export-Csv <file>` — Export data to CSV
- `Import-Csv <file>` — Import data from CSV
- `Send-MailMessage` — Send email from PowerShell
- `Try { ... } Catch { ... }` — Error handling in scripts
- `Write-Output`, `Write-Error`, `Write-Host` — Output and logging
- `Measure-Command { ... }` — Measure script execution time
- `Set-ExecutionPolicy RemoteSigned` — Allow running scripts

### Troubleshooting & Diagnostics
- `Get-WinEvent -LogName Application` — View event logs
- `Get-Process | Where-Object { $_.CPU -gt 100 }` — Find high CPU processes
- `Test-Path <path>` — Check if a file or folder exists
- `Resolve-DnsName <host>` — Advanced DNS lookup
- `Get-NetFirewallRule` — List firewall rules
- `Get-Module` — List loaded modules

---

## Tips for Using CMD and PowerShell
- Use `Tab` for auto-completion of commands and filenames.
- Use `help <command>` in CMD or `Get-Help <command>` in PowerShell for built-in help.
- Use `exit` to close the terminal.
- PowerShell supports aliases for many CMD commands (e.g., `ls`, `cd`, `cls`).
- PowerShell scripts use `.ps1` extension; CMD batch files use `.bat` or `.cmd`.

---

## Explanations
- **Remote Management**: PowerShell can manage remote systems using WinRM, SSH, or CIM sessions. Use `Invoke-Command` and `Enter-PSSession` for remote tasks.
- **Scripting & Automation**: Use loops (`ForEach-Object`, `for`), error handling (`Try/Catch`), and scheduled tasks for automation.
- **Data Export/Import**: Use `Export-Csv` and `Import-Csv` to work with tabular data.
- **Diagnostics**: Use event logs, process monitoring, and firewall rules to troubleshoot issues.
- **Security**: Use `Set-ExecutionPolicy` to control script permissions. Always review scripts before running from the internet.

For more advanced scenarios, see [PowerShell Gallery](https://www.powershellgallery.com/) and [Microsoft Docs](https://docs.microsoft.com/powershell/).

---

## Useful Resources
- [Windows Command Line Documentation](https://docs.microsoft.com/windows-server/administration/windows-commands/windows-commands)
- [PowerShell Documentation](https://docs.microsoft.com/powershell/)
- [Windows Client Documentation](https://learn.microsoft.com/en-us/windows/resources/)

---

This guide covers the most useful commands for everyday Windows administration, scripting, and troubleshooting. For advanced usage, see the official documentation links above.
