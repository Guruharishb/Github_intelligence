from github_services import get_User,get_Repositories
from dotenv import load_dotenv
import os
load_dotenv()

username="Guruharishb"

token=os.getenv("GITHUB_TOKEN")
user=get_User(username,token)


if(user):
    print("Username:",user["login"])
    print("Public repositories:",user["public_repos"])
    print("Followers:",user["followers"])
    print()
repositories=get_Repositories(username,token)
if(repositories):
    print("repositories")
    for repo in repositories:
        print(repo["name"])