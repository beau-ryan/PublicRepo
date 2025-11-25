
# Platforms/windows/win.ps1
# This script creates necessary folders and downloads development tools for Windows
. "$PSScriptRoot\env.ps1"
function create__all_folder_if_not_exists {
    param (
        [string]$path
    )
    if (-Not (Test-Path -Path $path)) {
        New-Item -ItemType Directory -Path $path | Out-Null
    }
}
function download_all_dev_tools {
    param (
        [string]$destination
    )

    $tools = @(
        # Node.js (latest LTS)
        "https://nodejs.org/dist/v20.11.1/node-v20.11.1-x64.msi",
        # Go (latest stable)
        "https://go.dev/dl/go1.22.2.windows-amd64.msi",
        # Java JDK 21 (latest LTS)
        "https://download.oracle.com/java/21/latest/jdk-21_windows-x64_bin.exe",
        # Maven (latest)
        "https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.zip",
        # Ant (latest)
        "https://dlcdn.apache.org/ant/binaries/apache-ant-1.10.14-bin.zip",
        # Gradle (latest)
        "https://services.gradle.org/distributions/gradle-8.8-bin.zip",
        # Python (latest stable)
        "https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe",
        # Rust (latest installer)
        "https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe",
        # Kali Linux (latest installer)
        "https://cdimage.kali.org/kali-2024.3/kali-linux-2024.3-installer-amd64.exe",
        # WSL (Microsoft Store)
        "https://aka.ms/wslstore",
        # Sysinternals Suite (latest)
        "https://download.sysinternals.com/files/SysinternalsSuite.zip",
        # Firefox (latest)
        "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US",
        # VS Code (latest stable)
        "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user",
        # Git for Windows (latest)
        "https://github.com/git-for-windows/git/releases/latest/download/Git-64-bit.exe",
        # 7-Zip (latest)
        "https://www.7-zip.org/a/7z2401-x64.exe",
        # Sublime Text (latest)
        "https://www.sublimetext.com/download_thanks?platform=win64",
        # Postman (latest agent)
        "https://dl.pstmn.io/download/latest/win64",
        # Docker Desktop (latest)
        "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe",
        # JetBrains Toolbox (latest)
        "https://download.jetbrains.com/toolbox/jetbrains-toolbox-2.3.1.31116.exe",
        # Vagrant (latest)
        "https://releases.hashicorp.com/vagrant/2.4.2/vagrant_2.4.2_windows_amd64.msi",
        # Terraform (latest)
        "https://releases.hashicorp.com/terraform/1.9.0/terraform_1.9.0_windows_amd64.zip",
        # VirtualBox (latest)
        "https://download.virtualbox.org/virtualbox/7.0.20/VirtualBox-7.0.20-162994-Win.exe",
        # Notepad++ (latest)
        "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/latest/download/npp.x64.installer.exe",
        # WinMerge (latest)
        "https://github.com/WinMerge/winmerge/releases/latest/download/WinMerge-2.16.36-x64-Setup.exe",
        # PuTTY (latest)
        "https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe",
        # Fiddler Everywhere (latest)
        "https://download.telerik.com/fiddler/fiddler-everywhere-3.3.2.exe",
        # GIMP (latest)
        "https://download.gimp.org/mirror/pub/gimp/v2.10/windows/gimp-2.10.36-setup.exe",
        # WinSCP (latest)
        "https://winscp.net/download/WinSCP-6.3.2-Setup.exe",
        # SQLite (latest)
        "https://www.sqlite.org/2024/sqlite-tools-win32-x86-3440000.zip",
        # cmder (latest)
        "https://github.com/cmderdev/cmder/releases/latest/download/cmder.zip",
        # Yarn (latest)
        "https://classic.yarnpkg.com/latest.msi",
        # MongoDB Compass (latest)
        "https://downloads.mongodb.com/compass/mongodb-compass-1.39.4-win32-x64.exe",
        # PostgreSQL (latest)
        "https://get.enterprisedb.com/postgresql/postgresql-16.3-1-windows-x64.exe",
        # MySQL Installer (latest)
        "https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.4.0.0.msi",
        # QEMU (latest Windows release)
        "https://github.com/qemu/qemu/releases/latest/download/qemu-w64-setup.exe",
        # VMware Workstation Player (latest)
        "https://www.vmware.com/go/getplayer-win",
        # DOSBox (latest)
        "https://downloads.sourceforge.net/project/dosbox/dosbox/0.74-3/DOSBox0.74-3-win32-installer.exe",
        # PCem (latest)
        "https://github.com/pcem-emulator/pcem/releases/latest/download/pcem.zip",
        # Virt-Manager (Windows port, if available)
        "https://github.com/virt-manager/virt-manager/releases/latest/download/virt-manager-setup.exe",
        # MobaXterm (latest)
        "https://mobaxterm.mobatek.net/download-home-edition.html"
    )

    foreach ($tool in $tools) {
        $fileName = Split-Path -Path $tool -Leaf
        $destinationPath = Join-Path -Path $destination -ChildPath $fileName
        if (-Not (Test-Path -Path $destinationPath)) {
            Write-Host "Downloading $fileName to $destinationPath"
            Invoke-WebRequest -Uri $tool -OutFile $destinationPath
        } else {
            Write-Host "$fileName already exists at $destinationPath"
        }
    }
}
# Main script execution
$env = "I:\PublicRepo\MySyS"
create__all_folder_if_not_exists -path $env
$toolsPath = Join-Path -Path $env -ChildPath "DevTools"
create__all_folder_if_not_exists -path $toolsPath
download_all_dev_tools -destination $toolsPath
# Note: After downloading, you may need to manually run the installers or script their installation as
# some installers may require user interaction.
# Also, ensure that the paths in env.ps1 are correctly set to where the tools are installed.
# Finally, consider adding error handling and logging for production scripts.
