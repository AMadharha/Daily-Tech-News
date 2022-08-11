import tweepy
import authentication

# Twitter Authentication
auth = authentication.authTwitter()

# Reddit Authentication
reddit = authentication.authReddit()

# Tweet Code
api = tweepy.API(auth, wait_on_rate_limit=True)
subreddit = reddit.subreddit("technews+apple+technology")
top = subreddit.top(time_filter = "day", limit = 1)
for post in top:
    api.update_status("#DTN\n[" + post.title + "]\n" + post.url)