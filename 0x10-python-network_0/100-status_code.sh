#!/bin/bash
# a Bash script that sends a request to a URL passed as an argument
curl -s -o -I -w "%{http_code}" "$1"
