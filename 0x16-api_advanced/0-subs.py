#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    user_agent = {'User-agent': 'My-User-Agent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent,
                   allow_redirects=False)
    results = response.json()
    
    if response.status_code >= 300:
        return 0
    return results.get('data').get('subscribers')
