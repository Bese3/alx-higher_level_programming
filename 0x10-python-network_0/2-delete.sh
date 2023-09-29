#!/bin/bash
# a Bash script that sends a DELETE request to the URL passed
# as the first argument and displays the body of the response
if [ $# -lt 1 ]; then
	exit
fi
curl -X DELETE $1
