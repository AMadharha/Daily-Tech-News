import tweepy
import authentication
import keywords

# Twitter Authentication
auth = authentication.authTwitter()
api = tweepy.API(auth, wait_on_rate_limit=True)

# Reddit Authentication
reddit = authentication.authReddit()

# Get top reddit post that contain a URL
subreddit = reddit.subreddit("apple+technology+technews")
submission = keywords.get_top_post(subreddit, api)

# Get keywords list
article = keywords.get_article(submission.url)
keyword_list = keywords.get_keywords(submission.title + ", " + article)

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

