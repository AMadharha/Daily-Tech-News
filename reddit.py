# IMPORTS
import praw
import os

# REDDIT KEYS
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

class RedditWrapper:
    def __init__(self):
        """
        Initialize the RedditWrapper instance with a PRAW Reddit object.

        The constructor sets up a PRAW Reddit object using the provided
        API credentials (client ID, client secret, user agent, username,
        and password), which are imported from the config module.
        """
        self.reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT,
            username=USERNAME,
            password=PASSWORD,
        )

    def get_top_post_title(self, time: str, subreddit: str) -> str:
        """
        Get the title of the top post for the specified time period in the given subreddit.

        Args:
            time (str): The time period for which the top post should be retrieved.
                        Valid values are 'hour', 'day', 'week', 'month', 'year', and 'all'.
            subreddit (str): The name of the subreddit to fetch the top post from.

        Returns:
            str: The title of the top post for the specified time period in the given subreddit.
        """
        subreddit = self.reddit.subreddit(subreddit)
        top_post = subreddit.top(time_filter=time, limit=1)
        
        for submission in top_post:
            title = submission.title
        
        return title
    
    def get_top_post_url(self, time: str, subreddit: str) -> str:
        """
        Get the URL of the top post for the specified time period in the given subreddit.

        Args:
            time (str): The time period for which the top post should be retrieved.
                        Valid values are 'hour', 'day', 'week', 'month', 'year', and 'all'.
            subreddit (str): The name of the subreddit to fetch the top post from.

        Returns:
            str: The URL of the top post for the specified time period in the given subreddit.
        """
        subreddit = self.reddit.subreddit(subreddit)
        top_post = subreddit.top(time_filter=time, limit=1)

        for submission in top_post:
            url = submission.url

        return url