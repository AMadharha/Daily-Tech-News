import tweepy
import Authentication
import Info

def generate_tweet(subreddit):
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
    return tweet

# Twitter Authentication
auth = Authentication.authTwitter()
api = tweepy.API(auth, wait_on_rate_limit=True)

# Reddit Authentication
reddit = Authentication.authReddit()

# Create tweet
subreddit = reddit.subreddit("technology")
tweet = generate_tweet(subreddit)

# Tweet 
api.update_status(tweet)

# Like own recent tweet
status = api.user_timeline(screen_name="DailyTechnoNews", count=1)
api.create_favorite(status[0].id)
