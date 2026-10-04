#!/usr/bin/env python3
"""
Daily Maya Journal Entry Generator
This script is called by the daily cron job to generate a new journal entry.
"""
import os
import sys
import subprocess
import json
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNAL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "journal.html")

def get_today_date():
    """Get today's date in format 'Month DD, YYYY'"""
    return datetime.now().strftime("%B %d, %Y")

def git_commit_and_push(message):
    """Commit and push changes to git."""
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        subprocess.run(["git", "add", "journal.html"], check=True, cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")
        return False

def main():
    # This script is called by the cron job
    # The actual content generation would be done by an LLM
    # For now, we just ensure the repo is clean
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Check git status
    result = subprocess.run(["git", "status", "--porcelain"], cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))), capture_output=True, text=True)
    if result.stdout.strip():
        print("Working tree not clean, committing changes...")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-commit before daily journal"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
    
    print(f"[{datetime.now()}] Daily journal entry generation ready.")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
