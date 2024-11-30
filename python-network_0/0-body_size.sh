#!/bin/bash
# Bash script to get the size of the body of the response from a URL

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"

# Use curl to send a request and display the size of the response body
curl -s "$URL" -o /dev/null -w "%{size_download}\n"
