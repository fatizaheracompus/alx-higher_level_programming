#!/bin/bash 
# Script that sends a request to  URL passed as an argument, and display only the status code of the response.
curl -s -L -X HEAD -w "%{http_code}" "$1"
