import os
import subprocess
from datetime import datetime, timedelta

# Repository details
repo_name = "py"  # Change this to your desired repo name
repo_path = os.path.join(os.getcwd(), repo_name)

# Number of commits per day (for a full green graph, make more commits per day)
commits_per_day = 2

# Create and initialize a Git repository
def initialize_repo():
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)
        subprocess.run(["git", "init"], cwd=repo_path)
    else:
        print("Repository already exists")

# Make commits for the past year
def make_commits():
    today = datetime.now()
    one_year_ago = today - timedelta(days=365)

    # Loop through each day for the past year
    for single_date in (one_year_ago + timedelta(n) for n in range(365)):
        for _ in range(commits_per_day):
            # Create a file with a unique name to avoid overwriting
            filename = f"commit_{single_date.strftime('%Y%m%d_%H%M%S')}.txt"
            filepath = os.path.join(repo_path, filename)
            
            # Write something into the file
            with open(filepath, 'w') as file:
                file.write(f"Commit for {single_date.strftime('%Y-%m-%d')}\n")

            # Stage the file
            subprocess.run(["git", "add", "."], cwd=repo_path)

            # Commit the file with the correct date
            commit_message = f"Commit on {single_date.strftime('%Y-%m-%d')}"
            commit_date = single_date.strftime('%Y-%m-%d %H:%M:%S')
            env = os.environ.copy()
            env['GIT_AUTHOR_DATE'] = commit_date
            env['GIT_COMMITTER_DATE'] = commit_date
            subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path, env=env)

# Push to GitHub
def push_to_github():
    # Ensure you've already created the repository on GitHub and set the correct remote URL
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/YOUR_USERNAME/github-full-green.git"], cwd=repo_path)
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_path)
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path)

if __name__ == "__main__":
    initialize_repo()
    make_commits()
    push_to_github()
