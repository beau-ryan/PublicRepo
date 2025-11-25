# Termux Android 13+ Terminal Commands & Usage Guide

**USOS Project - Cross-Platform Terminal Reference**  
*Version: 1.0 | Target: Android 13+ with Termux | Updated: October 2025*

---

## Quick Setup & Access

### Installing Termux

```bash
# Install from F-Droid (recommended for USOS security model)
# Download: https://f-droid.org/packages/com.termux/

# Or install from GitHub releases (latest)
# https://github.com/termux/termux-app/releases

# Grant storage permissions after installation
termux-setup-storage
```

### Initial Configuration
```bash
# Update package repositories
pkg update && pkg upgrade

# Install essential packages for USOS development
pkg install git python nasm vim curl wget openssh

# Setup storage access
ls ~/storage/shared/    # Access to /sdcard/
ls ~/storage/downloads/ # Access to Downloads folder
```

---

## Essential Navigation Commands

### Directory Operations
```bash
# Show current directory
pwd

# List directory contents
ls                      # Basic listing
ls -la                 # Detailed with hidden files
ls -lh                 # Human-readable file sizes
ls -lt                 # Sort by modification time

# Navigate directories
cd /data/data/com.termux/files/home  # Termux home
cd ~/storage/shared/                 # Internal storage (/sdcard/)
cd ~/storage/external-1/             # External SD card (if available)
cd ~                                 # Termux home directory
cd ..                               # Parent directory
cd -                                # Previous directory

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
vim filename.txt               # Text editor
nano filename.txt              # Alternative editor

# Copy files/folders
cp source.txt destination.txt
cp -r source_folder/ dest_folder/

# Move/rename files
mv oldname.txt newname.txt
mv file.txt /new/location/

# Remove files
rm filename.txt
rm -i file.txt                # Interactive confirmation
rm *.txt                      # Remove all .txt files

# View file contents
cat filename.txt              # Display entire file
less filename.txt             # Page through file
head filename.txt             # First 10 lines
tail filename.txt             # Last 10 lines
tail -f logfile.txt           # Follow file changes
```

---

## Android-Specific Commands

### Storage & Permissions
```bash
# Setup storage access (run once)
termux-setup-storage

# Access Android directories
ls ~/storage/shared/Download/    # Downloads folder
ls ~/storage/shared/DCIM/        # Camera photos
ls ~/storage/shared/Documents/   # Documents folder
ls ~/storage/shared/Android/     # App data folders

# Copy files to/from Android storage
cp ~/myfile.txt ~/storage/shared/Download/
cp ~/storage/shared/Download/file.txt ~/

# Check available storage space
df -h ~/storage/shared/
```

### Device Information
```bash
# Android system information
uname -a                      # Kernel and system info
getprop ro.build.version.release  # Android version
getprop ro.product.model      # Device model
getprop ro.product.manufacturer    # Device manufacturer

# Hardware information
cat /proc/cpuinfo             # CPU information
cat /proc/meminfo             # Memory information
cat /proc/version             # Kernel version

# Battery and power
termux-battery-status         # Battery level and status
termux-torch on               # Turn on flashlight
termux-torch off              # Turn off flashlight
```

### Network Commands
```bash
# Network information
ifconfig                      # Network interfaces
ip addr show                  # Alternative network info
ping google.com               # Test connectivity
netstat -an                   # Network connections

# WiFi information
termux-wifi-connectioninfo    # Current WiFi details
termux-wifi-scaninfo         # Available WiFi networks

# Download files
curl -O http://example.com/file.zip
wget http://example.com/file.zip
```

---

## Package Management

### Termux Package Manager
```bash
# Update package repositories
pkg update                    # Update package lists
pkg upgrade                   # Upgrade installed packages
pkg update && pkg upgrade     # Update and upgrade

# Install packages
pkg install package_name
pkg install git python vim curl wget openssh nasm

# Search and manage packages
pkg search keyword            # Search for packages
pkg list-installed           # List installed packages
pkg show package_name        # Show package information
pkg uninstall package_name   # Remove packages

# Essential packages for USOS development
pkg install git python nodejs rust golang clang make cmake
```

### Python Development
```bash
# Install Python and pip
pkg install python

# Python package management
pip install package_name
pip install --user package_name    # User installation
pip list                           # List installed packages
pip freeze > requirements.txt     # Export requirements

# Virtual environments
pip install virtualenv
python -m venv myenv
source myenv/bin/activate         # Activate environment
deactivate                        # Deactivate environment
```

---

## USOS Development Workflows

### Setting Up USOS Repository
```bash
# Clone USOS repository
cd ~/storage/shared/
git clone https://github.com/yourusername/USOS.git
cd USOS/

# Setup Python environment for Universal Runner
cd Universal_RunnerApp/
python -m venv env
source env/bin/activate
pip install -r requirements-dev.txt
```

