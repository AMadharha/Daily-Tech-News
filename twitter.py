# IMPORTS
import tweepy
import os

# TWITTER KEYS
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

class TwitterWrapper:
    def __init__(self):
        """
        Initialize the Twitter instance with a Tweepy Client and API object.

        The constructor sets up a Tweepy Client using the Bearer Token, API Key,
        API Key Secret, Access Token, and Access Token Secret for authentication,
        which are imported from the config module. It also sets up a Tweepy API 
        object using OAuth1UserHandler for user-based authentication.
        """
        self.client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def tweet(self, content: str):
        """
        Send a tweet with the given content.

        Args:
            content (str): The text content of the tweet. The content should be
                           280 characters or fewer, as per Twitter's character limit.
        """
        self.client.create_tweet(text=content)

    def reply_to_recent(self, content: str):
        """
        Reply to the most recent tweet from the authenticated user's timeline
        with the given content.

        Args:
            content (str): The content to include in the reply message.
        """
        tweets = self.api.user_timeline(screen_name='DailyTechnoNews', count=1)
        tweet = tweets[0]
        self.api.update_status(content, in_reply_to_status_id=tweet.id)