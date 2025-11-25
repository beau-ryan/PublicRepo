# Mac OS Lion Terminal Commands & Usage Guide

**USOS Project - Cross-Platform Terminal Reference**  
*Version: 1.0 | Target: Mac OS Lion (10.7) | Updated: October 2025*

---

## Quick Access Commands

### Opening Terminal

```bash
# Method 1: Spotlight Search
⌘ + Space → type "Terminal" → Enter

# Method 2: Applications
Applications → Utilities → Terminal

# Method 3: Launchpad
F4 (Mission Control) → Launchpad → Terminal
```

---

## Essential Navigation Commands

### Directory Operations

```bash
# Show current directory
pwd

# List directory contents
ls                    # Basic listing
ls -la               # Detailed with hidden files
ls -lh               # Human-readable file sizes
ls -lt               # Sort by modification time

# Change directories
cd /path/to/directory
cd ~                 # Home directory
cd ..                # Parent directory
cd -                 # Previous directory

# Create directories
mkdir new_folder
mkdir -p path/to/nested/folders

# Remove directories
rmdir empty_folder
rm -rf folder_with_contents    # CAUTION: Irreversible
```

### File Operations

```bash
# Create files
touch filename.txt
echo "content" > file.txt
nano filename.txt            # Text editor

# Copy files/folders
cp source.txt destination.txt
cp -r source_folder/ dest_folder/

# Move/rename files
mv oldname.txt newname.txt
mv file.txt /new/location/

# Remove files
rm filename.txt
rm -i file.txt              # Interactive confirmation
rm *.txt                    # Remove all .txt files

# View file contents
cat filename.txt            # Display entire file
less filename.txt           # Page through file
head filename.txt           # First 10 lines
tail filename.txt           # Last 10 lines
tail -f logfile.txt         # Follow file changes
```

---

## System Information & Monitoring

### System Details
```bash
# System information
uname -a                    # Complete system info
sw_vers                     # Mac OS version details
system_profiler SPSoftwareDataType

# Hardware information
system_profiler SPHardwareDataType
sysctl hw.memsize           # Memory size
df -h                       # Disk usage
du -sh folder/              # Folder size
```

### Process Management
```bash
# List processes
ps aux                      # All running processes
ps aux | grep process_name  # Find specific process
top                         # Real-time process monitor
Activity\ Monitor &         # GUI process monitor

# Kill processes
kill PID                    # Terminate by process ID
killall process_name        # Kill all instances
sudo kill -9 PID           # Force kill
```

### Network Commands
```bash
# Network information
ifconfig                    # Network interfaces
ping google.com             # Test connectivity
netstat -an                 # Network connections
nslookup domain.com         # DNS lookup
traceroute google.com       # Route tracing

# Download files
curl -O http://example.com/file.zip
wget http://example.com/file.zip  # Requires installation
```

---

## Package Management & Development

### Homebrew (Package Manager)
```bash
# Install Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Basic Homebrew commands
brew install package_name
brew uninstall package_name
brew update                 # Update Homebrew
brew upgrade               # Upgrade all packages
brew list                  # List installed packages
brew search package_name   # Search for packages
```

### Development Tools for USOS
```bash
# Install cross-compilation tools
brew install nasm          # Assembler for x86 OS
brew install i386-elf-gcc  # Cross-compiler
brew install qemu          # Emulator for testing
brew install git           # Version control

# Python development
brew install python3
pip3 install virtualenv
virtualenv venv
source venv/bin/activate

# Text editors
brew install nano
brew install vim
```

---

## File Permissions & Security

### Permission Management
```bash
# View permissions
ls -l filename.txt

# Change permissions
chmod 755 script.sh        # rwxr-xr-x
chmod +x script.sh         # Make executable
chmod 644 file.txt         # rw-r--r--

# Change ownership
sudo chown user:group file.txt
sudo chown -R user folder/

# Permission codes
# 4 = read (r)
# 2 = write (w)  
# 1 = execute (x)
# 755 = rwxr-xr-x (owner: rwx, group: r-x, others: r-x)
```

### Security Commands
```bash
# Sudo operations
sudo command               # Run as administrator
sudo -u username command   # Run as specific user
sudo su                   # Switch to root user

# File encryption (if available)
openssl enc -aes-256-cbc -in file.txt -out file.enc
openssl enc -d -aes-256-cbc -in file.enc -out file.txt
```

---

## Text Processing & Search

### Text Manipulation
```bash
# Search in files
grep "pattern" file.txt
grep -r "pattern" folder/   # Recursive search
grep -i "pattern" file.txt  # Case-insensitive

# Text processing
sort file.txt              # Sort lines
uniq file.txt              # Remove duplicates
wc file.txt                # Word/line/character count
cut -d',' -f1 file.csv     # Extract CSV columns

# Find files
find /path -name "*.txt"   # Find by name
find /path -type f -size +1M  # Find large files
locate filename            # Quick file search
```

### Text Editors
```bash
# Command-line editors
nano file.txt              # Simple editor
vim file.txt               # Advanced editor
emacs file.txt             # Emacs editor

# GUI editors
open -a TextEdit file.txt  # TextEdit
open -a "Sublime Text" file.txt  # Sublime Text
```

---

## Environment & Variables

