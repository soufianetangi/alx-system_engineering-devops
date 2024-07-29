#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
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

    # Correct formatting for the first line
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}"
          f"/{total_tasks}):")

    # Ensure all tasks are displayed and formatted correctly
    for task in completed_tasks:
        print(f"\t {task}")

