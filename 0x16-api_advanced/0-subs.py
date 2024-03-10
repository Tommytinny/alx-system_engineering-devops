#!/usr/bin/python3
"""module for Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """return numbers of subscribers"""
    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "My-User-Agent"}
    ries = requests.get(
            url,
            headers=header,
            allow_redirects=False
            )
    if res.status_code >= 300:
        return 0
    
    return res.json().get("data").get("subscribers")
