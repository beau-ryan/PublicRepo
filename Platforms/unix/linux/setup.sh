#/usr/bin/env bash
# Learning as i go to refine my linux setup script
# Solo DevOps project/script to help automate linux environment setup

# This script sets up a basic Linux environment with essential tools and configurations.
# So When I move over to Kali-linux or ubuntu, I can understand how to use all linux commands
#
# menu for linux specialized commands
# How to profit from this script
# like seriously. How?????????????. first step is to change the title
# This script sets up a basic Linux environment with essential tools and configurations.
# Command Menu for Kali Linux
# running all commands from a menu
# by: Shadow User
# version 0.0.1

title="======== Linux Environment Setup ========="
author="beau-ryan"



banner() {
    RED='\033[0;31m'
    NC='\033[0m' # No Color
    RESET='\033[0m'
    BOLD='\033[1m'
    YELLOW='\033[1;33m'
    GREEN='\033[0;32m'
    echo -e "${RED}${BOLD}${title}${RESET}"
    echo -e "${RED}${BOLD}${author}${RESET}"
	echo -e "${RED}${BOLD}===============================================${RESET}"
    echo -e "${YELLOW}${BOLD}     My Custom Linux Admin Toolkit         ${RESET}"
    echo -e "${RED}${BOLD}===============================================${RESET}"
    echo -e "${YELLOW}${BOLD}             Version: 0.0.1 ${RESET}"
    echo -e "${RED}${BOLD}===============================================${RESET}"
}
set -e

banner

# Function to check and display version if command exists
check_version() {
    if command -v "$1" &> /dev/null; then
        echo "$1 version:"
        "$1" --version 2>/dev/null || echo "  $1 is installed but version info unavailable"
    else
        echo "$1 is not installed"
    fi
}

# menu options so the user can choose to install 

menu() {
    echo -e "${YELLOW}${BOLD}Select an option:${RESET}"
    echo -e "${GREEN} 1) Update and install essential packages${RESET}"
    echo -e "${GREEN} 2) Check versions ${RESET}"
    echo -e "${GREEN} 0) Exit${RESET}"
}

while true; do
    menu 
    read -rp "Enter your choice (0-2, q to quit): " choice
    case $choice in
        # This option is to help update and updgrade 
        # the system and install essential packages - make sure to test or can use to improve manual command knowledge
        1) 
            echo -e "${YELLOW}${BOLD}Updating package lists and installing essential packages...${RESET}"
            sudo apt update && sudo apt upgrade -y
            # sudo apt install -y git curl vim htop build-essential # uncomment if needed 
            # sudo apt install -y build-essential curl file git lsb-release net-tools ufw nmap stunnel4  # uncomment if needed 
            sudo apt autoremove -y # uncomment if needed to clean up packages 
            echo -e "${YELLOW}${BOLD}Installation complete!${RESET}"
            ;;
        2) 
            echo "Checking Versions"
            check_version curl
            check_version git
            check_version nmap
            check_version stunnel4
            check_version gcc
            check_version c++
            check_version python3
            check_version qemu-system-x86_64
            echo -e  "${RED} all versions checked finished: results displayed ${RESET} "
            ;;
        0)
            echo "Exiting..."
            exit 0
            ;;
        q)
            echo -e "${YELLOW}${BOLD}Exiting setup.${RESET}"
            break
            ;;
        *)
            echo -e "${YELLOW}${BOLD}Invalid option. Please try again.${RESET}"
            ;;
    esac
done
echo -e "${YELLOW}${BOLD}Setup script finished.${RESET}"