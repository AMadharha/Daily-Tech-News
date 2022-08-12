import tweepy
import praw
import config
from boto.s3.connection import S3Connection
import os
from decouple import config

s3 = S3Connection(config("API_KEY"), 
                  config("API_KEY_SECRET"),
                  config("ACCESS_TOKEN"),
                  config("ACCESS_TOKEN_SECRET"),
                  config("CLIENT_SECRET"),
                  config("PASSWORD"))

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