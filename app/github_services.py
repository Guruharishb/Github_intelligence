import requests

def get_User(username,token):
    url=f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    try:
        response=requests.get(url,
                              headers=headers,
                              timeout=10,
                              )
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def get_Repositories(username,token):
    url=f"https://api.github.com/users/{username}/repos"
    params={
        "per_page":10,
        "sort":"updated"
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    try:
        response=requests.get(url,
                              headers=headers,
                              timeout=10,
                              params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return []
    