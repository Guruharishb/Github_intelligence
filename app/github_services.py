import requests
import os
from dotenv import load_dotenv
load_dotenv()
token=os.getenv("GITHUB_TOKEN")
headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
def get_user(username):
    url=f"https://api.github.com/users/{username}"

    try:
        response=requests.get(url,
                              headers=headers,
                              timeout=10,
                              )
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def get_repositories(username,page=1,per_page=10):
    url=f"https://api.github.com/users/{username}/repos"
    params={
        "page":page,
        "per_page":10,
        "sort":"updated"
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
def get_all_repositories(username):
    repo=[]
    page=1
    while True:
        curr=get_repositories(username,page)
        if not curr:
            break
        repo.extend(curr)
        page+=1
    return repo
def get_repository(username,repo):
    url=f"https://api.github.com/repos/{username}/{repo}"

    try:
        response=requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None
def get_repository_languages(username,repo):
    url=f"https://api.github.com/repos/{username}/{repo}/languages"

    try:
        response=requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return {}

def get_rate_limit():
    url="https://api.github.com/rate_limit"
    try:
        response=requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None