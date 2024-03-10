#!/usr/bin/python3
"""
module for Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    return numbers of subscribers
    """
    header = {'User-Agent': 'MyCustomUserAgent/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        return num_subreddits.json().get("data").get("subscribers")
    else:
        return 0
