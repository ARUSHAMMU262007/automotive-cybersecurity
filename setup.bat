@echo off
REM War & Current Affairs Dashboard - Quick Setup Script for Windows
REM This script automates the GitHub token setup and project creation

setlocal enabledelayedexpansion

echo ==========================================
echo War ^& Current Affairs Dashboard
echo Quick Setup Script (Windows)
echo ==========================================
echo.

REM Check if Python 3 is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python 3 is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://www.python.org
    pause
    exit /b 1
)

echo ✓ Python 3 detected
echo.

REM Install dependencies
echo Step 1: Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error installing dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed
echo.

REM Check for GitHub token
echo Step 2: GitHub Token Setup
echo ==================================

if "%GITHUB_TOKEN%"==" (
    echo ⚠ GITHUB_TOKEN environment variable not found
    echo.
    echo To create a GitHub token:
    echo 1. Go to: https://github.com/settings/tokens
    echo 2. Click 'Generate new token'
    echo 3. Select scopes: 'repo' and 'project'
    echo 4. Generate and copy the token
    echo.
    
    set /p token="Enter your GitHub Personal Access Token: "
    
    if "!token!"==" (
        echo Error: No token provided
        pause
        exit /b 1
    )
    
    setx GITHUB_TOKEN "!token!"
    echo ✓ Token set (requires new command prompt to take effect)
    echo.
) else (
    echo ✓ GITHUB_TOKEN found in environment
)

echo.

REM Create project
echo Step 3: Creating War ^& Current Affairs Dashboard
echo ==================================================
echo.

python create_war_dashboard_project.py

echo.
echo ==========================================
echo ✓ Setup Complete!
echo ==========================================
echo.
echo Your War ^& Current Affairs Dashboard has been created!
echo.
echo Next steps:
echo 1. Visit the project at: https://github.com/ARUSHAMMU262007/automotive-cybersecurity/projects
echo 2. Review the setup guide: WAR_DASHBOARD_SETUP.md
echo 3. Start adding conflict and event data
echo 4. Configure team access permissions
echo 5. Set up automated updates if needed
echo.
echo For more information, see WAR_DASHBOARD_SETUP.md
echo.
pause
