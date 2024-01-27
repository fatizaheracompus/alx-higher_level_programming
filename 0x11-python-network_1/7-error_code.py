#!/usr/bin/python3
"""
script that take in a URL, send a request to the URL and display the
body of the response (decod in utf-8).

"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    bd = response.text
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(bd)
