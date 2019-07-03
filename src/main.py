import code
import json
import subprocess
import os
import time

import requests

from dotenv import load_dotenv
from github import Github

load_dotenv()

DEBUG = os.getenv('DEBUG') == 'true'

g = Github(os.getenv('GITHUB_TOKEN'))

def run_shell_command(*args):
    subprocess.run(args)

def get_python_repos():
    repositories = g.search_repositories(query='language:python')

    if DEBUG:
        code.interact(local=dict(globals(), **locals()))

    for repo in repositories:
        print(repo)
        yield repo

def fetch(repo):
    path = f'/mnt/data/repos/{repo["full_name"]}'
    run_shell_command("git", "clone", "--depth", "1", repo["clone_url"], path)

def clone_repos():
    with open("/mnt/data/urls.json", "r") as f:
        for i, line in enumerate(f):
            repo = json.loads(line)
            print(i, repo)
            fetch(repo)

def fetch_urls():
print('Hello world!')
    res = requests.get('https://api.github.com/zen')
    print(res.text)
    print("fetching urls")
    c = 0
    MAX = 9
    begin = time.time()

    with open("/mnt/data/urls.json", "a") as f:
        for repo in get_python_repos():
            f.write(json.dumps(repo.raw_data))
            f.write("\n")
            c += 1
            if c > MAX:
                break

    delta = time.time() - begin
    print(f'done time: {delta} count: {c}')

def main():
    fetch_urls()
    clone_repos()


if __name__ == '__main__':
    main()
