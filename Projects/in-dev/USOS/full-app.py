
# The USOS FULL App main for beta users
"""Please refer to documetation Guides to
    help understand the scacle and 
    functionality of this app.
    SOLO-DEV-2025
___  ___  ________  ________  ________      
|\  \|\  \|\   ____\|\   __  \|\   ____\     
\ \  \\\  \ \  \___|\ \  \|\  \ \  \___|_    
 \ \  \\\  \ \_____  \ \  \\\  \ \_____  \   
  \ \  \\\  \|____|\  \ \  \\\  \|____|\  \  
   \ \_______\____\_\  \ \_______\____\_\  \
    \|_______|\_________\|_______|\_________\
"""

# from Beta_Users import users
import os
import sys

def open_powerShell():
    """Open a new PowerShell window and run USOS.ps1 script."""
    if sys.platform == "win32":
        # Get the absolute path to the USOS.ps1 script

        # Adjust the path as necessary 
        # script_path = os.path.join(os.getcwd(), "Platforms", "USOS.ps1")
        script_path = os.path.join("F:\\", "My local Repo", "PublicRepo", "Projects", "in-dev", "USOS", "Platforms", "USOS.ps1")
        
        # Option 1: Run in new PowerShell window
        command = f'start powershell -Command "& \'{script_path}\'; Read-Host \'Press Enter to exit\'"'
        
        # Option 2: Run in current process (uncomment to use instead)
        # command = f'powershell -ExecutionPolicy Bypass -File "{script_path}"'
        
        print(f"Executing: {script_path}")
        os.system(command)
    else:
        print("PowerShell can only be opened on Windows systems.")
        sys.exit(1)

if __name__ == "__main__":
    # comment open_powershell to run other functions
    # for feedback, View User Info, View My Modules & Featured Modules
    #users.menu()

    open_powerShell()

