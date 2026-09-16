from github_services import get_user,get_all_repositories,get_repository,get_repository_languages,get_rate_limit

from dotenv import load_dotenv
import os
load_dotenv()

username="Guruharishb"


user=get_user(username)

if not user:
    print("GitHub user not found")
    exit()

print("\nGitHub Profile")
print("Username:",user["login"])
print("Name:",user["name"])
print("Followers:",user["followers"])
print("Public repositories:",user["public_repos"])
repositories=get_all_repositories(username)

print("\nRepositories")

for index,repository in enumerate(repositories,1):
    print(index,repository["name"])
if repositories:
    selected=repositories[0]
    repository=get_repository(username,selected["name"])
    languages=get_repository_languages(
        username,selected["name"]
    )
    if repository:
        print("\nRepository Details")
        print("Name:", repository["name"])
        print("Description:", repository["description"])
        print("Language:", repository["language"])
        print("Stars:", repository["stargazers_count"])
        print("Forks:", repository["forks_count"])
        print("Open issues:", repository["open_issues_count"])
        print("Default branch:", repository["default_branch"])

    print("Languages:", languages)
rate_limit=get_rate_limit()

if rate_limit:
    print("\nAPI Rate Limit")
    print(rate_limit["rate"])