### Environment Variables
```bash
# View environment variables
env                        # All variables
echo $PATH                 # PATH variable
echo $HOME                 # Home directory

# Set variables
export VARIABLE_NAME="value"
export PATH="$PATH:/new/path"

# Persistent variables (add to ~/.bash_profile)
echo 'export PATH="$PATH:/usr/local/bin"' >> ~/.bash_profile
source ~/.bash_profile     # Reload profile
```

### Shell Configuration
```bash
# Profile files
~/.bash_profile           # Bash login shell
~/.bashrc                 # Bash interactive shell
~/.profile                # General profile

# View shell
echo $SHELL
which bash
```

---

## Archive & Compression

### Working with Archives
```bash
# Create archives
tar -czf archive.tar.gz folder/
zip -r archive.zip folder/

# Extract archives
tar -xzf archive.tar.gz
unzip archive.zip

# View archive contents
tar -tzf archive.tar.gz
unzip -l archive.zip
```

---

## USOS Development Specific

### x86 OS Development
```bash
# Navigate to USOS project
cd /path/to/USOS/Boot/bootloader/

# Build x86 OS (requires cross-compilation tools)
make                       # Build bootloader and kernel
make run                   # Test in QEMU
make clean                 # Clean build artifacts

# Debug with QEMU and GDB
make debug                 # Start debugging session
```

### Python Development
```bash
# Universal Runner App setup
cd /path/to/USOS/Universal_RunnerApp/
python3 -m venv env
source env/bin/activate
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/ -v
```

### Cross-Platform Scripts
```bash
# Make shell scripts executable
chmod +x Shell_Scripts/*.sh

# Run USOS shell scripts
./Shell_Scripts/linux.sh
./Shell_Scripts/android.sh
```

---

## Keyboard Shortcuts

### Terminal Shortcuts
```bash
⌘ + T                     # New tab
⌘ + N                     # New window
⌘ + W                     # Close tab
⌘ + Shift + }             # Next tab
⌘ + Shift + {             # Previous tab
⌘ + K                     # Clear screen
⌘ + Plus/Minus            # Zoom in/out
```

### Command Line Shortcuts
```bash
Ctrl + C                  # Interrupt command
Ctrl + D                  # End of input/logout
Ctrl + Z                  # Suspend process
Ctrl + A                  # Beginning of line
Ctrl + E                  # End of line
Ctrl + U                  # Clear line
Ctrl + R                  # Search command history
Tab                       # Auto-complete
!!                        # Repeat last command
```

---

## System Maintenance

### Disk Management
```bash
# Check disk usage
df -h                     # File system usage
du -sh /*                 # Directory sizes
diskutil list             # List all disks

# Disk repair (from Recovery Mode)
diskutil verifyVolume /
diskutil repairVolume /
```

### System Cleanup
```bash
# Clear caches (be careful)
sudo dscacheutil -flushcache
sudo purge               # Clear inactive memory

# Log files
sudo rm -rf /var/log/*.log
ls -la /var/log/         # View log files
```

---

## Remote Access & Networking

### SSH Operations
```bash
# Connect to remote server
ssh username@hostname # Example ssh jack@10.10.0.0
ssh -p 2222 user@server   # Custom port, ssh -p 2222 john@10.10.0.1

# Copy files over SSH
scp file.txt user@server:/remote/path/
scp -r folder/ user@server:/remote/path/

# SSH key management
ssh-keygen -t rsa -b 4096
ssh-copy-id user@server
```

### Network Utilities
```bash
# Test network connectivity
ping -c 4 google.com      # 4 pings only
nc -zv hostname 80        # Test port connectivity
nmap hostname             # Port scanning (if installed)
```

---

## Troubleshooting Common Issues

### Permission Problems
```bash
# Fix common permission issues
sudo chown -R $(whoami) /usr/local
chmod +x script.sh
sudo chmod 755 /usr/local/bin/command
```

### Path Issues
```bash
# Check and fix PATH
echo $PATH
export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"
which command_name
```

### Application Problems
```bash
# Force quit applications
pkill application_name
sudo pkill -f "application"
killall -9 application_name
```

---

## Safety Guidelines

### Important Warnings
- **Always backup before using `rm -rf`** - this permanently deletes files
- **Use `sudo` carefully** - you can damage system files
- **Test commands in safe directories first**
- **Keep important files backed up**

### Best Practices
- Use `ls` before `rm` to verify targets
- Use `-i` flag for interactive confirmations
- Test scripts in isolated environments
- Keep system updated: Software Update in System Preferences

---

## Quick Reference Card

```bash
# Most Used Commands
pwd                       # Where am I?
ls -la                    # What's here?
cd folder                 # Go somewhere
cp file1 file2           # Copy file
mv file1 file2           # Move/rename
rm file                   # Delete file
mkdir folder             # Create folder
chmod +x script          # Make executable
nano file                # Edit file
grep "text" file         # Search in file
ps aux                   # List processes
top                      # System monitor
```

---

**USOS Integration Notes:**
- This guide supports USOS cross-platform development on Mac OS Lion
- All commands tested for compatibility with Lion's default terminal
- Use with USOS project structure: Boot/, Universal_RunnerApp/, PS1/, Shell_Scripts/
- For USOS development, install Homebrew and cross-compilation tools first

**Last Updated:** October 29, 2025  
**Compatible with:** Mac OS Lion 10.7.x  
**Part of:** USOS Universal System Operations documentation suite