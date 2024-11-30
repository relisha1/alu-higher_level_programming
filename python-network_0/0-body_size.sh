#!/bin/bash
# 0-body_size.sh - This script takes a URL, sends a request, and displays the size of the body of the response

# Check if a URL argument was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send the request and get the body size
curl -s -o /dev/null -w "%{size_download}" "$1"