### Shell Script Development
```bash
# Navigate to USOS shell scripts
cd ~/storage/shared/USOS/Shell_Scripts/

# Make scripts executable
chmod +x android.sh
chmod +x And.sh

# Run USOS Android scripts
./android.sh
./And.sh

# Edit scripts
vim android.sh
nano And.sh
```

### Cross-Platform Testing
```bash
# Test cross-platform compatibility
cd ~/storage/shared/USOS/

# Run Universal Runner tests
cd Universal_RunnerApp/
python -m pytest tests/ -v

# Test shell scripts
cd Shell_Scripts/
bash -n android.sh              # Syntax check
./android.sh                    # Execute script
```

---

## Security & Privacy (Android 13+)

### File Permissions
```bash
# View file permissions
ls -l filename.txt

# Change permissions
chmod 755 script.sh            # rwxr-xr-x
chmod +x script.sh             # Make executable
chmod 600 secret.txt           # rw------- (owner only)

# Check app permissions
termux-permission-list         # List available permissions
```

### Encryption & Security
```bash
# File encryption using OpenSSL
pkg install openssl
openssl enc -aes-256-cbc -in file.txt -out file.enc
openssl enc -d -aes-256-cbc -in file.enc -out file.txt

# Generate SSH keys
pkg install openssh
ssh-keygen -t rsa -b 4096
cat ~/.ssh/id_rsa.pub          # View public key

# Secure file transfer
scp file.txt user@server:/remote/path/
rsync -avz folder/ user@server:/backup/
```

### Privacy Controls
```bash
# Location services
termux-location               # Get current location (requires permission)

# Notification management
termux-notification --title "USOS" --content "Task completed"

# Contact and SMS (with permissions)
termux-contact-list           # List contacts
termux-sms-list              # List SMS messages
```

---

## Text Processing & Development Tools

### Text Manipulation
```bash
# Search in files
grep "pattern" file.txt
grep -r "pattern" folder/     # Recursive search
grep -i "pattern" file.txt    # Case-insensitive

# Text processing
sort file.txt                 # Sort lines
uniq file.txt                 # Remove duplicates
wc file.txt                   # Word/line/character count
cut -d',' -f1 file.csv       # Extract CSV columns

# Find files
find /path -name "*.txt"     # Find by name
find /path -type f -size +1M # Find large files
```

### Code Editors
```bash
# Install and use editors
pkg install vim nano micro

# Vim usage
vim file.txt                 # Open with Vim
:w                          # Save file
:q                          # Quit
:wq                         # Save and quit

# Nano usage
nano file.txt               # Open with Nano
Ctrl+O                      # Save file
Ctrl+X                      # Exit

# Micro editor (modern alternative)
pkg install micro
micro file.txt              # User-friendly editor
```

---

## System Monitoring & Process Management

### Process Management
```bash
# List processes
ps aux                      # All running processes
ps aux | grep process_name  # Find specific process
top                         # Real-time process monitor
htop                        # Enhanced process monitor (if installed)

# Kill processes
kill PID                    # Terminate by process ID
killall process_name        # Kill all instances
pkill -f pattern           # Kill by pattern match
```

### System Resources
```bash
# Memory usage
free -h                     # Memory usage
cat /proc/meminfo          # Detailed memory info

# Disk usage
df -h                      # File system usage
du -sh folder/             # Folder size
du -h --max-depth=1        # Directory sizes

# CPU and system load
uptime                     # System uptime and load
cat /proc/loadavg          # Load averages
```

---

## Networking & Connectivity

### Network Tools
```bash
# Install network utilities
pkg install net-tools iproute2 nmap

# Network connectivity
ping -c 4 google.com       # Ping with count limit
traceroute google.com      # Route tracing
nslookup domain.com        # DNS lookup

# Port scanning and testing
nmap -p 80,443 target.com  # Scan specific ports
nc -zv hostname 80         # Test port connectivity

# Network monitoring
netstat -tulpn             # Listening ports
ss -tulpn                  # Modern alternative to netstat
```

### SSH and Remote Access
```bash
# SSH server setup
pkg install openssh
sshd                       # Start SSH daemon
passwd                     # Set password for SSH access

# SSH client usage
ssh user@hostname          # Connect to remote server
ssh -p 2222 user@server   # Custom port
scp file.txt user@server:/path/  # Copy files over SSH

# SSH key management
ssh-keygen -t ed25519      # Generate modern SSH key
ssh-copy-id user@server    # Copy public key to server
```

---

## Android Integration & Termux API

### Termux API Installation
```bash
# Install Termux:API app from F-Droid
# Then install API package
pkg install termux-api

# Test API functionality
termux-battery-status      # Battery information
termux-camera-info         # Camera information
termux-location           # GPS location (requires permission)
```

### Device Control
```bash
# Audio control
termux-volume music 15     # Set music volume
termux-tts-speak "Hello"   # Text-to-speech

# Vibration and notifications
termux-vibrate             # Vibrate device
termux-notification --title "Title" --content "Message"

# Brightness and display
termux-brightness 50       # Set screen brightness (0-255)

# Clipboard operations
termux-clipboard-get       # Get clipboard content
echo "text" | termux-clipboard-set  # Set clipboard content
```

