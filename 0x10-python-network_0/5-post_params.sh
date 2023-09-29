#!/bin/bash
# a Bash script that takes in a URL, sends a POST request
# to the passed URL, and displays the body of the response
if [ $# -lt 1 ]; then
	exit
fi
curl -sX POST  -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

