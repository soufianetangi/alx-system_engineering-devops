import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)  # Print the raw response text for debugging
    
    if response.status_code != 200:
        return 0
    
    try:
        data = response.json().get("data", {})
    except ValueError:
        return 0  # Return 0 if JSON decoding fails
    
    return data.get("subscribers", 0)

