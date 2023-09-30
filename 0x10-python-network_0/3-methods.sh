#1/bin/bash
# a Bash script that takes in a URL
# and displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | grep Allow | sed 's/Allow: //'

