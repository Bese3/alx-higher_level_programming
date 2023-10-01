#!/bin/bash
# a Bash script that sends a request to a URL passed as an argument
curl -sI "$1" | head -n 1 | grep -v [a-z] | tr -d '[A-Z]' | sed 's-/[0-9].[0-9] --' | tr -d '\n'
