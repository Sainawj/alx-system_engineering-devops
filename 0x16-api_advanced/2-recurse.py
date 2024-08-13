#!/usr/bin/python3
"""Module for recursively retrieving all hot posts from a subreddit"""


def recurse(subreddit, hot_list=[], count=0, after=None):
	"""Recursively fetches all hot posts from a given subreddit.

	Args:
		subreddit (str): The name of the subreddit.
		hot_list (list): Accumulator for storing titles of hot posts (used in recursion).
		count (int): The number of posts fetched so far (used in recursion).
		after (str): The ID of the last post fetched to continue fetching from where we left off (used in recursion).
    
	Returns:
		list: A list of titles of all hot posts from the subreddit, or None if the subreddit is invalid or an error occurs.
	"""
	import requests

	# Construct the URL to fetch hot posts with pagination parameters
	url = f"https://www.reddit.com/r/{subreddit}/hot.json"

	# Make a request to the Reddit API with custom User-Agent to avoid rate limiting and include pagination parameters
	response = requests.get(url, 
							params={"count": count, "after": after}, 
							headers={"User-Agent": "My-User-Agent"}, 
							allow_redirects=False)
    
	# Check if the request resulted in an error or an invalid subreddit
	if response.status_code >= 400:
		return None

	# Parse the JSON response to get the list of post titles
	hot_list.extend(child.get("data", {}).get("title", "") 
					for child in response.json().get("data", {}).get("children", []))

	# Check if there are more posts to fetch
	info = response.json().get("data", {})
	if not info.get("after"):
		return hot_list

	# Recursively fetch more posts
	return recurse(subreddit, hot_list, info.get("count", 0), info.get("after"))
