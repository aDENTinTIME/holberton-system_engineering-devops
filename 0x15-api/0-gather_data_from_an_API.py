#!/usr/bin/python3
"""
    Grabs info about an employee's accomplishments
"""


from sys import argv
import requests


employee_id = argv[1]

r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                 .format(employee_id))

EMPLOYEE_NAME = r.json().get('name')

r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                 .format(employee_id))

NUMBER_OF_DONE_TASKS = [x.get('completed') for x in r.json()].count(True)

TOTAL_NUMBER_OF_TASKS = len(r.json())

print('Employee {EMPLOYEE_NAME} is done with '
      'tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):'
      .format(EMPLOYEE_NAME=EMPLOYEE_NAME,
              NUMBER_OF_DONE_TASKS=NUMBER_OF_DONE_TASKS,
              TOTAL_NUMBER_OF_TASKS=TOTAL_NUMBER_OF_TASKS))

for x in r.json():
    if x.get('completed') is True:
        print('\t ' + x.get('title'))
