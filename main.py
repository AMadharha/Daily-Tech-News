import tweepy
import praw

allKeys = open("keys", "r").read().splitlines()

# Twitter Authentication
API_KEY = allKeys[0].strip()
API_KEY_SECRET = allKeys[1].strip()
ACCESS_TOKEN = allKeys[2].strip()
ACCESS_TOKEN_SECRET = allKeys[3].strip()

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) 

api = tweepy.API(auth, wait_on_rate_limit=True)

# Reddit Authentication
reddit = praw.Reddit(client_id = "lzGC0n5GmClEoK_gdSitAA",
                     client_secret = allKeys[4].strip(),
                     username = "DailyTechNewsTweet",
                     password = allKeys[5].strip(),
                     user_agent = "DailyTechNews")

# Tweet Code
subreddit = reddit.subreddit("technews+apple")
top = subreddit.top(time_filter = "day", limit = 1)
for post in top:
    api.update_status("#DTN\n[" + post.title + "]\n" + post.url)