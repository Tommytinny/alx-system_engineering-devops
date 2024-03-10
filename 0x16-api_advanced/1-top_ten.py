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
    header = {'User-Agent': 'MyCustomUserAgent/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        data = r.json()
        for value in data['data']['children']:
            subred_title = value['data']['title']
            print(subred_title)
    else:
        print("None")
