import os
import time
import jwt
import requests

APP_ID = int(os.getenv("GITHUB_APP_ID"))
PRIVATE_KEY_PEM = os.getenv("GITHUB_APP_PRIVATE_KEY")
INSTALLATION_ID = int(os.getenv("GITHUB_INSTALLATION_ID"))

def build_app_jwt():
    now = int(time.time())
    payload = {
        "iat": now - 60,
        "exp": now + 540,  # < 10 min
        "iss": APP_ID,
    }
    return jwt.encode(payload, PRIVATE_KEY_PEM, algorithm="RS256")

def get_installation_token():
    jwt_token = build_app_jwt()
    url = f"https://api.github.com/app/installations/{INSTALLATION_ID}/access_tokens"
    r = requests.post(url, headers={
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github.v3+json"
    })
    r.raise_for_status()
    data = r.json()
    return data["token"], data["expires_at"]

def fetch_latest_release(owner="rgullik1", repo="GitHub-App-Integration-playground"):
    token, _ = get_installation_token()
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    r = requests.get(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    })
    if r.status_code == 404:
        return None
    r.raise_for_status()
    data = r.json()
    return {
        "tag": data.get("tag_name"),
        "name": data.get("name"),
        "published_at": data.get("published_at"),
        "assets": [
            {"name": a["name"], "download_url": a["browser_download_url"]}
            for a in data.get("assets", [])
        ]
    }

# Example usage:
if __name__ == "__main__":
    release = fetch_latest_release()
    if release:
        print("Latest release tag:", release["tag"])
    else:
        print("No releases found.")
