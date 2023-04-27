#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# -w option specifies the format of the output and returns the size of the response body in bytes
# -s option tells curl to operate in silent mode

url="$1"
curl -s "$url" | wc -c
