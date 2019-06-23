import code
import os

import requests

from dotenv import load_dotenv
from github import Github

load_dotenv()

DEBUG = os.getenv('DEBUG') == 'true'

g = Github(os.getenv('GITHUB_TOKEN'))


def get_python_repos():
    repositories = g.search_repositories(query='language:python')

    if DEBUG:
        code.interact(local=dict(globals(), **locals()))

    for repo in repositories:
        print(repo)

    # TODO: save to an index file

# TODO: fetch each git repo

def main():
    print('Hello world!')
    res = requests.get('https://api.github.com/zen')
    print(res.text)

    get_python_repos()


if __name__ == '__main__':
    main()
