#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve in challenge
"""

import requests
import sys


if __name__ == "__main__":
    try:
        repot_name = sys.argv[1]
        username = sys.argv[2]
        commmits_url = "https://api.github.com/repos/{}/{}/commits" \
            .format(username, repot_name)
        response = requests.get(commmits_url)
        json_obj = response.json()
        for k, objt in enumerate(json_objt):
            if k == 10:
                break
            if type(objt) is dict:
                name = objt.get('commit').get('author').get('name')
                print("{}: {}".format(objt.get('sha'), name))
    except ValueError as invalid_json:
        pass
