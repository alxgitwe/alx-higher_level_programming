#!/bin/bash
# script
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
