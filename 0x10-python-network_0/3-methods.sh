#!/bin/bash

# Check if a URL was provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to get the allowed HTTP methods for the given URL
curl -sI "$1" | grep -i '^Allow:' | sed 's/Allow: //'
