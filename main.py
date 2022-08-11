import tweepy
import authentication
import keywords

# Twitter Authentication
auth = authentication.authTwitter()
api = tweepy.API(auth, wait_on_rate_limit=True)

# Reddit Authentication
reddit = authentication.authReddit()

# Get top reddit post
subreddit = reddit.subreddit("technews+apple+technology")
top = subreddit.top(time_filter = "day", limit = 1)

# Keywords
for post in top:
    article = keywords.get_article(post.url)


# Tweet Code
#for post in top:
    #api.update_status("#DTN\n[" + post.title + "]\n" + post.url)