#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit,
the function should return None
"""
import requests


def recurse(subreddit, hot_list=None, after=None, count=None):
    """
    returns a list containing the titles of all hot articles
    """
    if hot_list is None:
        hot_list = []

    header = {'User-Agent': 'MyCustomUserAgent/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {'after': None}
    r = requests.get(url, headers=header, params=params)
    if r.status_code == 200:
        data = r.json()
        for value in data['data']['children']:
            subred_title = value['data']['title']
            hot_list.append(subred_title)
        after = data['data']['after']
        if after:
            recurse(subreddit, hot_list, after)
    else:
        return None

    return hot_list
