#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
gathers data from API and exports it to CSV file
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
            user_response = requests.get('{}/users/{}'.format(API_ENDPOINT, employee_id)).json()
            todos_response = requests.get('{}/todos'.format(API_ENDPOINT)).json()
            employee_username = user_response.get('username')
            todos_list = list(filter(lambda x: x.get('userId') == employee_id, todos_response))
            with open('{}.csv'.format(employee_id), 'w') as file:
                for todo in todos_list:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            employee_id,
                            employee_username,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
