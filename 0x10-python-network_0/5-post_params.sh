#!/bin/bash
# a Bash script that takes in a URL, sends a POST request
curl -sX POST  -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
