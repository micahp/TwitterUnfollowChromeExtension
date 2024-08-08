import tweepy
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def unfollow_all():
    try:
        # Get the authenticated user's ID
        user_id = api.verify_credentials().id

        # Get the list of users the authenticated user is following
        friends = api.get_friend_ids(user_id=user_id)
        print(f"Found {len(friends)} users to unfollow.")

        for friend_id in friends:
            try:
                api.destroy_friendship(user_id=friend_id)
                print(f"Unfollowed user ID {friend_id}")
                time.sleep(1)  # To avoid hitting rate limits
            except tweepy.TweepError as e:
                print(f"Failed to unfollow user ID {friend_id}: {e}")
                continue

        print("Unfollowed all users.")
    except tweepy.TweepError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    unfollow_all()