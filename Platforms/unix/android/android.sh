
#!/data/data/com.termux/files/usr/bin/bash
# Android Custom Script
# Description: Interactive Termux utility for Android 13+ devices.
# Author: [jamie]
# Usage: Run this script in Termux to access device info, update packages, connect via SSH, and view IP address.

title="======My Android Script====="
author="beau-ryan on git"

show_banner() {
	RED='\033[0;31m'
	GREEN='\033[0;32m'
	BOLD='\033[1m'
	RESET='\033[0m'
    echo -e "${BOLD}${RED}$title${RESET}"
	echo -e "$author"
	echo -e  "${BOLD}${GREEN} ==You suck at progamming==${RESET} " 
    echo -e "    All Android 13++  "
    echo -e "   My Custom script   "
    echo -e "${BOLD}${RED}========≠≠≠≠≠=========${RESET}"
}
set -e 
show_banner
	
show_menu() {
    echo "1. Show Device info"
    echo "2. update termux packages"
    echo "3. ssh remote connection"
    echo "4. show IP "
    echo "5. List All Packages"
	echo "6. adroid-tools install"
	echo "7. Scanning w/nmap "
	echo "8. Active Network "
	echo "9. Battery Status"
	echo "10. WI-FI Check"
	echo "11. Check Ram "
	echo "12. Check PID/running processes "
    echo "13. location info"  
    echo "0. exit"
}

while true; do
    show_menu
    read -p "Enter your choice (0-13): " choice
    case $choice in
        1)
            echo "Device Information:"
            uname -a
            ;;
        2)
            echo "Updating Termux packages..."
            pkg update 
            pkg upgrade 
			pkg install openssh
            ;;
        3)
            read -p "Enter remote user@host: " remote
            ssh "$remote"
            echo "SSH connection closed."
            ;;
        4)
            echo "Your IP Address is:"
            ip addr show
            ;;

        5)	echo "List of Packages..."
			apt list --installed
			pkg list-installed
                        ;;
		6) 	echo "Installing ADB"
			pkg install android-tools
			echo "done"
			;;
		7)	# Advanced option 1.
			echo "scanning open ports"
			if command -v nmap >/dev/null 2>&1; then
				read -p "Enter IP or port no to scan (default: localhost): " target
				target=${target:-192.168.1.8/24}
				nmap -Pn -p- "$target"
			else
				nmap -v 192.168.1.8/24
				echo "nmap not found install try again"
				netstat -tuln
			fi
			;;
		8)
			echo "Active Networks are...."
			netstat -anp
			;;
		9)
			echo "Battery status"
			termux-battery-status
			;;
		10)
			echo "WI-FI Network"
			termux-wifi-scaninfo
			;;
		11)
			echo "Checking Ram"
			free -h
			;;
		12)
			echo "checking running processes"
			ps aux
			;;
        13)
            echo "termux-location"
            termux-sensor -L
            ;; 

        0)
            echo "Exiting...happy hacking"
            exit
            ;;
        *)
            echo "Invalid choice. Please try again."
			break
            ;;
    esac
done
echo "Thanks for trying me out happy hacking "