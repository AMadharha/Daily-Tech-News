import Info
import Authentication
import tweepy
from essential_generators import DocumentGenerator

def reply_to_user(api, user):
    status = api.user_timeline(screen_name=user, count=1, exclude_replies=True)
    keywords = Info.get_keywords(status[0].text, 1)
    gen = DocumentGenerator()

    if not keywords:
        return

    while True:
        reply = gen.gen_sentence(min_words=10, max_words=20)
        if keywords[0] in reply:
            break

    api.update_status(status="@" + user + " " + reply, in_reply_to_status_id=status[0].id)

    status = api.user_timeline(screen_name="DailyTechnoNews", count=1)
    api.create_favorite(status[0].id)   

auth = Authentication.authTwitter()
api = tweepy.API(auth, wait_on_rate_limit=True)

reply_to_user(api, "elonmusk")
reply_to_user(api, "sundarpichai")
reply_to_user(api, "satyanadella")
reply_to_user(api, "tim_cook")
reply_to_user(api, "MKBHD")