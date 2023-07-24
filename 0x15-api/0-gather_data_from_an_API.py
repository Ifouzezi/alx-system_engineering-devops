#!/usr/bin/python3
"""
Retrieve information about employee's TODO progress
from https://jsonplaceholder.typicode.com
Implemented using recursion
"""
import re
import requests
import sys


API_ENDPOINT = "https://jsonplaceholder.typicode.com"
"""REST API URL"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            user_response = requests.get(
                '{}/users/{}'.format(API_ENDPOINT, employee_id)).json()
            todos_response = requests.get(
                '{}/todos'.format(API_ENDPOINT)).json()
            employee_name = user_response.get('name')
            todos = list(filter
                         (lambda x: x.get('userId') == employee_id, todos_response))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    employee_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
