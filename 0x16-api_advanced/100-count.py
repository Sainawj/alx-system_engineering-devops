#!/usr/bin/python3
"""Module for counting word occurrences in subreddit hot posts"""


def count_words(subreddit, word_list, word_count={}, after=None):
	"""Fetches and counts occurrences of specified words in the titles of all hot posts from a subreddit.
 
	Args:
		subreddit (str): The name of the subreddit.
		word_list (list): A list of words to count in post titles.
		word_count (dict): Dictionary for accumulating word counts (used in recursion).
		after (str): The ID of the last post fetched for pagination (used in recursion).

	Returns:
		None: Prints word counts for non-zero occurrences.
	"""
	import requests

	# Construct the URL to fetch hot posts with pagination
	url = f"https://www.reddit.com/r/{subreddit}/hot.json"

	# Make a request to the Reddit API with custom User-Agent and pagination parameter
	response = requests.get(url, 
							params={"after": after}, 
							headers={"User-Agent": "My-User-Agent"}, 
							allow_redirects=False)

	# Check if the request was successful
	if response.status_code != 200:
		return None

	# Parse the JSON response to extract post titles
	info = response.json()
	hot_posts = [child.get("data", {}).get("title", "") 
				for child in info.get("data", {}).get("children", [])]

	# If no posts are found, return None
	if not hot_posts:
		return None

	# Remove duplicate words from word_list
	word_list = list(dict.fromkeys(word_list))

	# Initialize word_count dictionary if it's empty
	if not word_count:
		word_count = {word: 0 for word in word_list}

	# Count occurrences of each word in post titles
	for title in hot_posts:
		split_words = title.split(' ')
		for word in word_list:
		for s_word in split_words:
				if s_word.lower() == word.lower():
					word_count[word] += 1

	# If there are no more posts to fetch, print the sorted word counts
	if not info.get("data", {}).get("after"):
		sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
		sorted_counts = sorted(sorted_counts, key=lambda kv: kv[1], reverse=True)
		for k, v in sorted_counts:
			if v != 0:
				print(f'{k}: {v}')
	else:
		# Recursively fetch more posts
		return count_words(subreddit, word_list, word_count, info.get("data", {}).get("after"))
