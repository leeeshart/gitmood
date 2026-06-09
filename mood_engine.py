import datetime
import requests
import os

def get_commit_count(username):
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}
    
    today = datetime.date.today().isoformat()
    url = f"https://api.github.com/search/commits?q=author:{username}+committer-date:{today}"
    headers["Accept"] = "application/vnd.github.cloak-preview"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("total_count", 0)
    return 0

def get_mood(username):
    hour = datetime.datetime.now().hour
    commits = get_commit_count(username)

    if commits >= 3:
        return "grind"
    elif 5 <= hour < 12:
        return "chill"
    elif 12 <= hour < 18:
        return "grind"
    elif 18 <= hour < 22:
        return "chill"
    else:
        return "night"
