#!/usr/bin/python3
"""module for Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """return numbers of subscribers"""
    try:
        r = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            allow_redirects=False
            )
        if r.status_code >= 300:
            return 0
        else:
            return r.json().get("data").get("subscribers")
    except requests.exceptions.RequestException as e:
        return 0
