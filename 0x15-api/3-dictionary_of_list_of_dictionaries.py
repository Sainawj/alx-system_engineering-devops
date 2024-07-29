#!/usr/bin/python3
"""Exports data in the JSON format for all employees."""

import json
import requests


def get_users():
    """Fetch all users."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_todos():
    """Fetch all TODO items."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def write_todos_to_json(users, todos):
    """Write TODO items to a JSON file for all users."""
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todos if task['userId'] == user_id
        ]
        all_tasks[str(user_id)] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as f:
        json.dump(all_tasks, f)


def main():
    users = get_users()
    todos = get_todos()
    write_todos_to_json(users, todos)


if __name__ == "__main__":
    main()
