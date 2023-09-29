#!/bin/bash
# a Bash script that takes in a URL as an argument,
# sends a GET request to the URL, and displays the body of the response
if [ $# -lt 1 ]; then
	exit
fi
curl -sH "X-School-User-Id: 98" "$1"

