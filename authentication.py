import tweepy
import praw
import config

# Twitter authentication
def authTwitter():
    auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET) 
    return auth

# Reddit Authentication
def authReddit():
    reddit = praw.Reddit(client_id = "lzGC0n5GmClEoK_gdSitAA",
                     client_secret = config.CLIENT_SECRET,
                     username = "DailyTechNewsTweet",
                     password = config.PASSWORD,
                     user_agent = "DailyTechNews")
    return reddit