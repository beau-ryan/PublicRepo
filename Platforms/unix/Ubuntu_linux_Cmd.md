# Essential Kali Linux Commands

## Navigation & System Info

- `pwd` — Show current directory

- `ls` — List files and folders

- `cd <folder>` — Change directory

- `tree` — Show directory tree

- `find <path> -name <filename>` — Search for files

- `whoami` — Show your username

- `uname -a` — Show system info

- `cat /etc/os-release` — Show distro version

- `history` — Show command history

### File Operations

- `cp <src> <dest>` — Copy files

- `mv <src> <dest>` — Move/rename files

- `rm <file>` — Delete files

- `touch <file>` — Create empty file

- `mkdir <folder>` — Create directory

- `nano <file>` — Edit file in terminal

- `cat <file>` — View file contents

- `less <file>` — View file with paging

- `rm -rf <foldername>` - deletes folders

### Package Management

- `sudo apt update` — Update package list

- `sudo apt upgrade` — Upgrade all packages

- `sudo apt install <package>` — Install a package

- `sudo apt remove <package>` — Remove a package

- `apt search <term>` — Search for packages

- `dpkg --get-selections | grep kali` — List installed Kali tools

### Networking
- `ip a` — Show network interfaces

- `ping <host>` — Test network connection

- `ifconfig` — Show IP info (may need: `sudo apt install net-tools`)

- `nmap <target>` — Network scan (Kali comes with nmap)

- `netstat -tulnp` — Show open ports

- `curl <url>` — Download web content

### Security Tools (Kali highlights)
- `msfconsole` — Start Metasploit Framework
- `nmap` — Network scanner
- `hydra` — Password cracker
- `john` — John the Ripper (password cracker)
- `airmon-ng` — Wireless monitoring
- `burpsuite` — Web vulnerability scanner (GUI)
- `sqlmap` — SQL injection tool
- `wireshark` — Network protocol analyzer (GUI)
- `nikto` — Web server scanner
- `enum4linux` — Windows/Samba enumeration
- `dirb` — Web content scanner
- `wpscan` — WordPress vulnerability scanner

### System Management
- `sudo reboot` — Restart system
- `sudo shutdown now` — Shutdown
- `df -h` — Disk usage
- `top` — System resource monitor
- `htop` — Advanced resource monitor (may need: `sudo apt install htop`)
- `ps aux` — List running processes
- `kill <pid>` — Kill process by PID
- `free -h` — Show memory usage

### User & Permissions
- `sudo` — Run command as root
- `adduser <username>` — Add user
- `passwd <username>` — Change password
- `chmod <mode> <file>` — Change file permissions
- `chown <user>:<group> <file>` — Change file owner
- `groups` — Show group memberships

### Useful Navigation Tips
- Use `Tab` for auto-completion of commands and filenames.
- Use `Ctrl+R` to search your command history.
- Use `man <command>` to read the manual for any command (e.g., `man nmap`).
- Use `clear` to clear the terminal screen.
- Use `exit` to leave the terminal or WSL session.

---

## Categories of Kali Tools
Kali Linux tools are organized by category. Some popular categories:
- **Information Gathering**: nmap, dnsenum, theHarvester
- **Vulnerability Analysis**: nikto, wpscan, sqlmap
- **Web Application Analysis**: burpsuite, zaproxy
- **Password Attacks**: hydra, john, medusa
- **Wireless Attacks**: aircrack-ng, reaver
- **Exploitation Tools**: metasploit, armitage
- **Sniffing & Spoofing**: wireshark, ettercap
- **Forensics**: autopsy, sleuthkit
- **Reporting Tools**: dradis, magicTree

