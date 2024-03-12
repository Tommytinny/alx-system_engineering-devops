#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of the first 10
hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    first 10 hot posts listed for a given subreddit
    """
    header = {"User-Agent": "MyCustomUserAgent/1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    params = {
        "limit": 10
    }
    r = requests.get(url, headers=header, params=params,
                     allow_redirects=False)

    if r.status_code != 404:
        data = r.json().get("data")
        [print(v.get("data").get("title")) for v in data.get("children")]
    else:
        print("None")
        return
