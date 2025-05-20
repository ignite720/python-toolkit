import requests
import json
import time

CONFIG_FILENAME = "starred-repos-saver-config.json"

# 1. Read config
config = {
    'username': '',
    'password': '',
    'output_path': 'starred_repos.json',
}

try:
    with open(CONFIG_FILENAME, "r") as f:
        config = json.load(f)
except FileNotFoundError:
    with open(CONFIG_FILENAME, mode="w", encoding="utf-8", newline="\n") as f:
        json.dump(config, f, indent=4)
    
username = config['username']
password = config['password']
output_path = config['output_path']

api_url = f"https://api.github.com/users/{config['username']}/starred"
headers = {"Accept": "application/vnd.github.v3+json"}

# 2. Fetch all pages of starred repositories
page = 1
starred_repos = []
while True:
    r = requests.get(api_url, auth=(username, password), headers=headers, params={"per_page": 100, "page": page})
    if r.status_code == 200:
        data = r.json()
        if not data:
            break
        
        repo_items = []
        for item in data:
            item_lite = {
                "id": item["id"],
                "full_name": item["full_name"],
                "owner": {
                    "html_url": item["owner"]["html_url"],
                },
                "html_url": item["html_url"],
                "description": item["description"],
                "fork": item["fork"],
                "created_at": item["created_at"],
                "size": item["size"],
                "stargazers_count": item["stargazers_count"],
                "language": item["language"],
                "forks_count": item["forks_count"],
                "license": item["license"]["url"] if item["license"] else None,
            }
            repo_items.append(item_lite)
        starred_repos.extend(repo_items)
        
        print(f"Page: {page}, {len(data)}/{len(repo_items)} items received, total => {len(starred_repos)}")
        time.sleep(0.2)
        page += 1
    else:
        print("API request failed with error code:", r.status_code)
        break

# 3. Save the data to a JSON file
if len(starred_repos) > 0:
    with open(output_path, mode="w", encoding="utf-8", newline="\n") as f:
        json.dump(starred_repos, f, indent=4)

    print(f"The list({page - 1} pages, {len(starred_repos)} items) of all starred repositories have been saved to the file '{output_path}'")
    time.sleep(5.0)