#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response
if [ $# -lt 1 ]; then
	exit
fi
curl -sL $1
