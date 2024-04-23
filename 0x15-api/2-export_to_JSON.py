#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import json
import requests
from sys import argv


if __name__ == "__main__":
    # Get the employee ID
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # A dictionary containing user task list information and a list of tasks
    data_to_export = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
