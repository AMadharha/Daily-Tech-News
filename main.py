import tweepy
import authentication
import keywords

# Twitter Authentication
auth = authentication.authTwitter()
api = tweepy.API(auth, wait_on_rate_limit=True)

# Reddit Authentication
reddit = authentication.authReddit()

# Get top reddit post
subreddit = reddit.subreddit("apple+technology")
top = subreddit.top(time_filter = "day", limit = 1)

# URL and duplication verification
status = api.user_timeline(screen_name="DailyTechnoNews", count=1)
if(status):
    prev_tweet = status[0].text[status[0].text.find('[')+1:status[0].text.find(']')]
    substring = "www.reddit.com"
    for post in top:
        if (substring in post.url) or (prev_tweet.strip() == post.title.strip()):
            subreddit = reddit.subreddit("technews")
            new_top = subreddit.top(time_filter="day", limit = 1)
        else:
            new_top = subreddit.top(time_filter = "day", limit = 1)
else:
    new_top = subreddit.top(time_filter = "day", limit = 1)

# Get keywords list
article = ""
for post in new_top:
    article = keywords.get_article(post.url)
keyword_list = keywords.get_keywords(post.title + ", " + article)

# Create Tweet
hashtags = ""
for kw in keyword_list:
    hashtags += "#" + kw + " "
tweet = "#DTN #DailyTechNews\n[" + post.title + "]\n" + hashtags + "\n" + post.url

# Tweet 
api.update_status(tweet)

# Like own recent tweet
status = api.user_timeline(screen_name="DailyTechnoNews", count=1)
api.create_favorite(status[0].id)