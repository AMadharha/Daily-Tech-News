import tweepy
import Authentication
from praw.models import MoreComments

def reply_to_user(user, subreddit):
    auth = Authentication.authTwitter()
    api = tweepy.API(auth, wait_on_rate_limit=True)
    reddit = Authentication.authReddit()

    subreddit = reddit.subreddit(subreddit)
    top_list_generator = subreddit.top(time_filter="day", limit=1)
    submission = next(top_list_generator)
    top_score = 0
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        if top_level_comment.score > top_score:
            top_comment = top_level_comment.body
            top_score = top_level_comment.score

    if len(top_comment) > 275:
        top_comment = top_comment[0:150] + "..."

    status = api.user_timeline(screen_name=user, count=1, exclude_replies=True)
    api.update_status(status="@" + user + " " + top_comment, in_reply_to_status_id=status[0].id)

    status = api.user_timeline(screen_name="DailyTechnoNews")
    api.create_favorite(status[0].id) 

reply_to_user("elonmusk", "teslamotors")
reply_to_user("sundarpichai", "google")
reply_to_user("tim_cook", "apple")