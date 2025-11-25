# Define the list of tool URLs

function download_all_dev_tools {
    param (
        [string]$destination
    )
        foreach ($tool in $tools) {
            $filename = ($tool -split "/")[-1]
            $destinationPath = Join-Path -Path $destination -ChildPath $filename
            if (-Not (Test-Path -Path $destinationPath)) {
                try {
                    Invoke-WebRequest -Uri $tool -OutFile $destinationPath
                    Write-Host "Downloaded: $filename" -ForegroundColor Green
                } catch {
                    Write-Host ("Failed to download " + $filename + ": " + $error[0].Exception.Message) -ForegroundColor Red
                }
            } else {
                Write-Host "$filename already exists. Skipping download." -ForegroundColor Yellow
            }
        }
    }

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
    "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/latest/download/Notepad++_Installer.exe",
    # WinMerge (latest)
    "https://winmerge.org/downloads/WinMerge-2.16.0-Setup.exe",
    # MinGW (latest)
    "https://sourceforge.net/projects/mingw-w64/files/latest/download",
    # MySYS (latest)
    "https://www.msys2.org/msys2-x86_64-latest.exe",
    # Cygwin (latest)
    "https://cygwin.com/setup-x86_64.exe",
    # arm64x 86 versions can be added similarly if needed
    "https://cygwin.com/setup-arm64.exe",
    "https://www.msys2.org/msys2-arm64-latest.exe",
    "https://sourceforge.net/projects/mingw-w64/files/latest/download",
    "https://nmap.org/dist/nmap-7.94-setup.exe"  # Nmap (Windows installer)
)
# download_all_dev_tools -destination "$env:USERPROFILE\DevTools"
# Add more URLs as needed
# $downloadDir = "$env:USERPROFILE\DevTools"
# if (-not (Test-Path $downloadDir)) {
#     New-Item -ItemType Directory -Path $downloadDir | Out-Null
# }