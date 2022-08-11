import tweepy
import praw
import config

# Twitter Authentication
auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET) 

# Reddit Authentication
reddit = praw.Reddit(client_id = "lzGC0n5GmClEoK_gdSitAA",
                     client_secret = config.CLIENT_SECRET,
                     username = "DailyTechNewsTweet",
                     password = config.PASSWORD,
                     user_agent = "DailyTechNews")

# Tweet Code
api = tweepy.API(auth, wait_on_rate_limit=True)
subreddit = reddit.subreddit("technews+apple+technology")
top = subreddit.top(time_filter = "day", limit = 1)
for post in top:
    api.update_status("#DTN\n[" + post.title + "]\n" + post.url)