#!/usr/bin/python3
"""extend your Python script to
export data in the JSON format"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    user = requests.get("https://jsonplaceholder.typicode.com/users/" + argv[1]
                        )
    user_dic = user.json()
    user = user_dic["username"]

    taskarr = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get("userId") == int(argv[1]):
            task = {}
            task["user_id"] = t["userId"]
            task["username"] = user
            task["completed"] = t["completed"]
            task["title"] = t["title"]
            taskarr.append(task)

    try:
        id = "{}.csv".format(argv[1])
        with open(id, "w") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for elem in taskarr:
                lined = [elem["user_id"], elem["username"],
                         elem["completed"], elem["title"]]
                writer.writerow(lined)
    except IOError:
        print("I/O error")
