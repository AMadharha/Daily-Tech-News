import tweepy
import Authentication

auth = Authentication.authTwitter()
api = tweepy.API(auth, wait_on_rate_limit=True)

search_results = api.search_tweets(q="science", 
                                   lang="en", 
                                   result_type="mixed",
                                   count=1)

result = search_results[0]
api.create_favorite(id=result.id)