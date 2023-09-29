#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
if [ $# -lt 1 ]; then
	exit
fi
curl -sI $1 | grep Content-Length | sed 's/Content-Length: //'

