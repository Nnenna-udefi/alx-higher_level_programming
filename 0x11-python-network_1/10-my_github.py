#!/usr/bin/python3
"""
    script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
    if r.status_code == 200:
        res_json = r.json()
        print(res_json.get("id"))
