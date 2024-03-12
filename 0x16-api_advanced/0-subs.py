#!/usr/bin/python3
"""module for Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """return numbers of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-agent': 'Google Chrome Version 81.04044.129'}
    res = requests.get(
            url,
            headers=header,
            allow_redirects=False
            )
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    try:
        return res.json().get("data").get("subscribers")
    except Exception:
        return 0
