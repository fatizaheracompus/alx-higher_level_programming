#!/bin/bash
# Script that send a DELETE request to the URL passed as the first argument and display the body of  response
curl -s "$1" -X DELETE
