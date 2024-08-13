#!/usr/bin/python3
"""Module for retrieving subreddit subscriber count"""

import requests

def number_of_subscribers(subreddit):
    """Fetches the number of subscribers for a given subreddit from Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit
        is invalid or an error occurs.
    """
    # Construct the URL to access subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Make a request to the Reddit API with a custom User-Agent to avoid rate limiting
    response = requests.get(url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False)
    
    # Check if the request was redirected or resulted in an error
    if response.status_code >= 300:
        return 0

    # Parse the JSON response and return the number of subscribers
    return response.json().get("data", {}).get("subscribers", 0)
