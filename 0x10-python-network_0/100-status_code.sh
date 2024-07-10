#!/bin/bash
# script
curl -s -o /dev/null --write-out "%{http_code}" "$1"
