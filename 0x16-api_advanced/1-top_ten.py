#!/usr/bin/python3
"""
    Prints the titles of the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """
        Takes one argument, `subreddit`
        and prints the first 10 hot posts
        if it exists, or None if it doesn't or otherwise failed.
    """

    head = {
        'User-Agent': 'Totally human'
    }

    response = requests.get('https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit), headers=head)

    if (response.status_code == 200 and
       response.json().get('data').get('children')):
        for i, story in enumerate(response.json().get('data').get('children')):
            if i == 10:
                break
            print(story.get('data').get('title'))
    else:
        print('None')
