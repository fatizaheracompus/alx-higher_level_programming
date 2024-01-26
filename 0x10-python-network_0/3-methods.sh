#!/bin/bash
# Script that take in a URL and display all HTTP method the server will accept
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
