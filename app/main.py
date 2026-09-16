from github_services import get_User,get_Repositories
from dotenv import load_dotenv
import os
load_dotenv()

username="Guruharishb"
user=get_User(username)



if(user):
    print("Username:",user["login"])
    print("Public repositories:",user["public_repos"])
    print("Followers:",user["followers"])
    print()
repositories=get_Repositories(username)
if( repositories!=[]):
    print("repositories")
for repo in repositories:
    print(repo["name"])