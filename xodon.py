import tweepy
import requests
import json
import time
from datetime import datetime

# --- X API Setup ---
X_API_KEY = "your-api-key"
X_API_SECRET = "your-api-secret"
X_ACCESS_TOKEN = "your-access-token"
X_ACCESS_SECRET = "your-access-token-secret"

auth = tweepy.OAuthHandler(X_API_KEY, X_API_SECRET)
auth.set_access_token(X_ACCESS_TOKEN, X_ACCESS_SECRET)
x_api = tweepy.API(auth, wait_on_rate_limit=True)

# --- Mastodon API Setup ---
MASTODON_INSTANCE = "https://mastodon.social"  # Your instance URL
MASTODON_TOKEN = "your-mastodon-access-token"

mastodon_headers = {
    "Authorization": f"Bearer {MASTODON_TOKEN}"
}

last_tweet_id = None  # To track the latest tweeted post

def get_latest_tweet(username):
    """Fetch the most recent tweet from the user."""
    global last_tweet_id
    try:
        tweets = x_api.user_timeline(screen_name=username, count=1, tweet_mode="extended")
        if tweets:
            tweet = tweets[0]
            if last_tweet_id != tweet.id:  # Check if it's a new tweet
                last_tweet_id = tweet.id
                return tweet.full_text
        return None
    except tweepy.TweepyException as e:
        print(f"Error fetching latest tweet: {e}")
        return None

def post_to_mastodon(content):
    """Post content to Mastodon."""
    url = f"{MASTODON_INSTANCE}/api/v1/statuses"
    payload = {"status": content}
    try:
        response = requests.post(url, headers=mastodon_headers, data=payload)
        response.raise_for_status()
        print(f"Posted to Mastodon: {content[:50]}...")
    except requests.RequestException as e:
        print(f"Error posting to Mastodon: {e}")

def get_x_following(username):
    """Fetch users you follow on X."""
    following = []
    try:
        for user in tweepy.Cursor(x_api.get_friends, screen_name=username).items():
            following.append({
                "username": user.screen_name,
                "display_name": user.name
            })
        return following
    except tweepy.TweepyException as e:
        print(f"Error fetching X following: {e}")
        return []

def search_mastodon_user(username):
    """Search for a user on Mastodon."""
    url = f"{MASTODON_INSTANCE}/api/v2/search"
    params = {"q": username, "limit": 5}
    try:
        response = requests.get(url, headers=mastodon_headers, params=params)
        response.raise_for_status()
        data = response.json()
        accounts = data.get("accounts", [])
        if accounts:
            return accounts[0]["id"], accounts[0]["acct"]  # Return user ID and handle
        return None, None
    except requests.RequestException as e:
        print(f"Error searching Mastodon for {username}: {e}")
        return None, None

def follow_mastodon_user(user_id):
    """Follow a user on Mastodon by their ID."""
    url = f"{MASTODON_INSTANCE}/api/v1/accounts/{user_id}/follow"
    try:
        response = requests.post(url, headers=mastodon_headers)
        response.raise_for_status()
        print(f"Successfully followed user ID {user_id}")
    except requests.RequestException as e:
        print(f"Error following user ID {user_id}: {e}")

def sync_following(x_username):
    """Sync X following to Mastodon."""
    print(f"Syncing following list for {x_username}...")
    x_following = get_x_following(x_username)
    print(f"Found {len(x_following)} users on X.")

    for user in x_following:
        user_id, mastodon_handle = search_mastodon_user(user["username"])
        if user_id:
            follow_mastodon_user(user_id)
            print(f"Followed {user['username']} on Mastodon as {mastodon_handle}")
        else:
            print(f"Could not find {user['username']} on Mastodon")
        time.sleep(1)  # Avoid rate limits


def xodon_tools_app(x_username, poll_interval=60):
    """Main function for Xodon Tools app."""
    print("Xodon Tools - A bridging utility for seamless transmission between X and Mastodon")
    print(f"Starting app for {x_username}...")

    # Initial sync of following list
    sync_following(x_username)

    # Continuous monitoring for new tweets
    print(f"Monitoring X posts every {poll_interval} seconds...")
    while True:
        new_tweet = get_latest_tweet(x_username)
        if new_tweet:
            print(f"New tweet detected: {new_tweet[:50]}...")
            post_to_mastodon(new_tweet)
        else:
            print(f"No new tweets at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(poll_interval)  # Wait before checking again

if __name__ == "__main__":
    x_username = input("Enter your X username (without @): ")
    poll_interval = int(input("Enter polling interval in seconds (e.g., 60): "))
    xodon_tools_app(x_username, poll_interval)
    
