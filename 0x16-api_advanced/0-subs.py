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
    response = requests.get(
        url,
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )

    # Print the response status and content for debugging
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

    # Check if the request was redirected or resulted in an error
    if response.status_code >= 300:
        return 0

    # Parse the JSON response and return the number of subscribers
    data = response.json().get("data", {})
    print(f"Parsed Data: {data}")
    return data.get("subscribers", 0)

# Example usage
if __name__ == "__main__":
    subreddit = "programming"  # Replace with the desired subreddit
    print(f"Subscribers in '{subreddit}': {number_of_subscribers(subreddit)}")
