import tweepy
import praw
import config
from boto.s3.connection import S3Connection
import os

s3 = S3Connection(os.environ["API_KEY"], 
                  os.environ["API_KEY_SECRET"],
                  os.environ["ACCESS_TOKEN"],
                  os.environ["ACCESS_TOKEN_SECRET"],
                  os.environ["CLIENT_SECRET"],
                  os.environ["PASSWORD"])

# Twitter authentication
def authTwitter():
    auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET")) 
    return auth

# Reddit Authentication
def authReddit():
    reddit = praw.Reddit(client_id = "lzGC0n5GmClEoK_gdSitAA",
                     client_secret = os.getenv("CLIENT_SECRET"),
                     username = "DailyTechNewsTweet",
                     password = os.getenv("PASSWORD"),
                     user_agent = "DailyTechNews")
    return reddit