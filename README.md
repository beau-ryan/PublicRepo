# USOS: Universal System Operations Technology Independence & User Sovereignty

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Language](https://img.shields.io/badge/Languages-Python%20|%20PowerShell%20|%20Bash-orange)

> **Empowering users with accessible, cross-platform tools for device management, security, and digital independence.**

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/beau-ryan/PublicRepo.git
cd PublicRepo

# Quick setup (Windows)
.\Platforms\windows\powershell\menu.ps1

# Quick setup (Linux/macOS)
./Platforms/unix/linux/setup.sh
```

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Supported Platforms](#-supported-platforms)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**USOS (Universal System Operations)** is a comprehensive cross-platform toolkit born from a simple frustration: being tired of subscription fees and not truly owning your software. What started as a personal Python learning journey in July 2024 to build my own apps has evolved into a complete platform for digital independence.

### 🎪 The Problem We Solve

- **Subscription Fatigue**: Tired of monthly fees for basic tools and never truly owning what you pay for
- **Digital Dependency**: Over-reliance on Big Tech platforms and cloud services you can't control
- **Learning Barriers**: Want to code your own solutions but don't know where to start
- **Platform Lock-in**: Different expensive tools needed for different operating systems
- **Privacy Invasion**: Your data scattered across services you don't control

### ✨ Our Solution

**From frustration to freedom** - USOS provides tools that let you:

- **Own your software**: No subscriptions, no dependencies, complete control
- **Learn by building**: Started as Python education, now teaches all aspects of computing
- **Work offline**: Everything runs locally without cloud dependencies  
- **Cross-platform freedom**: One toolkit for Windows, Linux, macOS, and Android
- **Transparent operation**: See exactly what your tools are doing with full logging

---

## 🔥 Features

### 🛡️ Security & Privacy First

- **Local Antivirus Scanning**: No cloud dependencies
- **Device Security Audits**: Comprehensive system analysis
- **Privacy Protection**: All data stays on your device
- **Transparent Logging**: See exactly what the tools are doing

### 🌐 Cross-Platform Compatibility

- **Windows**: PowerShell-based tools and GUI applications
- **Linux**: Bash scripts and native utilities
- **macOS**: Universal compatibility layer
- **Android**: Mobile device management tools

### 📚 Educational Focus

- **Beginner-Friendly**: Menu-driven interfaces with clear instructions
- **Learning Resources**: Built-in tutorials and explanations
- **Skill Building**: Progress from basic to advanced operations
- **Documentation**: Comprehensive guides for all levels

### ⚙️ Universal Runner Engine

- **Modular Architecture**: Plugin-based extensibility
- **Multi-Language Support**: Python, Java, C#, Assembly, Bash, PowerShell
- **Automation Workflows**: Reduce setup time from 30+ minutes to under 5
- **Web Interface**: Browser-based desktop environment

---

## 💻 Supported Platforms

| Platform | Status | Features |
|----------|--------|----------|
| ![Windows](https://img.shields.io/badge/Windows-10%2F11-blue) | ✅ Full Support | PowerShell automation, GUI tools, system management |
| ![Linux](https://img.shields.io/badge/Linux-Ubuntu%2FKali%2FFedora-orange) | ✅ Full Support | Bash scripts, package management, security tools |
| ![macOS](https://img.shields.io/badge/macOS-Universal-lightgrey) | 🔄 In Progress | Cross-compatibility layer, native tools |
| ![Android](https://img.shields.io/badge/Android-7+-green) | 🔄 Beta | Mobile device management, security scanning |

---

## 📦 Installation

### Prerequisites

#### Windows

- PowerShell 5.1+ or PowerShell Core 7+
- Windows 10/11 recommended
- Administrator privileges for security tools

#### Linux

- Bash 4.0+
- Python 3.8+ (for Universal Runner and USOS apps)
- Standard Unix utilities (grep, find, awk, sed)

#### macOS

- Zsh or Bash
- Python 3.8+
- Xcode Command Line Tools

#### Android

- Android 7.0+ (API level 24+)
- Termux or compatible terminal emulator
- Storage permissions for security scanning

### Quick Install

#### Windows PowerShell Setup

```powershell
# Run as Administrator (if needed for execution policy)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Navigate to platform scripts
cd Platforms\windows\powershell

# Launch main menu
.\menu.ps1

# Or run specific tools:
.\security-scan.ps1        # Security scanning
.\demo-menu.ps1            # Demo features
```

#### Linux/macOS

```bash
# Navigate to platform scripts
cd Platforms/unix/linux

# Make scripts executable
chmod +x *.sh

# Run setup
./setup.sh

# Launch security menu
./security-menu.sh

# Or run system audit
./system-audit.sh
```

#### Universal Runner Installation

```bash
# Navigate to Universal Runner
cd Projects/in-dev/USOS/Universal_RunnerApp/src/content/applications/code_review/universal_runner

# Install Python dependencies
pip install -r requirements.txt

# Run setup
python setup.py install

# Launch Universal Runner
python main.py
```

#### USOS Full Application

```bash
# Navigate to USOS project
cd Projects/in-dev/USOS

# Run the full application
python full-app.py
```

#### Android (SpiritApp)

```bash
# Navigate to spiritapp
cd Projects/in-dev/USOS/Universal_RunnerApp/src/content/applications/spiritapp

# Build with Gradle
./gradlew build

# Or open in Android Studio
```

---

## 🎮 Usage

### Getting Started

1. **Security First**: Run the antivirus and system scan tools

2. **Explore Gradually**: Use menu-driven interfaces to learn your system
3. **Check Logs**: Review detailed feedback and troubleshooting info
4. **Build Skills**: Progress through educational modules
5. **Share Knowledge**: Help others by sharing guides and scripts

### Example Workflows

#### Windows System Health Check

```powershell
# Launch main menu
.\Platforms\windows\powershell\menu.ps1

# Run security scan
.\Platforms\windows\powershell\security-scan.ps1

# Demo menu for testing
.\Platforms\windows\powershell\demo-menu.ps1

# Open Linux/Ubuntu subsystem demo
.\Platforms\windows\powershell\demo-open-linux-ubuntu.ps1
```

#### Linux Security Audit

```bash
# Launch interactive security menu
./Platforms/unix/linux/security-menu.sh

# Run comprehensive system audit
./Platforms/unix/linux/system-audit.sh

# Run setup/installation
./Platforms/unix/linux/setup.sh
```

---

## 📁 Project Structure

```plaintext
PublicRepo/
│   .gitattributes
│   .gitignore
│   CODE_OF_CONDUCT.md
│   CONTRIBUTING.md
│   LICENSE
│   PublicRepo.sln
│   README.md                       # You are here
│   tree.txt
│   
├───Platforms/                      # Platform-specific implementations
│   ├───unix/
│   │   │   Ubuntu_linux_Cmd.md
│   │   │   
│   │   └───linux/
│   │           security-menu.sh
│   │           setup.sh
│   │           system-audit.sh
│   │           
│   └───windows/
│       │   Essential_Windows_CMD&PowerShell_Commands.md
│       │   
│       └───powershell/
│               demo-menu.ps1
│               demo-open-linux-ubuntu.ps1
│               menu.ps1
│               security-scan.ps1
│               
├───Project-Docs/                   # Project documentation
│   │   Dev_Guide.md
│   │   Full-project.md
│   │   Project_Management.md
│   │   USOS-Project.md
│   │   
│   └───Docs/
│           AI Orchestration Worker.doc
│           CONTRIBUTION_README.md
│           FULL_PROJECT_README.doc
│           innovation_README.md
│           Internal Pitch Deck for Stakeholders_Investors.md
│           Kubernetes Deployment Example.doc
│           Meta-Operating System vs. Full.md
│           MobileOS_Comprehensive_Report.md
│           MobileOS_Technical_Report.md
│           NO-Trust-Policy.md
│           Security Policy.md
│           Universal Runner Contributing Guidelines.md
│           Universal Runner External Pitch & Fundraising Overview.md
│           USOS_Comprehensive_Report.md
│           USOS_Technical_Report.md
│           
└───Projects/                       # Active and future projects
    ├───ideas/
    │       FutureProjectsdoc.md
    │       
    └───in-dev/
        │   USOS.md
        │   
        └───USOS/                   # Main USOS project
            │   .gitattributes
            │   .gitignore
            │   full-app.py
            │   README.md
            │   USOS.pyproj
            │   USOS.sln
            │   USOS.slnLaunch.user
            │   USOS_README.md
            │   __init__.py
            │   
            ├───PlatForms/          # USOS platform implementations
            │   │   README.md
            │   │   USOS.hta
            │   │   USOS.ps1
            │   │   
            │   ├───Android/
            │   │       android.sh
            │   │       
            │   ├───unix/
            │   │   │   ssh.sh
            │   │   │   
            │   │   ├───android/
            │   │   │       Termux.md
            │   │   │       
            │   │   ├───linux/
            │   │   │       Ubuntu_linux_Cmd.md
            │   │   │       
            │   │   └───macOs/
            │   │           MAC_OS_lion.md
            │   │           
            │   └───windows/
            │       │   Essential_Windows_CMD&PowerShell_Commands.md
            │       │   
            │       └───powershell/
            │               
            └───Universal_RunnerApp/    # Universal Runner application
                │   __init__.py
                │   
                └───src/
                    │   __init__.py
                    │   
                    └───content/
                        │   __init__.py
                        │   
                        └───applications/
                            ├───code_review/
                            │   │   README.md
                            │   │   root.txt
                            │   │   __init__.py
                            │   │   
                            │   └───universal_runner/
                            │       │   main.py
                            │       │   requirements.txt
                            │       │   setup.py
                            │       │   __init__.py
                            │       │   
                            │       └───src/
                            │           │   __init__.py
                            │           │   
                            │           ├───cli/
                            │           │   │   main.py
                            │           │   │   __init__.py
                            │           │   │   
                            │           │   └───tests/
                            │           │           test_runner_functionality.py
                            │           │           
                            │           ├───runner/
                            │           │       formatter.py
                            │           │       formatter_map.py
                            │           │       language_map.py
                            │           │       linter.py
                            │           │       linter_map.py
                            │           │       utils.py
                            │           │       __init__.py
                            │           │       
                            │           ├───server/
                            │           │       app.py
                            │           │       
                            │           └───universal_runner_web/
                            │               │   .hintrc
                            │               │   app.js
                            │               │   index.html
                            │               │   styles.css
                            │               │   three.min.js
                            │               │   
                            │               └───css/
                            │                       tailwind.min.css
                            │                       
                            ├───LumenCast/          # Live streaming application
                            │   │   A_Versatile_Live_Streaming_App.md
                            │   │   
                            │   └───app/
                            │       │   .txt
                            │       │   
                            │       └───src/
                            │           ├───application/
                            │           ├───core/
                            │           ├───Infrastructure/
                            │           ├───Infrastructure.Firebase/
                            │           ├───Platform/
                            │           └───tests/
                            │               
                            ├───shadow/             # Security application
                            │   └───shadownet_sec/
                            │       │   app.py
                            │       │   requirements.txt
                            │       │   STRIDE Analysis for MVP.txt
                            │       │   __init__.py
                            │       │   
                            │       ├───docs/
                            │       ├───src/
                            │       │   ├───core/
                            │       │   ├───montioring/
                            │       │   ├───network/
                            │       │   └───tests/
                            │       │       
                            │       └───web/
                            │               
                            └───spiritapp/          # Android application
                                │   .gitignore
                                │   build.gradle.kts
                                │   gradle.properties
                                │   gradlew
                                │   gradlew.bat
                                │   local.properties
                                │   settings.gradle.kts
                                │   
                                ├───.gradle/
                                ├───.idea/
                                ├───app/
                                │   └───src/
                                │       ├───androidTest/
                                │       ├───main/
                                │       └───test/
                                │           
                                └───gradle/
```

---

## 📚 Documentation

### Main Documentation

- **[USOS README](Projects/in-dev/USOS/USOS_README.md)** - Comprehensive USOS project overview ⭐
- **[USOS Project Details](Projects/in-dev/USOS/USOS.md)** - In-development features

### Core Documentation

- **[USOS Project Overview](Project-Docs/USOS-Project.md)** - Complete project details
- **[Project Management](Project-Docs/Project_Management.md)** - Development planning and roadmap
- **[Full Project](Project-Docs/Full-project.md)** - Technical deep dive
- **[Developer Guide](Project-Docs/Dev_Guide.md)** - Development guidelines

### Extended Documentation

- **[AI Orchestration Worker](Project-Docs/Docs/AI%20Orchestration%20Worker.doc)** - AI integration
- **[Innovation README](Project-Docs/Docs/innovation_README.md)** - Innovation strategies
- **[Security Policy](Project-Docs/Docs/Security%20Policy.md)** - Security guidelines
- **[NO-Trust Policy](Project-Docs/Docs/NO-Trust-Policy.md)** - Zero-trust architecture
- **[Contribution Guidelines](Project-Docs/Docs/CONTRIBUTION_README.md)** - How to contribute
- **[Universal Runner Guidelines](Project-Docs/Docs/Universal%20Runner%20Contributing%20Guidelines.md)** - Runner development

### Technical Reports

- **[USOS Comprehensive Report](Project-Docs/Docs/USOS_Comprehensive_Report.md)** - Full USOS analysis
- **[USOS Technical Report](Project-Docs/Docs/USOS_Technical_Report.md)** - Technical specifications
- **[MobileOS Comprehensive Report](Project-Docs/Docs/MobileOS_Comprehensive_Report.md)** - Mobile OS analysis
- **[MobileOS Technical Report](Project-Docs/Docs/MobileOS_Technical_Report.md)** - Mobile technical specs

### Platform Guides

- **[Windows Commands](Platforms/windows/Essential_Windows_CMD&PowerShell_Commands.md)** - PowerShell reference
- **[Linux Commands](Platforms/unix/Ubuntu_linux_Cmd.md)** - Bash and Unix utilities
- **[Platform README](Projects/in-dev/USOS/PlatForms/README.md)** - Platform development guidelines

### Application Documentation

- **[Universal Runner](Projects/in-dev/USOS/Universal_RunnerApp/src/content/applications/code_review/universal_runner/README.md)** - Runner documentation
- **[LumenCast](Projects/in-dev/USOS/Universal_RunnerApp/src/content/applications/LumenCast/A_Versatile_Live_Streaming_App.md)** - Live streaming app
- **[ShadowNet Security](Projects/in-dev/USOS/Universal_RunnerApp/src/content/applications/shadow/shadownet_sec/docs/README.md)** - Security application

### Quick References

- **Installation**: See [Installation](#-installation) section above
- **Usage Examples**: Check platform-specific folders (`Platforms/windows/powershell/` or `Platforms/unix/linux/`)
- **Troubleshooting**: Review log files in each tool's output directory
- **Future Projects**: See [Ideas](Projects/ideas/FutureProjectsdoc.md)

---

## 🤝 Contributing

We welcome contributions from developers, educators, and users of all skill levels!

### How to Contribute

1. **Fork** this repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Areas Where We Need Help

- 🌐 **Platform Support**: macOS and Android implementations
- 📝 **Documentation**: Tutorials, guides, and translations
- 🔧 **Features**: New tools and automation scripts
- 🐛 **Testing**: Bug reports and quality assurance
- 🎨 **UI/UX**: Interface improvements and accessibility

---

## 🙋‍♂️ Support & Community

- **🐛 Issues**: [Report bugs and request features](../../issues)
- **💬 Discussions**: [Join community conversations](../../discussions)
- **📧 Contact**: Open an issue for questions and support

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### What This Means

- ✅ **Free to use** for personal and commercial projects
- ✅ **Modify and distribute** with attribution
- ✅ **No warranty** - use at your own risk
- ✅ **Community-driven** development and improvements

---

## 🌟 Acknowledgments

**The Journey**: What started in July 2024 as frustration with subscription software and a desire to learn Python has evolved into a comprehensive platform for digital independence.

- Built by [Beau-Ryan](https://github.com/beau-ryan) - one developer's journey from Python beginner to platform creator
- **Mission**: Prove that you can own your tools, learn by building, and break free from subscription culture
- **Timeline**: 0-8 months from "I want to learn Python" to foundational toolkit and platform prototype
- **Inspiration**: Every developer who's ever been frustrated with monthly fees and wanted to build their own solution
- Dedicated to users worldwide seeking to own their digital tools and learn through hands-on building

---

## **🎯 Born from subscription fatigue • Built for digital independence • Evolved into enterprise innovation**

**⭐ Star this repository if you're tired of subscription culture and want to own your tools!**

```markdown

[🚀 Get Started](#-quick-start)

[Documentation](#-documentation)

[🤝 Contribute](#-contributing)

```
