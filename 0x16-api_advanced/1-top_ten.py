#!/usr/bin/python3
""" Module queries the Reddit API and prints the
    titles of the first 10 hot posts
"""

def top_ten(subreddit):
    """ Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    
    # Import the requests library to handle HTTP requests
    import requests

    # Send a GET request to Reddit's API to fetch the top 10
    # hot posts from the specified subreddit
    sub_info = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},  # Set a custom User-Agent
        allow_redirects=False  # Prevent automatic redirection of the request
    )

    # Check if the request resulted in a redirect or error (status code >= 300)
    if sub_info.status_code >= 300:
        print('None')  # Print 'None' if there's an error or redirect
    else:
        # Parse the JSON response and print the titles of the top 10 hot posts
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]
