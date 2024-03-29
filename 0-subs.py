#!/usr/bin/python3
<<<<<<< HEAD
'''
Defines function that queries the Reddit API and returns the
number of subscribers
'''
import requests
import sys


def number_of_subscribers(subreddit):
    '''Queries the Reddit API and returns the
    number of subscribers
    Return:
        0 - if invalid subreddit is given
    '''
    if subreddit is None or not isinstance(subreddit, str):
        return(0)
    endpoint = 'https://www.reddit.com'
    headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    info = requests.get('{}/r/{}/about.json'.format(
            endpoint,
            subreddit), headers=headers, allow_redirects=False)
    if info.status_code == 200:
        json_info = info.json()
        return(json_info.get('data').get('subscribers'))
    else:
        return(0)
=======
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
>>>>>>> f919471098e16c7da239b8dad8e588afbb5288ba
