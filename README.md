# War & Current Affairs Dashboard - GitHub Projects API Setup

## 🎯 Overview

This is a comprehensive **GitHub Projects-based dashboard** for tracking global conflicts, geopolitical developments, military operations, humanitarian crises, peace negotiations, and real-time current affairs data with verified sources.

## 📦 What's Included

- **`create_war_dashboard_project.py`** - Python script to automate project creation via GitHub API
- **`war-dashboard-api-config.json`** - Configuration file with all dashboard specifications
- **`WAR_DASHBOARD_SETUP.md`** - Comprehensive setup and implementation guide
- **`requirements.txt`** - Python dependencies
- **`setup.sh`** - Automated setup script for macOS/Linux
- **`setup.bat`** - Automated setup script for Windows
- **`.env.example`** - Environment variables template

## ⚡ Quick Start (Choose One)

### Option 1: Automated Setup (Easiest)

**macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows:**
```bash
setup.bat
```

### Option 2: Manual Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate GitHub Token:**
   - Go to https://github.com/settings/tokens
   - Create token with `repo` and `project` scopes
   - Copy the token

3. **Set environment variable:**
   ```bash
   export GITHUB_TOKEN='your_token_here'
   ```

4. **Run the script:**
   ```bash
   python3 create_war_dashboard_project.py
   ```

## 📊 Dashboard Features

### 8 Main Tracking Sections

1. **Active Conflicts & War Zones** - Global conflict monitoring
2. **Military Operations & Tactics** - Military action tracking
3. **Humanitarian Crisis Data** - Crisis response and aid
4. **Geopolitical Developments** - International relations
5. **Peace Negotiations & Treaties** - Peace efforts
6. **International Response & Sanctions** - Global response measures
7. **Real-time Current Affairs** - Breaking news and developments
8. **Data & Statistics** - Verified metrics and statistics

### Data Sources

- UN Official Reports
- Red Cross/Red Crescent
- Reuters & AP News
- BBC News
- Government Official Statements
- International Criminal Court
- Human Rights Watch
- OCHA & SIPRI

## ✅ Accuracy Standards

- **Cross-verification**: Minimum 2 reliable sources per claim
- **Timestamps**: All information dated and timestamped
- **Attribution**: Full source citations
- **Distinction**: Clear separation of confirmed vs. unconfirmed reports
- **Update Frequency**: Critical events within 24 hours

## 📋 File Descriptions

| File | Purpose |
|------|----------|
| `create_war_dashboard_project.py` | Main automation script |
| `war-dashboard-api-config.json` | Project configuration |
| `WAR_DASHBOARD_SETUP.md` | Complete setup guide |
| `requirements.txt` | Python dependencies |
| `setup.sh` | Linux/macOS setup |
| `setup.bat` | Windows setup |
| `.env.example` | Environment template |

## 🔧 API Endpoints Used

- `POST /repos/{owner}/{repo}/projects` - Create project
- `POST /projects/{project_id}/columns` - Create columns
- `POST /repos/{owner}/{repo}/issues` - Create tracking issues
- `POST /projects/columns/{column_id}/cards` - Add cards to columns

## 🛡️ Security Notes

- ⚠️ Never commit `.env` file with real tokens
- Use `export GITHUB_TOKEN=...` or `.env` file (in .gitignore)
- Rotate tokens regularly
- Limit token permissions to minimum needed
- Enable 2FA on GitHub account

## 📞 Need Help?

Refer to **WAR_DASHBOARD_SETUP.md** for:
- Detailed implementation guide
- Troubleshooting section
- Template examples
- Automation options
- Team collaboration guidelines

## 🚀 Next Steps After Setup

1. Visit your project dashboard
2. Review the setup guide
3. Add real conflict/event data
4. Configure team permissions
5. Set up automated updates
6. Start tracking global events

## 📄 License

MIT License - See LICENSE file for details

---

**Version**: 1.0  
**Last Updated**: June 25, 2026  
**Maintainer**: ARUSHAMMU262007

**Repository**: https://github.com/ARUSHAMMU262007/automotive-cybersecurity
