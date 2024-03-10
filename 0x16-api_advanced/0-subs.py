#!/usr/bin/python3
"""
module for Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    return numbers of subscribers
    """
    r = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        url, headers={"User-Agent": "MyCustomUserAgent"},
        allow_redirects=False
        )
    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0
