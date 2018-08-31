#!/usr/bin/python3
"""
    Returns number of subscribers to a subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """
        Takes one argument, `subreddit`
        and returns the number of subscribers to it
        if it exists, or 0 if it doesn't or otherwise failed.
    """
    head = {
        'User-Agent': 'Totally human'
    }
    response = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit), headers=head)
    if response.status_code == 200:
        return response.json()['data'].get('subscribers')
    else:
        return 0
