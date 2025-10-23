import os
import subprocess
import datetime
import random
import time

def setup_educational_repo():
    """Initialize a repository for educational purposes"""
    print("Setting up educational repository...")
    
    # Create important disclaimer file
    with open("DISCLAIMER.md", "w") as f:
        f.write("# EDUCATIONAL PURPOSE ONLY\n\n")
        f.write("This repository demonstrates git date manipulation for learning purposes.\n")
        f.write("DO NOT use this to misrepresent your actual work or contributions.\n")
        f.write("Real coding practice is always better than artificial commits.\n\n")
        f.write("Created for understanding git internals and date handling mechanisms.\n")
    
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"], check=True)
        print("✓ Git repository initialized")
    
    # Create initial commit
    subprocess.run(["git", "add", "DISCLAIMER.md"], check=True)
    
    # Set current date for the disclaimer commit
    current_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = current_date
    env["GIT_COMMITTER_DATE"] = current_date
    
    subprocess.run([
        "git", "commit", "-m", 
        "Add educational purpose disclaimer"
    ], env=env, check=True)
    print("✓ Disclaimer commit created")

def create_educational_commits():
    """Create educational commits with past dates"""
    print("\nStarting educational commit creation...")
    
    # Calculate date range (last 90 days for demo - shorter than 365)
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=90)
    current_date = start_date
    
    commit_count = 0
    total_days = 90
    
    # Common commit messages for educational context
    messages = [
        "Learn: Study git date functionality",
        "Docs: Add educational notes",
        "Demo: Show git commit date manipulation",
        "Test: Verify git date commands",
        "Example: Demonstrate educational use case",
        "Update: Add learning progress",
        "Fix: Correct educational example"
    ]
    
    for day in range(total_days):
        # Skip weekends occasionally for realism
        if current_date.weekday() >= 5 and random.random() > 0.3:
            current_date += datetime.timedelta(days=1)
            continue
        
        # Determine how many commits today (0-3)
        commits_today = random.choices([0, 1, 2, 3], weights=[0.2, 0.5, 0.2, 0.1])[0]
        
        for commit_num in range(commits_today):
            # Create random time during working hours
            hour = random.randint(9, 17)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            
            commit_date = current_date.replace(
                hour=hour, minute=minute, second=second
            )
            git_date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
            
            # Create or modify a file
            with open("learning_log.md", "a") as f:
                f.write(f"## {commit_date.strftime('%Y-%m-%d %H:%M')}\n")
                f.write(f"Educational commit #{commit_count + 1}\n")
                f.write(f"Purpose: Understanding git date manipulation\n\n")
            
            # Stage changes
            subprocess.run(["git", "add", "learning_log.md"], check=True)
            
            # Prepare environment with custom dates
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = git_date_str
            env["GIT_COMMITTER_DATE"] = git_date_str
            
            # Create commit
            message = random.choice(messages)
            full_message = f"{message} - {commit_date.strftime('%Y-%m-%d')}"
            
            subprocess.run([
                "git", "commit", "-m", full_message
            ], env=env, capture_output=True)
            
            commit_count += 1
            
            # Show progress
            if commit_count % 10 == 0:
                print(f"  Created {commit_count} educational commits...")
        
        # Move to next day
        current_date += datetime.timedelta(days=1)
    
    return commit_count

def verify_commits():
    """Verify the created commits"""
    print("\nVerifying educational commits...")
    
    # Get commit history
    result = subprocess.run([
        "git", "log", "--oneline", "--date=short", 
        "--pretty=format:%h %ad %s", "--reverse"
    ], capture_output=True, text=True, check=True)
    
    commits = result.stdout.strip().split('\n')
    
    print(f"Total commits created: {len(commits)}")
    print("\nFirst 5 commits:")
    for commit in commits[:5]:
        print(f"  {commit}")
    
    print("\nLast 5 commits:")
    for commit in commits[-5:]:
        print(f"  {commit}")

def main():
    """Main educational demonstration"""
    print("=" * 60)
    print("GIT DATE MANIPULATION - EDUCATIONAL DEMONSTRATION")
    print("=" * 60)
    print("Purpose: Learn how git handles custom commit dates")
    print("Warning: For educational use only!")
    print("=" * 60)
    
    try:
        # Step 1: Setup
        setup_educational_repo()
        
        # Step 2: Create educational commits
        input("\nPress Enter to create educational commits (90 days)...")
        total_commits = create_educational_commits()
        
        # Step 3: Verify
        input("\nPress Enter to verify commits...")
        verify_commits()
        
        # Final instructions
        print("\n" + "=" * 60)
        print("EDUCATIONAL DEMONSTRATION COMPLETE!")
        print("=" * 60)
        print(f"Total educational commits created: {total_commits}")
        print("\nNext steps for learning:")
        print("1. Run 'git log --oneline' to see all commits")
        print("2. Run 'git log --graph --oneline' to see visual history")
        print("3. Check dates with 'git log --pretty=fuller'")
        print("4. Study the DISCLAIMER.md file for important notes")
        print("\nRemember: This is for learning git internals only!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if _name_ == "_main_":
    main()