#!/usr/bin/python3
"""
Module for counting occurrences of keywords in subreddit hot posts.
"""

import requests
import re
from sys import argv

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries Reddit API to count occurrences of keywords in hot posts.
    
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count (case-insensitive).
        after (str): The parameter to get the next set of results.
        count_dict (dict): A dictionary to keep track of keyword counts.
    
    Returns:
        None: Prints the results sorted by count and then alphabetically.
    """
    if count_dict is None:
        count_dict = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after", None)
        
        if not posts:
            # Print results if no more posts
            sorted_keywords = sorted(
                count_dict.items(),
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_keywords:
                if count > 0:
                    print(f"{word}: {count}")
            return
        
        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            for word in count_dict.keys():
                count_dict[word] += len(re.findall(r'\b{}\b'.format(re.escape(word)), title))

        count_words(subreddit, word_list, after, count_dict)
        
    except requests.RequestException:
        return

if __name__ == "__main__":
    if len(argv) < 3:
        print(f"Usage: {argv[0]} <subreddit> <list of keywords>")
    else:
        count_words(argv[1], [x.lower() for x in argv[2].split()])
