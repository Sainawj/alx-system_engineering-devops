#!/usr/bin/python3
"""Exports data in the CSV format."""

import csv
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


def write_todos_to_csv(user_id, username, todos):
    """Write TODO items to a CSV file for a given user."""
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in todos:
            if task['userId'] == user_id:
                writer.writerow([user_id, username, str(task['completed']),
                                 task['title']])


def main():
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    user = get_user(user_id)
    username = user.get('username')
    todos = get_todos()

    write_todos_to_csv(user_id, username, todos)


if __name__ == "__main__":
    main()
