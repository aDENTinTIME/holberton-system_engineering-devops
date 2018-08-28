#!/usr/bin/python3
"""
    Grabs info about an employee's accomplishments
    Creates JSON of all employees
"""


import csv
from json import dump
import requests


if __name__ == "__main__":
    initial_req = requests.get('https://jsonplaceholder.typicode.com/users')
    max_user = len(initial_req.json()) + 1
    master = {}
    for x in range(1, max_user):
        USER_ID = x

        r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(USER_ID))

        USERNAME = r.json().get('username')

        r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(USER_ID))

        master[USER_ID] = [{'task': x.get('title'),
                            'completed': x.get('completed'),
                            'username': USERNAME} for x in r.json()]

    with open('todo_all_employees.json', mode='w', encoding="UTF8") as fd:
        dump(master, fd, sort_keys=True)
