#!/usr/bin/python3
"""
module for Reddit API
"""


from requests import get


def number_of_subscribers(subreddit):
    """
    return numbers of subscribers
    """

    user_agent = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) \
        Gecko/20100101 Firefox/123.0'
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    results = get(
        url,
        headers=user_agent,
        allow_redirects=False
    )

    if results.status_code == 200:
        return results.json()['data']['subscribers']
    return 0
