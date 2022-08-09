import tweepy
import praw

all_keys = open("keys", "r").read().splitlines()

# Twitter Authentication
API_KEY = all_keys[0].strip()
API_KEY_SECRET = all_keys[1].strip()
ACCESS_TOKEN = all_keys[2].strip()
ACCESS_TOKEN_SECRET = all_keys[3].strip()

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) 

api = tweepy.API(auth, wait_on_rate_limit=True)

# Reddit Authentication
reddit = praw.Reddit(client_id = "lzGC0n5GmClEoK_gdSitAA",
                     client_secret = all_keys[4].strip(),
                     username = "DailyTechNewsTweet",
                     password = all_keys[5].strip(),
                     user_agent = "DailyTechNews")

# Tweet Code
subreddit = reddit.subreddit("technews")
top = subreddit.top("day", limit = 1)
