#!/bin/bash
# a Bash script that takes in a URL
curl -sIX OPTIONS "$1" | grep Allow | sed 's/Allow: //'
