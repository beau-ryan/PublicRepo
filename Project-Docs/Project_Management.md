# PowerShell Commands for  Project Management

---

## 1. Show Folder Tree

```powershell
Tree /F > project.txt
Tree /F > full_project_tree.txt
Tree /F > root_tree.txt    
Tree /F > src_tree.txt  
clear
```

---

## 2. Create Folders and Files

```powershell
# Create a new folder
mkdir NewFolderName

# Create a subfolder
mkdir NewFolderName\SubFolderName

# Create a new file inside a folder
New-Item -Path NewFolderName\filename.txt -ItemType File
```

---

## 3. Create and Activate a Virtual Environment

```powershell
or you can name the venv folder anything you like

python -m venv .venv(3.11.9)
.venv(3.11.9)\Scripts\Activate.ps1

```powershell
python.exe -m pip install --upgrade pip
---

## 4. Upgrade pip (Recommended)
Optionally you can run this command to ensure pip is up to date.

```powershell
python -m pip install --upgrade pip

```powershell
pip install -r Env_Library\requirements-dev.txt 
pip install -r Env_Library\requirements.txt
---

## 5. Install Dependencies

```powershell
pip install -r Env_Library\requirements.txt

```powershell
pip install python-dotenv
pip install psutil

---

## 6. Copy .env.example to .env (If Needed)

```powershell
Copy-Item .env.example .env
```

---

## 7. Run the Main Application (Adjust Path as Needed)

```powershell
python Universal_RunnerApp\Universal_Runner.py
```

---

## 8. Check Python Version

```powershell
python --version
```

---

## 9. List Installed Packages

```powershell
pip list
pip list --outdated
```

---

## 10. Run Tests (Adjust Path as Needed)

```powershell
python -m unittest discover
```

---

## 11. Freeze Current Environment to requirements.txt

```powershell
pip freeze > Env_Library\requirements.txt
```

---

## 12. Deactivate Virtual Environment

```powershell
deactivate
```

---

## 13. Remove Virtual Environment (Use with Caution)

```powershell
Remove-Item -Recurse -Force .venv(3.11.9)
```

---

## 14. Remove All __pycache__ Folders Recursively

```powershell
Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
```

---

## 15. Change Directory

```powershell
cd C:USOS
cd C:USOS\Universal_RunnerApp
cd C:USOS\Universal_RunnerApp\src
```

---

## Project Management Documentation

This document provides a collection of PowerShell commands for managing Python projects, including creating virtual environments, installing dependencies, and running applications.
