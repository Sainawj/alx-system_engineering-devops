#!/usr/bin/python3
"""For a given employee ID, returns information about their
TODO list progress."""

import requests
import sys


def get_user(user_id):
    """Fetch user information by user ID."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_todos():
    """Fetch all TODO items."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def calculate_todo_progress(user_id, todos):
    """Calculate the total and completed tasks for a given user ID."""
    total_tasks = 0
    completed_tasks = 0
    completed_titles = []

    for task in todos:
        if task['userId'] == user_id:
            total_tasks += 1
            if task['completed']:
                completed_tasks += 1
                completed_titles.append(task['title'])

    return total_tasks, completed_tasks, completed_titles


def main():
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    user = get_user(user_id)
    todos = get_todos()

    (total_tasks, completed_tasks,
     completed_titles) = calculate_todo_progress(user_id, todos)

    print(f"Employee {user['name']} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")
    print("\n".join(f"\t {title}" for title in completed_titles))


if __name__ == "__main__":
    main()
