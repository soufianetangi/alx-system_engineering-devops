#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/yourusername)"
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if subreddit exists
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        
        # If status code is 404 or any other error, return 0
        return 0
    except requests.RequestException:
        # If there's an exception during the request, return 0
        return 0
