import tweepy
import Authentication
import Info
import Reply

# Twitter Authentication
auth = Authentication.authTwitter()
api = tweepy.API(auth, wait_on_rate_limit=True)

# Reddit Authentication
reddit = Authentication.authReddit()

# Get top reddit post that contain a URL
subreddit = reddit.subreddit("technology")
submission = Info.get_post(subreddit, api)
if len(submission.title) > 150:
    title = submission.title[0:150] + "..."
else:
    title = submission.title

# Get keywords list
article = Info.get_article(submission.url)
keyword_list = Info.get_keywords(submission.title + ", " + article, 7)

# Create Tweet
hashtags = ""
for kw in keyword_list:
    hashtags += "#" + kw + " "
tweet = "#DTN #DailyTechNews\n[" + title + "]\n" + hashtags + "\n" + submission.url

# Tweet 
api.update_status(tweet)

# Like own recent tweet
status = api.user_timeline(screen_name="DailyTechnoNews", count=1)
api.create_favorite(status[0].id)

# Reply to popular tech people's most recent tweet
Reply.reply_to_user(api, "elonmusk")
Reply.reply_to_user(api, "sundarpichai")
Reply.reply_to_user(api, "satyanadella")
Reply.reply_to_user(api, "tim_cook")
Reply.reply_to_user(api, "MKBHD")