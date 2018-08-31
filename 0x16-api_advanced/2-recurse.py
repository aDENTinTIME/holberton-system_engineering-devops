#!/usr/bin/python3
"""
    Returns the titles of every hot post in a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], aft=None):
    """
        Takes two arguments, `subreddit` and `hot_list`
        recursivly adds the title of every hot post in a subreddit
        if it exists, or None if it doesn't or otherwise failed.
    """

    head = {
        'User-Agent': 'Totally human'
    }

    response = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'
                            .format(subreddit, aft), headers=head)

    if (not response.status_code == 200 or
       not response.json().get('data').get('children')):
        return None

    aft = response.json().get('data').get('after')
    hot_list += [x.get('data').get('title') for x in
                 [y for y in response.json().get('data').get('children')]]
    if aft:
        return recurse(subreddit, hot_list, aft)
    else:
        return hot_list
