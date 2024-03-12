#!/usr/bin/python3
"""module for Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """return numbers of subscribers"""
    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "My-User-Agent"}
    res = requests.get(
            url,
            headers=header,
            allow_redirects=False
            )
    if subreddit is None or not instance(subreddit, str):
        return 0

    try:
        return res.json().get("data").get("subscribers")
    except Exception as e:
        return 0
