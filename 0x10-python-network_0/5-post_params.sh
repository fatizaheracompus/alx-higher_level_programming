#!/bin/bash
# Script that take in a URL, send a POST request to the passed URL, and display the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
