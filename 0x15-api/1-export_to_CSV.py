#!/usr/bin/python3
"""
    Grabs info about an employee's accomplishments
    Creates CSV
"""


import csv
import requests
from sys import argv


if __name__ == "__main__":
    USER_ID = argv[1]

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(USER_ID))

    USERNAME = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(USER_ID))

    NUMBER_OF_DONE_TASKS = [x.get('completed') for x in r.json()].count(True)

    TOTAL_NUMBER_OF_TASKS = len(r.json())

    with open(USER_ID + '.csv', mode='w', encoding="UTF8") as fd:
        cw = csv.writer(fd, quoting=csv.QUOTE_ALL)
        for x in r.json():
            cw.writerow([USER_ID,
                         USERNAME,
                         x.get('completed'),
                         x.get('title')])
