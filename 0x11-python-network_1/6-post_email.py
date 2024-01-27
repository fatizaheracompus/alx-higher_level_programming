#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payloade = {
        "email": email
    }
    response = requests.post(url, data=payload)
    print(response.text)
