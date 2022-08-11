import tweepy
import authentication
from bs4 import BeautifulSoup

# Twitter Authentication
auth = authentication.authTwitter()
api = tweepy.API(auth, wait_on_rate_limit=True)

# Reddit Authentication
reddit = authentication.authReddit()

# Tweet Code
subreddit = reddit.subreddit("technews+apple+technology")
top = subreddit.top(time_filter = "day", limit = 1)
for post in top:
    api.update_status("#DTN\n[" + post.title + "]\n" + post.url)