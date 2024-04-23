#!/usr/bin/python3
"""Python script that, using this REST API, to give employee ID, exports their TODO list progress to a CSV file"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # get the user information from API and then response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write each item's details (user ID, username, completion status,
    #   and title) as row in the CSV file.
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, task.get("completed"), task.get("title")]
         ) for task in todos]