To see all tools:
- Visit [Kali Tools List](https://tools.kali.org/tools-list)
- Or run:
  ```bash
  dpkg --get-selections | grep kali
  ```

---

## Tips for Using Kali Linux on Windows 10
- You can access your Windows files from `/mnt/c/Users/<yourname>` inside Kali.
- Use `sudo` for admin tasks.
- Most Kali tools work in WSL, but some (like wireless tools) may need a full VM or live USB.
- For a GUI, use `sudo apt install kali-desktop-xfce` and an X server for Windows (like X410 or VcXsrv).
- For more info, see [Kali Linux WSL Docs](https://www.kali.org/docs/wsl/win-kex/).
- For official documentation, visit [Kali Linux Docs](https://www.kali.org/docs/).

---

## Getting Help
- Use `man <command>` for built-in help.
- Use `--help` with most tools (e.g., `nmap --help`).
- Visit [Kali Linux Documentation](https://www.kali.org/docs/)

---

## Advanced Kali Linux Options

### Scripting & Automation
- `bash script.sh` — Run a shell script
- `for i in {1..10}; do echo $i; done` — Loop in shell
- `if [ -f file ]; then ...; fi` — Conditional statements
- `crontab -e` — Edit scheduled tasks (cron jobs)
- `at <time>` — Run a command at a specific time
- `systemctl enable <service>` — Enable service at boot
- `journalctl -xe` — View system logs

### Remote Management
- `ssh <user>@<host>` — Connect to remote server
- `scp <src> <user>@<host>:<dest>` — Secure copy files
- `rsync -avz <src> <user>@<host>:<dest>` — Sync files remotely
- `ssh-keygen` — Generate SSH keys
- `ssh-copy-id <user>@<host>` — Copy SSH key to remote host

### Troubleshooting & Diagnostics
- `dmesg | less` — View kernel messages
- `journalctl -xe` — View system logs
- `systemctl status <service>` — Check service status
- `top` / `htop` — Monitor system resources
- `strace <command>` — Trace system calls
- `lsof -i` — List open network files/ports
- `ping`, `traceroute`, `nslookup` — Network diagnostics

### Security & Permissions
- `ufw status` — Check firewall status
- `sudo ufw enable` — Enable firewall
- `sudo ufw allow <port>` — Allow port through firewall
- `chmod`, `chown`, `groups` — Manage permissions
- `sudo visudo` — Edit sudoers file
- `sudo adduser <user> sudo` — Add user to sudo group

### Advanced Security Tools
- `aircrack-ng` — Wireless security auditing
- `ettercap` — Network sniffing and MITM
- `autopsy` — Digital forensics
- `msfvenom` — Payload generator (Metasploit)
- `beef-xss` — Browser exploitation framework
- `hashcat` — Advanced password cracking
- `maltego` — Data mining and link analysis
- `social-engineer-toolkit` — Social engineering attacks

---

## Explanations
- **Scripting & Automation**: Use shell scripts, loops, and cron jobs to automate tasks. Scripts can be run with `bash script.sh` or made executable with `chmod +x script.sh`.
- **Remote Management**: Use SSH for secure remote access and file transfer. Set up SSH keys for passwordless login.
- **Troubleshooting**: Use system logs, resource monitors, and network tools to diagnose issues.
- **Security**: Use UFW to manage firewall rules. Use permissions and groups to control access. Kali includes advanced tools for penetration testing, forensics, and exploitation.
- **Tool Usage**: Many Kali tools have their own manuals (`man <tool>`) and help options (`tool --help`).

For more advanced scenarios, see [Kali Linux Documentation](https://www.kali.org/docs/) and [Kali Tools List](https://tools.kali.org/tools-list).

---

## Finding Phones and Routers on Your Network

You can use Kali Linux tools to discover phones, routers, and other devices on your network:

### Quick Device Discovery
- Use `nmap` to scan your local network for active devices:
  ```bash
  nmap -sn 192.168.1.0/24
  ```
  This will show all devices responding to ping on your network. Adjust the subnet as needed.

### Identify Device Types
- Use `nmap` with OS and service detection:
  ```bash
  nmap -O -sV 192.168.1.0/24
  ```
  This attempts to identify operating systems and services (may require root).

### Find Routers and Phones
- Routers often have web interfaces on ports 80/443. Scan for these:
  ```bash
  nmap -p 80,443 192.168.1.0/24
  ```
- Phones may show up with Android, iOS, or manufacturer info in nmap results.
- Use `arp -a` to list devices by IP and MAC address:
  ```bash
  arp -a
  ```
- Use `netdiscover` (install with `sudo apt install netdiscover`) for passive discovery:
  ```bash
  sudo netdiscover
  ```

### Example Project: Scan and Identify All Devices
1. Run a ping scan:
   ```bash
   nmap -sn 192.168.1.0/24
   ```
2. Run a service/OS scan:
   ```bash
   sudo nmap -O -sV 192.168.1.0/24
   ```
3. Review results for phones (Android/iOS) and routers (web interfaces, manufacturer info).
4. Use MAC address info from `arp -a` or `netdiscover` to help identify device types.

---

# Essential Ubuntu Linux Commands

## Getting Started
Ubuntu is a popular Linux distribution for desktops, servers, and WSL. These commands help you navigate, manage files, install software, and troubleshoot your system.

---

## Navigation & File Management
- `pwd` — Show current directory
- `ls` — List files and folders
- `cd <folder>` — Change directory
- `tree` — Show directory tree
- `find <path> -name <filename>` — Search for files
- `cp <src> <dest>` — Copy files
- `mv <src> <dest>` — Move/rename files
- `rm <file>` — Delete files
- `touch <file>` — Create empty file
- `mkdir <folder>` — Create directory
- `nano <file>` — Edit file in terminal
- `cat <file>` — View file contents
- `less <file>` — View file with paging

---

## System Info & Management
- `uname -a` — Show system info
- `lsb_release -a` — Show Ubuntu version
- `whoami` — Show your username
- `hostname` — Show computer name
- `date` — Show current date/time
- `df -h` — Disk usage
- `free -h` — Memory usage
- `top` — System resource monitor
- `htop` — Advanced monitor (`sudo apt install htop`)
- `ps aux` — List running processes
- `kill <pid>` — Kill process by PID
- `uptime` — Show system uptime
- `reboot` — Restart system
- `shutdown now` — Shutdown system

---

## Package Management
- `sudo apt update` — Update package list
- `sudo apt upgrade` — Upgrade all packages
- `sudo apt install <package>` — Install a package
- `sudo apt remove <package>` — Remove a package
- `apt search <term>` — Search for packages
- `dpkg -l` — List installed packages
- `snap install <package>` — Install snap package

---

## Networking
- `ip a` — Show network interfaces
- `ping <host>` — Test network connection
- `ifconfig` — Show IP info (`sudo apt install net-tools`)
- `netstat -tuln` — Show open ports (`sudo apt install net-tools`)
- `curl <url>` — Download web content
- `wget <url>` — Download files
- `nmap <target>` — Network scan (`sudo apt install nmap`)
- `ssh <user>@<host>` — Connect to remote server

---

## User & Permissions
- `sudo` — Run command as root
- `adduser <username>` — Add user
- `passwd <username>` — Change password
- `chmod <mode> <file>` — Change file permissions
- `chown <user>:<group> <file>` — Change file owner
- `groups` — Show group memberships

---

## Disk & File Utilities
- `fdisk -l` — List disk partitions
- `mount` — Show mounted filesystems
- `umount <device>` — Unmount device
- `du -sh <folder>` — Show folder size
- `tar -czvf <archive.tar.gz> <folder>` — Create compressed archive
- `unzip <file.zip>` — Extract zip file (`sudo apt install unzip`)

---

## Useful Tips
- Use `Tab` for auto-completion of commands and filenames.
- Use `Ctrl+R` to search your command history.
- Use `man <command>` to read the manual for any command (e.g., `man apt`).
- Use `clear` to clear the terminal screen.
- Use `exit` to leave the terminal session.

---

## Getting Help
- Use `man <command>` for built-in help.
- Use `--help` with most tools (e.g., `apt --help`).
- Visit [Ubuntu Documentation](https://help.ubuntu.com/)
- Search for tutorials and guides on [Ubuntu Official Site](https://ubuntu.com/)

---

## Advanced Ubuntu Linux Options

### Scripting & Automation
- `bash script.sh` — Run a shell script
- `for i in {1..10}; do echo $i; done` — Loop in shell
- `if [ -f file ]; then ...; fi` — Conditional statements
- `crontab -e` — Edit scheduled tasks (cron jobs)
- `at <time>` — Run a command at a specific time
- `systemctl enable <service>` — Enable service at boot
- `journalctl -xe` — View system logs

### Remote Management
- `ssh <user>@<host>` — Connect to remote server
- `scp <src> <user>@<host>:<dest>` — Secure copy files
- `rsync -avz <src> <user>@<host>:<dest>` — Sync files remotely
- `ssh-keygen` — Generate SSH keys
- `ssh-copy-id <user>@<host>` — Copy SSH key to remote host

### Troubleshooting & Diagnostics
- `dmesg | less` — View kernel messages
- `journalctl -xe` — View system logs
- `systemctl status <service>` — Check service status
- `top` / `htop` — Monitor system resources
- `strace <command>` — Trace system calls
- `lsof -i` — List open network files/ports
- `ping`, `traceroute`, `nslookup` — Network diagnostics

### Security & Permissions
- `ufw status` — Check firewall status
- `sudo ufw enable` — Enable firewall
- `sudo ufw allow <port>` — Allow port through firewall
- `chmod`, `chown`, `groups` — Manage permissions
- `sudo visudo` — Edit sudoers file
- `sudo adduser <user> sudo` — Add user to sudo group

---

## Explanations
- **Scripting & Automation**: Use shell scripts, loops, and cron jobs to automate tasks. Scripts can be run with `bash script.sh` or made executable with `chmod +x script.sh`.
- **Remote Management**: Use SSH for secure remote access and file transfer. Set up SSH keys for passwordless login.
- **Troubleshooting**: Use system logs, resource monitors, and network tools to diagnose issues.
- **Security**: Use UFW to manage firewall rules. Use permissions and groups to control access.
- **Package Management**: Use `apt` for installing, updating, and removing software. Use `snap` for snap packages.

For more advanced scenarios, see [Ubuntu Documentation](https://help.ubuntu.com/) and [Linux Command Library](https://linuxcommandlibrary.com/).

---

This guide covers the most useful commands for everyday Ubuntu administration, scripting, and troubleshooting. For advanced usage, see the official documentation links above.
