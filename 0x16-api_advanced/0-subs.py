#!/usr/bin/python3
"""Prototype: def number_of_subscribers
(subreddit)"""
import requests


def number_of_subscribers(subreddit):
    """ensure you’re setting a custom User-Agent."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    req = requests.get(url, headers=headers).json()
    subscriber = req.get('data', {}).get('subscribers')
    if not subscriber:
        return 0
    return subscriber
