#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the specified URL using curl
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the size of the response body in bytes
echo "$response"
