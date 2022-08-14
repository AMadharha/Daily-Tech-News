import tweepy
import authentication
import info

# Twitter Authentication
auth = authentication.authTwitter()
api = tweepy.API(auth, wait_on_rate_limit=True)

# Reddit Authentication
reddit = authentication.authReddit()

# Get top reddit post that contain a URL
subreddit = reddit.subreddit("technology")
submission = info.get_post(subreddit, api)

# Get keywords list
article = info.get_article(submission.url)
keyword_list = info.get_keywords(submission.title + ", " + article)

# Create Tweet
hashtags = ""
for kw in keyword_list:
    hashtags += "#" + kw + " "
tweet = "#DTN #DailyTechNews\n[" + submission.title + "]\n" + hashtags + "\n" + submission.url

# Tweet 
api.update_status(tweet)

# Like own recent tweet
status = api.user_timeline(screen_name="DailyTechnoNews", count=1)
api.create_favorite(status[0].id)

