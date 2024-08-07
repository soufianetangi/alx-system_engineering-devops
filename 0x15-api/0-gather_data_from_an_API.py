#!/usr/bin/python3
"""
This script retrieves and displays the to-do list information for a given
employee ID using data from the JSONPlaceholder API.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(f"{url}users/{user_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]

    # Correcting the line length and whitespace issues
    print(f"Employee {employee_name} is done with tasks("
          f"{len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task}")

