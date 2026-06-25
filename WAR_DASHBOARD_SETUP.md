# War & Current Affairs Dashboard - Implementation Guide

## 📊 Project Overview

A comprehensive GitHub-based dashboard for tracking global conflicts, geopolitical developments, military operations, humanitarian crises, peace negotiations, and real-time current affairs with verified data sources.

---

## 🚀 Quick Start

### Prerequisites
- GitHub Account
- GitHub Personal Access Token with `repo` and `project` scopes
- Python 3.7+
- `requests` library (`pip install requests`)

### Step 1: Generate GitHub Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token"
3. Give it a descriptive name: `War Dashboard API Access`
4. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `project` (Full control of projects)
5. Click "Generate token"
6. **Copy the token** (you won't see it again)

### Step 2: Set Environment Variable

**On macOS/Linux:**
```bash
export GITHUB_TOKEN='your_copied_token_here'
```

**On Windows (PowerShell):**
```powershell
$env:GITHUB_TOKEN='your_copied_token_here'
```

### Step 3: Run the Setup Script

```bash
python3 create_war_dashboard_project.py
```

### Expected Output
```
============================================================
War & Current Affairs Dashboard Setup
============================================================

Step 1: Creating project...
✓ Project created successfully!
  Project ID: 1234567
  Name: War & Current Affairs Dashboard
  URL: https://github.com/ARUSHAMMU262007/automotive-cybersecurity/projects/1

Step 2: Creating columns...
✓ Column created: Active Conflicts
✓ Column created: Military Operations
✓ Column created: Humanitarian Crisis
✓ Column created: Geopolitical Events
✓ Column created: Peace Negotiations
✓ Column created: International Response
✓ Column created: Current Affairs
✓ Column created: Statistics & Data

Step 3: Creating sample tracking issues...
✓ Issue created: [Active Conflict] Middle East Conflict Tracking
  Issue #: 1
✓ Issue created: [Humanitarian] Crisis Response & Aid Assessment
  Issue #: 2
✓ Issue created: [Geopolitical] International Relations & Development
  Issue #: 3
✓ Issue created: [Peace Talks] Negotiation Tracking & Mediation
  Issue #: 4
✓ Issue created: [Data] Statistics & Metrics Tracking
  Issue #: 5

============================================================
✓ Dashboard setup complete!
============================================================

Project URL: https://github.com/ARUSHAMMU262007/automotive-cybersecurity/projects/1

Next Steps:
1. Add real conflict/event data to the tracking issues
2. Configure automated updates for real-time data
3. Set up team permissions and access
4. Enable notifications for critical updates
5. Link to reliable data sources (UN, Reuters, AP, etc.)
```

---

## 📋 Dashboard Structure

### 8 Main Columns/Sections

#### 1. **Active Conflicts & War Zones**
Track ongoing conflicts globally
- Conflict name and location
- Start date and current status
- Parties involved
- Casualty counts and displaced persons
- International involvement level

#### 2. **Military Operations & Tactics**
Document military operations and strategies
- Operation name and date
- Location and combatants
- Outcome and casualties
- Equipment and strategic significance

#### 3. **Humanitarian Crisis Data**
Monitor humanitarian emergencies
- Crisis location and type
- Affected population
- Severity assessment
- Aid organizations involved
- Funding status and urgent needs

#### 4. **Geopolitical Developments**
Track international relations changes
- Event title and date
- Countries involved
- Implications (regional/global)
- International response
- Diplomatic actions

#### 5. **Peace Negotiations & Treaties**
Monitor peace efforts
- Negotiation name and location
- Parties and mediators
- Progress status
- Key points and agreements
- Expected outcomes

#### 6. **International Response & Sanctions**
Track global response measures
- Sanction type
- Imposing countries/organizations
- Target entities
- Reason and duration
- Impact assessment

#### 7. **Real-time Current Affairs**
Capture breaking news and developments
- News title and date
- Source and credibility rating
- Impact level
- Related conflicts
- Follow-up actions needed

#### 8. **Data & Statistics**
Maintain verified metrics
- Metric names and values
- Data source and confidence level
- Trend analysis
- Historical comparison
- Important notes

---

## 🔍 Data Source Standards

### Verified Information Sources (Priority Order)

1. **Official Government Sources**
   - Official government statements
   - Ministry of Foreign Affairs
   - Military official releases

2. **International Organizations**
   - United Nations (UN.org)
   - International Committee of the Red Cross (ICRC)
   - UN Office for Coordination of Humanitarian Affairs (OCHA)
   - International Criminal Court (ICC)

3. **Reputable News Agencies**
   - Reuters
   - Associated Press (AP)
   - BBC News
   - AFP (Agence France-Presse)

4. **Specialized Tracking Organizations**
   - SIPRI (Stockholm International Peace Research Institute)
   - Human Rights Watch
   - Amnesty International
   - Crisis Group

5. **Academic & Research Institutions**
   - University conflict research centers
   - Think tanks (Brookings, RAND, etc.)

---

## ✅ Accuracy Standards

### Cross-Reference Requirements
- **Minimum Sources**: Every claim must be verified by at least 2 independent reliable sources
- **Timestamp**: All information must include verification timestamp
- **Attribution**: Always cite the specific source
- **Distinction**: Clearly separate:
  - ✅ Confirmed events (reported by official sources)
  - ⚠️ Unconfirmed reports (single source, needs verification)
  - ❌ Disputed claims (contradictory reports)

### Update Frequency
- **Critical Events**: Within 24 hours of verification
- **Major Developments**: Within 48 hours
- **Routine Updates**: Weekly minimum
- **Statistics**: Monthly or as new data released

### Data Validation Checklist
Before adding any information:
- [ ] Source is reliable and verified
- [ ] Information is current and relevant
- [ ] Cross-referenced with at least one other source
- [ ] Timestamp is included
- [ ] Source attribution is clear
- [ ] Distinction noted if unconfirmed
- [ ] No personal opinion or speculation added

---

## 🔧 API Endpoints Reference

### Create Project
```bash
POST /repos/{owner}/{repo}/projects
Authorization: Bearer YOUR_GITHUB_TOKEN
Accept: application/vnd.github.inertia-preview+json

{
  "name": "War & Current Affairs Dashboard",
  "body": "Project description"
}
```

### Create Project Column
```bash
POST /projects/{project_id}/columns
Authorization: Bearer YOUR_GITHUB_TOKEN
Accept: application/vnd.github.inertia-preview+json

{
  "name": "Active Conflicts"
}
```

### Create Issue
```bash
POST /repos/{owner}/{repo}/issues
Authorization: Bearer YOUR_GITHUB_TOKEN

{
  "title": "[Active Conflict] Conflict Name",
  "body": "Issue description with details",
  "labels": ["active-conflicts", "region-name"]
}
```

### Add Card to Column
```bash
POST /projects/columns/{column_id}/cards
Authorization: Bearer YOUR_GITHUB_TOKEN
Accept: application/vnd.github.inertia-preview+json

{
  "content_id": 12345,
  "content_type": "Issue"
}
```

---

## 🏷️ Recommended Labels

Create these labels for better organization:

```
- active-conflicts (red)
- military-operations (darkred)
- humanitarian-crisis (orange)
- geopolitical (blue)
- peace-negotiations (green)
- sanctions (yellow)
- current-affairs (purple)
- statistics (gray)
- urgent (red with exclamation)
- verified (green checkmark)
- unconfirmed (yellow warning)
- disputed (orange warning)
```

---

## 📱 Template Examples

### Active Conflict Tracking Template
```
**Conflict Name**: [Name]
**Location**: [Geographic coordinates if available]
**Start Date**: [Date]
**Current Status**: [Ongoing/Ceasefire/Escalating/De-escalating]
**Parties Involved**: [All parties]
**Casualty Count**: [Number with source]
**Displaced Persons**: [Number with source]
**International Involvement**: [Countries/Organizations involved]

## Recent Developments
- [Latest development with timestamp]
- [Previous significant update]

## Sources
1. [Source 1 with link]
2. [Source 2 with link]

## Last Updated
[Date and time]
```

### Humanitarian Crisis Template
```
**Crisis Type**: [Type]
**Location**: [Location]
**Affected Population**: [Number]
**Severity Level**: [Critical/High/Medium/Low]

## Aid Organizations Active
- [Organization 1]
- [Organization 2]

## Funding Status
- Total Required: $[Amount]
- Pledged: $[Amount]
- Funding Gap: $[Amount]

## Urgent Needs
1. [Need 1]
2. [Need 2]
3. [Need 3]

## Sources
1. [Source with link]
2. [Source with link]
```

---

## 🔄 Automation Options

### GitHub Actions Integration
Create `.github/workflows/update-dashboard.yml`:

```yaml
name: Update Dashboard

on:
  schedule:
    # Run daily at 9 AM UTC
    - cron: '0 9 * * *'
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Update conflict data
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python3 create_war_dashboard_project.py
```

### Webhook Integration
Setup webhooks to:
- Monitor news APIs
- Track UN feeds
- Monitor Reuters/AP news feeds
- Integrate with OCHA crisis alerts

---

## 👥 Team Collaboration

### Access Levels
- **Admin**: Can create/edit all data, manage project structure
- **Editor**: Can add/edit entries and update information
- **Viewer**: Read-only access for monitoring

### Discussion Guidelines
1. Use issue comments for discussions
2. Pin verified source links
3. Tag relevant team members for review
4. Use labels for quick categorization
5. Reference related issues

---

## 📊 Metrics & Analytics

### Track These Metrics
- Number of active conflicts
- Total affected population
- Displaced persons count
- Humanitarian funding gaps
- Active peace negotiations
- Sanctions in effect
- Major geopolitical events

### Generate Reports
Create monthly reports summarizing:
- New conflicts emerged
- Conflicts resolved
- Humanitarian impacts
- International responses
- Peace progress

---

## 🛡️ Security & Privacy

- Keep token secure (never commit to repo)
- Use environment variables for sensitive data
- Limit API token permissions to minimum needed
- Enable 2FA on GitHub account
- Regularly rotate access tokens
- Audit access logs

---

## 🔗 Useful Resources

- **UN Data**: https://data.un.org
- **OCHA Crisis Data**: https://www.humanitarianresponse.info
- **SIPRI Conflict Data**: https://www.sipri.org
- **Human Rights Watch**: https://www.hrw.org
- **Reuters News**: https://reuters.com
- **BBC News**: https://bbc.com/news
- **GitHub API Docs**: https://docs.github.com/en/rest

---

## 🐛 Troubleshooting

### Issue: "Invalid GitHub Token"
- Verify token has `repo` and `project` scopes
- Check token hasn't expired
- Regenerate token if needed

### Issue: "403 Forbidden Error"
- Ensure account has repository access
- Check token permissions
- Verify repository settings allow projects

### Issue: "404 Not Found"
- Verify owner/repo names are correct
- Check repository exists and is accessible
- Ensure project ID is valid

### Issue: Script Hangs
- Check internet connection
- Verify GitHub API is accessible
- Check rate limits: `curl -H "Authorization: Bearer TOKEN" https://api.github.com/rate_limit`

---

## 📞 Support & Contributions

For issues, improvements, or contributions:
1. Create an issue in the repository
2. Submit with detailed information
3. Include relevant sources
4. Follow accuracy standards
5. Link related issues

---

## 📝 License

This project follows the same license as the parent repository: **MIT License**

---

**Last Updated**: June 25, 2026
**Maintained By**: ARUSHAMMU262007
