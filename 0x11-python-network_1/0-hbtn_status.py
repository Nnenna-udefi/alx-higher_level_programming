#!/usr/bin/python3
"""script that fetches a url"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
