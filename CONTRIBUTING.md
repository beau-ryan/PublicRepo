# Contributing to USOS: Universal System Operations

First off, thank you for considering contributing to USOS! 🎉

We welcome contributions from developers, educators, and users of all skill levels. Your input helps make technology more accessible for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Areas We Need Help](#areas-we-need-help)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming, inclusive environment. By participating, you are expected to uphold these values:

- **Be respectful and inclusive** of different viewpoints and experiences
- **Focus on what's best for the community** and educational goals
- **Show empathy** towards other community members
- **Accept constructive criticism** gracefully
- **Help others learn** - remember our educational mission

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates.

**Good Bug Reports Include:**

- Clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- System information (OS, versions, etc.)
- Screenshots or logs if helpful

**Bug Report Template:**

```markdown
**Bug Description:**
Brief description of the issue

**To Reproduce:**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior:**
What should have happened

**System Information:**
- OS: [e.g., Windows 11, Ubuntu 22.04]
- Tool Version: [e.g., 1.2.3]
- Environment: [e.g., PowerShell 7.3]

**Additional Context:**
Add any other context about the problem here
```

### 💡 Suggesting Features

We love new ideas! Feature requests should:

- Align with our mission of accessibility and education
- Include clear use cases
- Consider cross-platform compatibility
- Think about beginner-friendliness

**Feature Request Template:**

```markdown
**Feature Description:**
Clear description of the proposed feature

**Problem It Solves:**
What user problem does this address?

**Proposed Solution:**
How should this feature work?

**Platforms:**
Which platforms should this support?

**Educational Value:**
How does this help users learn?
```

### 📝 Improving Documentation

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add examples and tutorials
- Translate content to other languages
- Create video tutorials or guides
- Improve code comments

### 🔧 Contributing Code

We welcome code contributions in all supported languages:

- **PowerShell** for Windows tools
- **Bash** for Linux/macOS scripts
- **Python** for cross-platform utilities
- **Documentation** improvements

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/beau-ryan/PublicRepo.git
cd PublicRepo

# Add upstream remote
git remote add upstream https://github.com/beau-ryan/PublicRepo.git
```

### 2. Set Up Development Environment

#### Windows Development

```powershell
# Ensure PowerShell execution policy allows scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Navigate to Windows tools
cd PlatForms\windows\powershell
```

#### Linux/macOS Development

```bash
# Make scripts executable
chmod +x PlatForms/unix/bashScripts/*.sh

# Navigate to Unix tools
cd PlatForms/unix/bashScripts
```

### 3. Create Feature Branch

```bash
# Update your main branch
git checkout master
git pull upstream master

# Create feature branch
git checkout -b feature/amazing-new-feature
```

## Development Process

### 1. **Plan First**

- Discuss major changes in an issue before coding
- Consider cross-platform compatibility
- Think about educational value and accessibility

### 2. **Code with Care**

- Follow our coding standards (below)
- Add comments explaining complex logic
- Include error handling and user feedback
- Test on multiple platforms when possible

### 3. **Document Everything**

- Update relevant README files
- Add inline comments for complex code
- Include usage examples
- Update help text and menus

### 4. **Test Thoroughly**

- Test your changes on your target platform
- Verify error handling works correctly
- Check that logging provides useful information
- Ensure backwards compatibility

## Coding Standards

### PowerShell Guidelines

```powershell
# Use approved verbs and clear function names
function Get-SystemInformation {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [string]$ComputerName
    )
    
    # Always include error handling
    try {
        # Clear, descriptive variable names
        $systemInfo = Get-WmiObject -Class Win32_ComputerSystem -ComputerName $ComputerName
        
        # Provide user feedback
        Write-Host "Successfully retrieved system information for $ComputerName" -ForegroundColor Green
        
        return $systemInfo
    }
    catch {
        Write-Error "Failed to get system information: $_"
        return $null
    }
}
```

### Bash Guidelines

```bash
#!/bin/bash

# Use strict error handling
set -euo pipefail

# Clear function names with comments
function check_system_health() {
    local log_file="/tmp/health_check.log"
    
    # Always validate inputs
    if [[ $# -eq 0 ]]; then
        echo "Error: No parameters provided" >&2
        return 1
    fi
    
    # Provide user feedback
    echo "Starting system health check..." | tee -a "$log_file"
    
    # Error handling with meaningful messages
    if ! command -v systemctl >/dev/null 2>&1; then
        echo "Warning: systemctl not found, skipping service checks" | tee -a "$log_file"
    fi
    
    echo "Health check completed. Log saved to: $log_file"
}
```

### General Guidelines

- **Clear Naming**: Use descriptive names for functions, variables, and files
- **Error Handling**: Always include proper error handling and user feedback
- **Logging**: Log important actions and errors for troubleshooting
- **Comments**: Explain complex logic and provide context
- **User Feedback**: Keep users informed of progress and results
- **Accessibility**: Consider users with different skill levels

## Commit Guidelines

### Commit Message Format

```bash
type(scope): brief description

Longer explanation if needed

Fixes #123
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Formatting changes (no code logic changes)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
feat(windows): add system health check script

Add comprehensive PowerShell script for Windows system health monitoring.
Includes disk space, memory usage, and service status checks.

Fixes #45

---

docs(readme): update installation instructions

Clarify PowerShell execution policy requirements and add troubleshooting section.

---

fix(linux): handle missing systemctl gracefully

Add proper error handling when systemctl is not available on older systems.

Fixes #67
```

## Pull Request Process

### 1. **Prepare Your PR**

```bash
# Update your branch with latest changes
git fetch upstream
git rebase upstream/master

# Run tests if available
# ./run-tests.sh

# Push your changes
git push origin feature/your-feature-name
```

### 2. **Create Pull Request**

Include in your PR description:

- **What**: Brief description of changes
- **Why**: Problem this solves or feature it adds
- **How**: Technical approach taken
- **Testing**: How you tested the changes
- **Platforms**: Which platforms this affects
- **Documentation**: Any docs that need updating

### 3. **PR Review Process**

- All PRs require review before merging
- Address feedback promptly and respectfully
- Update your branch if requested
- Squash commits if asked (we can help with this)

### 4. **After Merge**

```bash
# Clean up your local branches
git checkout master
git pull upstream master
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

## Areas We Need Help

### 🔥 High Priority

- **macOS Support**: Native tools and scripts for macOS users
- **Android Tools**: Mobile device management utilities
- **Documentation**: User guides and tutorials
- **Testing**: Cross-platform testing and validation

### 📚 Documentation Needs

- **Video Tutorials**: Screen recordings of tool usage
- **Beginner Guides**: Step-by-step tutorials for newcomers
- **Translation**: Translate guides to other languages
- **Examples**: Real-world usage scenarios

### 🛠️ Technical Areas

- **GUI Development**: User-friendly interfaces for command-line tools
- **Error Handling**: Improve error messages and recovery
- **Performance**: Optimize script execution speed
- **Security**: Security audits and improvements

### 🌐 Platform-Specific

- **Windows**: Advanced PowerShell modules and GUI tools
- **Linux**: Support for more distributions and package managers
- **macOS**: Native Objective-C or Swift implementations
- **Android**: Termux-compatible tools and utilities

## Recognition

Contributors are recognized in several ways:

- Listed in repository contributors
- Mentioned in release notes for significant contributions
- Special recognition for educational content and accessibility improvements

## Questions?

- **General Questions**: Open a [discussion](../../discussions)
- **Bug Reports**: Create an [issue](../../issues)
- **Feature Ideas**: Start with a [discussion](../../discussions) then create an issue
- **Security Issues**: Please email privately (see README for contact info)

## Thank You! 🙏

Every contribution, no matter how small, helps make technology more accessible to everyone. Whether you're fixing a typo, adding a feature, or helping other users, you're making a difference.
**Happy coding!** 🚀
