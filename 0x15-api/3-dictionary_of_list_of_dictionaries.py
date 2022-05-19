#!/usr/bin/python3
"""using this REST API,
for a given employee ID,
return list progress"""
import json
import requests

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    user_json = user.json()
    afterdic = {}
    for name in user_json:
        afterdic[name["id"]] = name["username"]
    task = ""
    dicci = {}
    lista = []
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for t in todos.json():
        dictio = {}
        dictio["task"] = t["title"]
        dictio["completed"] = t["completed"]
        dictio["username"] = afterdic[t["userId"]]
        lista.append(dictio)
        dicci[t["userId"]] = lista
    filename = "todo_all_employees.json"
    with open(filename, "w") as outfile:
        json.dump(dicci, outfile)
