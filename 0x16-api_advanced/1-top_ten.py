#!/usr/bin/python3
"""Module for retrieving top 10 hot posts from a subreddit"""


def top_ten(subreddit):
	"""Fetches the top 10 hot posts from a given subreddit.
 
	Args:
		subreddit (str): The name of the subreddit.
    
	Prints:
		The titles of the top 10 hot posts from the subreddit. If the subreddit is invalid or an error occurs, prints 'None'.
	"""
	import requests

	# Construct the URL to fetch the top 10 hot posts from the subreddit
	url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

	# Make a request to the Reddit API with a custom User-Agent to avoid rate limiting
	response = requests.get(url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False)
 
	# Check if the request was redirected or resulted in an error
	if response.status_code >= 300:
		print('None')
	else:
		# Parse the JSON response and print the titles of the top 10 hot posts
		posts = response.json().get("data", {}).get("children", [])
		for post in posts:
			print(post.get("data", {}).get("title"))
