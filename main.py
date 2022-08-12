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

# Get keywords list
for post in top:
    article = keywords.get_article(post.url)
keyword_list = keywords.get_keywords(post.title + ", " + article)

# Create Tweet
hashtags = ""
for kw in keyword_list:
    hashtags += "#" + kw + " "
tweet = "#DTN #DailyTechNews\n[" + post.title + "]\n" + hashtags + "\n" + post.url

# Tweet Code
api.update_status(tweet)