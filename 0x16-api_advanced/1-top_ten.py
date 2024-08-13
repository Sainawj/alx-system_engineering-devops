#!/usr/bin/python3
"""
This module contains the function top_ten
"""

import requests
from sys import argv


def top_ten(subreddit):
    """
    Returns the top ten posts for a given subreddit.
    """
    # Define the user-agent header
    user = {'User-Agent': 'Google'}

    # Construct the URL to fetch top 10 hot posts from Reddit API
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    try:
        # Send the GET request to Reddit API
        response = requests.get(url, headers=user)

        # Check if the request was successful
        if response.status_code != 200:
            print(None)
            return

        # Parse the JSON response
        data = response.json()

        # Extract and print titles of the top 10 hot posts
        posts = data.get('data', {}).get('children', [])
        if posts:
            for post in posts:
                print(post.get('data', {}).get('title', 'No Title'))
        else:
            print(None)

    except requests.RequestException:
        # Handle any request-related exceptions
        print(None)
    except ValueError:
        # Handle JSON decoding errors
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: ./1-top_ten.py <subreddit>")
