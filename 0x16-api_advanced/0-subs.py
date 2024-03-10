#!/usr/bin/python3
"""
function that queries the Reddit API and
returns the number of subscribers (not active users,
total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """
    return numbers of subscribers
    """
    header = {'User-Agent': 'MyCustomUserAgent/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        data = r.json()
        num_subreddits = data['data']['subscribers']
        return num_subreddits
    else:
        return 0
