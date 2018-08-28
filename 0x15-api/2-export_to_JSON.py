#!/usr/bin/python3
"""
    Grabs info about an employee's accomplishments
    Creates JSON
"""


import csv
from json import dump
import requests
from sys import argv


if __name__ == "__main__":
    USER_ID = argv[1]

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(USER_ID))

    USERNAME = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(USER_ID))

    master = {}
    master[USER_ID] = [{'task': x.get('title'),
                        'completed': x.get('completed'),
                        'username': USERNAME} for x in r.json()]

    with open(USER_ID + '.json', mode='w', encoding="UTF8") as fd:
        dump(master, fd, sort_keys=True)
