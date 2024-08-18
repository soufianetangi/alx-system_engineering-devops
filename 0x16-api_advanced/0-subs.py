#!/usr/bin/python3
"""Module for task 0"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"  # Make sure to use a descriptive User-Agent
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0
        
        # Handle other HTTP errors
        if response.status_code >= 300:
            return 0

        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    
    except requests.exceptions.RequestException:
        # Handle any exception that occurs during the request
        return 0
    except ValueError:
        # Handle JSON decoding errors
        return 0

