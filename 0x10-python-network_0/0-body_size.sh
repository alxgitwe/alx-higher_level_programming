#!/bin/bash
# script
curl -i $1 | grep Content-Length | tail -c 4
