#!/usr/bin/python3
"""module for Reddit API"""


def number_of_subscribers(subreddit):
    """return numbers of subscribers"""
    import requests


    r = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        url, headers={"User-Agent": "MyCustomUserAgent"},
        allow_redirects=False
        )
    if r.status_code >= 300:
        return 0
    else:
        return r.json().get("data").get("subscribers")