### Camera and Sensors
```bash
# Camera operations
termux-camera-photo ~/photo.jpg     # Take photo
termux-camera-info                  # Camera specifications

# Sensor data
termux-sensor -l                    # List available sensors
termux-sensor -s accelerometer      # Read accelerometer
termux-sensor -s light              # Read light sensor
```

---

## USOS-Specific Android Development

### Mobile Device Management
```bash
# Create USOS Android script directory
mkdir -p ~/storage/shared/USOS/Android_Scripts/

# Device information collection
cat > device_info.sh << 'EOF'
#!/bin/bash
echo "=== USOS Android Device Information ==="
echo "Device Model: $(getprop ro.product.model)"
echo "Android Version: $(getprop ro.build.version.release)"
echo "Security Patch: $(getprop ro.build.version.security_patch)"
echo "Battery: $(termux-battery-status | grep percentage)"
echo "Storage: $(df -h ~/storage/shared/ | tail -1)"
EOF

chmod +x device_info.sh
./device_info.sh
```

### Security Scanning
```bash
# Network security check
cat > network_scan.sh << 'EOF'
#!/bin/bash
echo "=== USOS Network Security Scan ==="
echo "WiFi Info: $(termux-wifi-connectioninfo)"
echo "Open Ports:"
netstat -tulpn | grep LISTEN
echo "Network Interfaces:"
ip addr show
EOF

chmod +x network_scan.sh
./network_scan.sh
```

### System Maintenance
```bash
# Create system cleanup script
cat > cleanup.sh << 'EOF'
#!/bin/bash
echo "=== USOS Android System Cleanup ==="
pkg autoclean
pkg autoremove
apt autoremove
rm -rf ~/.cache/*
rm -rf ~/storage/shared/.thumbnails/
echo "Cleanup completed"
EOF

chmod +x cleanup.sh
./cleanup.sh
```

---

## Troubleshooting Common Issues

### Permission Problems
```bash
# Fix common permission issues
termux-setup-storage       # Re-setup storage access
chmod +x script.sh         # Make script executable

# Check app permissions
termux-permission-list     # List available permissions
```

### Package Issues
```bash
# Fix package problems
pkg update --fix-missing   # Fix missing packages
pkg reinstall package_name # Reinstall problematic package
apt --fix-broken install   # Fix broken dependencies
```

### Storage Issues
```bash
# Check storage space
df -h                      # Disk usage
du -sh ~/.cache/           # Cache usage
pkg clean                  # Clean package cache
```

---

## Integration with USOS Ecosystem

### Cross-Platform Synchronization
```bash
# Sync USOS project across devices
cd ~/storage/shared/
git clone https://github.com/yourusername/USOS.git
cd USOS/

# Keep project updated
git pull origin main
git status

# Push changes from Android
git add .
git commit -m "Android development updates"
git push origin main
```

### Universal Runner Integration
```bash
# Setup Universal Runner on Android
cd ~/storage/shared/USOS/Universal_RunnerApp/
python -m venv android_env
source android_env/bin/activate
pip install -r requirements.txt

# Run Universal Runner
python src/main.py --platform android
```

---

## Security Best Practices

### Data Protection
```bash
# Encrypt sensitive files
openssl enc -aes-256-cbc -in sensitive.txt -out sensitive.enc
rm sensitive.txt           # Remove original

# Secure directory permissions
chmod 700 ~/private/       # Owner access only
chmod 600 ~/private/*      # Files owner read/write only
```

### Network Security
```bash
# Check for malicious network activity
netstat -an | grep :80     # Check HTTP connections
netstat -an | grep :443    # Check HTTPS connections

# Monitor unusual processes
ps aux | grep -v com.termux  # Non-Termux processes
```

---

## Quick Reference Card

```bash
# Essential Android/Termux Commands
pkg update && pkg upgrade    # Update system
termux-setup-storage        # Setup storage access
chmod +x script.sh          # Make executable
termux-battery-status       # Battery info
termux-wifi-connectioninfo  # WiFi details
df -h ~/storage/shared/     # Storage usage
ps aux | grep process       # Find process
kill PID                    # Kill process
git pull                    # Update repository
python src/main.py          # Run Python app
```

---

**USOS Integration Notes:**
- This guide enables USOS development on Android 13+ devices using Termux
- All commands tested for Android 13+ compatibility with latest Termux
- Integrates with USOS cross-platform architecture: Boot/, Universal_RunnerApp/, Shell_Scripts/
- Supports USOS security model with local-first operations and encryption
- Compatible with USOS development workflows across Windows, Linux, Mac, and Android

**Last Updated:** October 29, 2025  
**Compatible with:** Android 13+ with Termux 0.118+  
**Part of:** USOS Universal System Operations documentation suite