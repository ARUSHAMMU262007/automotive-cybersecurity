#!/usr/bin/env python3
"""
GitHub War & Current Affairs Dashboard Project Creator
Creates a comprehensive project for tracking global conflicts, geopolitical events, and current affairs
"""

import requests
import json
import sys
from typing import Dict, Any, Optional

class WarDashboardProjectCreator:
    """Create and manage War & Current Affairs Dashboard via GitHub API"""
    
    def __init__(self, github_token: str, owner: str = "ARUSHAMMU262007", repo: str = "automotive-cybersecurity"):
        """
        Initialize the project creator
        
        Args:
            github_token: GitHub Personal Access Token with 'repo' and 'project' scopes
            owner: Repository owner (default: ARUSHAMMU262007)
            repo: Repository name (default: automotive-cybersecurity)
        """
        self.token = github_token
        self.owner = owner
        self.repo = repo
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.inertia-preview+json",
            "Content-Type": "application/json"
        }
        self.project_id = None
        self.columns = {}
    
    def create_project(self) -> Dict[str, Any]:
        """Create the main War & Current Affairs Dashboard project"""
        
        project_data = {
            "name": "War & Current Affairs Dashboard",
            "body": """Comprehensive tracking system for global conflicts, geopolitical developments, and current affairs with real-time data integration.

Sections:
- Active Conflicts & War Zones
- Military Operations & Tactics
- Humanitarian Crisis Data
- Geopolitical Developments
- Peace Negotiations & Treaties
- International Response & Sanctions
- Real-time Current Affairs
- Data & Statistics

Data Sources: UN, Red Cross, Reuters, AP, BBC, ICC, Human Rights Watch, OCHA, SIPRI
Accuracy Standards: Cross-referenced sources, verified timestamps, confirmed vs unconfirmed reporting"""
        }
        
        url = f"{self.base_url}/repos/{self.owner}/{self.repo}/projects"
        
        try:
            response = requests.post(url, headers=self.headers, json=project_data)
            response.raise_for_status()
            
            project = response.json()
            self.project_id = project.get("id")
            
            print(f"✓ Project created successfully!")
            print(f"  Project ID: {self.project_id}")
            print(f"  Name: {project.get('name')}")
            print(f"  URL: {project.get('html_url')}")
            
            return project
        
        except requests.exceptions.RequestException as e:
            print(f"✗ Error creating project: {e}")
            if hasattr(e.response, 'json'):
                print(f"  Details: {e.response.json()}")
            return {}
    
    def create_columns(self) -> Dict[str, Dict[str, Any]]:
        """Create project columns for different sections"""
        
        column_names = [
            "Active Conflicts",
            "Military Operations",
            "Humanitarian Crisis",
            "Geopolitical Events",
            "Peace Negotiations",
            "International Response",
            "Current Affairs",
            "Statistics & Data"
        ]
        
        if not self.project_id:
            print("✗ Project ID not set. Create project first.")
            return {}
        
        columns_created = {}
        
        for column_name in column_names:
            url = f"{self.base_url}/projects/{self.project_id}/columns"
            data = {"name": column_name}
            
            try:
                response = requests.post(url, headers=self.headers, json=data)
                response.raise_for_status()
                
                column = response.json()
                columns_created[column_name] = column
                
                print(f"✓ Column created: {column_name}")
                self.columns[column_name] = column.get("id")
            
            except requests.exceptions.RequestException as e:
                print(f"✗ Error creating column '{column_name}': {e}")
        
        return columns_created
    
    def create_issue(self, title: str, body: str, labels: Optional[list] = None) -> Dict[str, Any]:
        """
        Create an issue to track in the project
        
        Args:
            title: Issue title
            body: Issue description
            labels: Optional list of labels
        """
        
        issue_data = {
            "title": title,
            "body": body
        }
        
        if labels:
            issue_data["labels"] = labels
        
        url = f"{self.base_url}/repos/{self.owner}/{self.repo}/issues"
        
        try:
            response = requests.post(url, headers=self.headers, json=issue_data)
            response.raise_for_status()
            
            issue = response.json()
            print(f"✓ Issue created: {title}")
            print(f"  Issue #: {issue.get('number')}")
            
            return issue
        
        except requests.exceptions.RequestException as e:
            print(f"✗ Error creating issue: {e}")
            return {}
    
    def add_card_to_column(self, column_id: int, content_id: int, content_type: str = "Issue") -> Dict[str, Any]:
        """
        Add a card (issue) to a project column
        
        Args:
            column_id: The column ID
            content_id: The issue/PR ID
            content_type: Type of content (Issue or PullRequest)
        """
        
        card_data = {
            "content_id": content_id,
            "content_type": content_type
        }
        
        url = f"{self.base_url}/projects/columns/{column_id}/cards"
        
        try:
            response = requests.post(url, headers=self.headers, json=card_data)
            response.raise_for_status()
            
            card = response.json()
            print(f"✓ Card added to column")
            
            return card
        
        except requests.exceptions.RequestException as e:
            print(f"✗ Error adding card: {e}")
            return {}
    
    def setup_dashboard(self) -> bool:
        """Setup the complete dashboard with project, columns, and sample issues"""
        
        print("\n" + "="*60)
        print("War & Current Affairs Dashboard Setup")
        print("="*60 + "\n")
        
        # Step 1: Create project
        print("Step 1: Creating project...")
        project = self.create_project()
        
        if not self.project_id:
            print("✗ Failed to create project. Aborting.")
            return False
        
        print()
        
        # Step 2: Create columns
        print("Step 2: Creating columns...")
        self.create_columns()
        
        print()
        
        # Step 3: Create sample issues
        print("Step 3: Creating sample tracking issues...")
        
        sample_issues = [
            {
                "title": "[Active Conflict] Middle East Conflict Tracking",
                "body": """Track ongoing conflicts in the Middle East region
                
**Status**: Active
**Region**: Middle East
**Parties Involved**: Multiple
**Last Updated**: [Auto-update timestamp]
**Data Sources**: UN, Reuters, AP, BBC

### Key Metrics
- Affected Population: [Data]
- Displaced Persons: [Data]
- Casualty Count: [Data]

### Recent Updates
- [Latest development]
- [Previous update]
""",
                "labels": ["active-conflicts", "middle-east"]
            },
            {
                "title": "[Humanitarian] Crisis Response & Aid Assessment",
                "body": """Track humanitarian crises and aid response efforts
                
**Crisis Type**: [Type]
**Location**: [Location]
**Severity Level**: [Level]
**Affected Population**: [Number]

### Organizations Involved
- International Red Cross/Red Crescent
- UN OCHA
- WHO
- Other NGOs

### Funding Status
- Total Required: [Amount]
- Funded: [Amount]
- Gap: [Amount]

### Urgent Needs
- [Need 1]
- [Need 2]
- [Need 3]
""",
                "labels": ["humanitarian-crisis", "aid-response"]
            },
            {
                "title": "[Geopolitical] International Relations & Development",
                "body": """Track geopolitical developments and international relations
                
**Event**: [Event Title]
**Date**: [Date]
**Countries Involved**: [Countries]
**Significance**: [High/Medium/Low]

### Implications
- Regional Impact: [Description]
- Global Impact: [Description]
- Economic Impact: [Description]

### International Response
- UN Statement: [Statement]
- Major Countries Response: [Responses]
- Sanctions/Actions: [If applicable]
""",
                "labels": ["geopolitical", "international-relations"]
            },
            {
                "title": "[Peace Talks] Negotiation Tracking & Mediation",
                "body": """Track ongoing peace negotiations and diplomatic efforts
                
**Negotiation**: [Name]
**Location**: [Location]
**Parties**: [Parties Involved]
**Mediators**: [Mediating Countries/Organizations]
**Start Date**: [Date]

### Progress Status
- Phase: [Current Phase]
- Key Points Discussed: [Points]
- Agreements Reached: [Agreements]
- Outstanding Issues: [Issues]

### Next Steps
- Scheduled Meetings: [Dates]
- Expected Outcomes: [Outcomes]
- Timeline: [Timeline]
""",
                "labels": ["peace-negotiations", "mediation"]
            },
            {
                "title": "[Data] Statistics & Metrics Tracking",
                "body": """Maintain accurate statistics and key metrics
                
**Metric**: [Metric Name]
**Current Value**: [Value]
**Previous Value**: [Value]
**Trend**: [Up/Down/Stable]
**Data Source**: [Verified Source]
**Confidence Level**: [High/Medium/Low]

### Historical Data
- Date 1: [Value]
- Date 2: [Value]
- Date 3: [Value]

### Notes
- [Important note]
- [Additional context]
""",
                "labels": ["statistics", "data-tracking"]
            }
        ]
        
        for issue_data in sample_issues:
            self.create_issue(
                title=issue_data["title"],
                body=issue_data["body"],
                labels=issue_data.get("labels", [])
            )
        
        print()
        print("="*60)
        print("✓ Dashboard setup complete!")
        print("="*60)
        print(f"\nProject URL: https://github.com/{self.owner}/{self.repo}/projects/{self.project_id}")
        print("\nNext Steps:")
        print("1. Add real conflict/event data to the tracking issues")
        print("2. Configure automated updates for real-time data")
        print("3. Set up team permissions and access")
        print("4. Enable notifications for critical updates")
        print("5. Link to reliable data sources (UN, Reuters, AP, etc.)")
        
        return True


def main():
    """Main execution"""
    
    # Get GitHub token from environment or user input
    import os
    github_token = os.getenv("GITHUB_TOKEN")
    
    if not github_token:
        print("Error: GITHUB_TOKEN environment variable not set")
        print("\nTo use this script:")
        print("1. Create a GitHub Personal Access Token with 'repo' and 'project' scopes")
        print("2. Set it as an environment variable: export GITHUB_TOKEN='your_token'")
        print("3. Run this script again")
        sys.exit(1)
    
    # Create the dashboard
    creator = WarDashboardProjectCreator(github_token)
    success = creator.setup_dashboard()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
