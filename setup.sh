#!/bin/bash

# War & Current Affairs Dashboard - Quick Setup Script
# This script automates the GitHub token setup and project creation

set -e

echo "==========================================="
echo "War & Current Affairs Dashboard"
echo "Quick Setup Script"
echo "==========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo "✓ Python 3 detected"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 is not installed"
    exit 1
fi

echo "✓ pip3 detected"
echo ""

# Install dependencies
echo "Step 1: Installing dependencies..."
pip3 install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Check for GitHub token
echo "Step 2: GitHub Token Setup"
echo "==================================="

if [ -z "$GITHUB_TOKEN" ]; then
    echo "⚠️  GITHUB_TOKEN environment variable not found"
    echo ""
    echo "To create a GitHub token:"
    echo "1. Go to: https://github.com/settings/tokens"
    echo "2. Click 'Generate new token'"
    echo "3. Select scopes: 'repo' and 'project'"
    echo "4. Generate and copy the token"
    echo ""
    read -p "Enter your GitHub Personal Access Token: " token
    
    if [ -z "$token" ]; then
        echo "❌ Error: No token provided"
        exit 1
    fi
    
    export GITHUB_TOKEN="$token"
    echo "✓ Token set for this session"
    echo ""
    
    # Ask to save to .env
    read -p "Save token to .env file for future use? (y/n): " save_env
    if [ "$save_env" = "y" ]; then
        echo "GITHUB_TOKEN=$token" > .env
        echo "✓ Token saved to .env file"
        echo "⚠️  Remember to add .env to .gitignore!"
    fi
else
    echo "✓ GITHUB_TOKEN found in environment"
fi

echo ""

# Create project
echo "Step 3: Creating War & Current Affairs Dashboard"
echo "=================================================="
echo ""

python3 create_war_dashboard_project.py

echo ""
echo "==========================================="
echo "✓ Setup Complete!"
echo "==========================================="
echo ""
echo "Your War & Current Affairs Dashboard has been created!"
echo ""
echo "Next steps:"
echo "1. Visit the project at: https://github.com/ARUSHAMMU262007/automotive-cybersecurity/projects"
echo "2. Review the setup guide: WAR_DASHBOARD_SETUP.md"
echo "3. Start adding conflict and event data"
echo "4. Configure team access permissions"
echo "5. Set up automated updates if needed"
echo ""
echo "For more information, see WAR_DASHBOARD_SETUP.md"
