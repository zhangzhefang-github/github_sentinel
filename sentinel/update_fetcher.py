import requests

class UpdateFetcher:
    def __init__(self, config):
        self.api_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {config['github_token']}"
        }

    def fetch_updates(self, repos):
        updates = {}
        for repo in repos:
            url = f"{self.api_url}/repos/{repo}/commits"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                updates[repo] = response.json()
            else:
                updates[repo] = []
        return updates
