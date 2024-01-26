#!/bin/bash
# Script that send a JSON POST request to a URL passed as the first argument, and display the body of  response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
