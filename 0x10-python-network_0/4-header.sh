#!/bin/bash
# Script that take a URL as an argument, send a GET request to the URL, and display the body of response
curl -s "$1" -H "X-School-User-Id: 98"
