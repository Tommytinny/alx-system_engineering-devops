#!/usr/bin/python3
"""module for Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """return numbers of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "My-User-Agent"}
    r = requests.get(
            url,
            headers=header,
            allow_redirects=False
            )
    if r.status_code >= 300:
        return 0
    
    return r.json().get("data").get("subscribers")
