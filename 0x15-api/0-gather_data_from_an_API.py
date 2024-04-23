#!/usr/bin/python3
"""
This script, using this REST API, to give employee ID,
returns the information for a progress list.
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # employee information ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filter to count the employee
    completed = [task.get("title") for task in todos if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print all completed tasks sequentially
    [print("\t{}".format(complete)) for complete in completed]
