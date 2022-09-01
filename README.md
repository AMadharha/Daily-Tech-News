# Daily-Tech-News

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/ankushmadharha/)

Twitter Account: https://twitter.com/DailyTechnoNews

# Project Description
This is a twitter bot that tweets out technology-related news from the subreddit [r/technology](www.reddit.com/r/technology). It uses the [Tweepy](https://docs.tweepy.org/en/stable/) and [PRAW](https://praw.readthedocs.io/en/stable/) python wrappers to use the twitter and reddit API's to send and recieve information.

## Functionality
The bot does it all, it tweets, retweets, likes, and replies.

### Tweets:
    tweet.py
It tweets out an article from the subreddit [r/technology](www.reddit.com/r/technology). It avoids tweeting out duplicate articles by checking if the bot has already tweeted out the specific news article. It takes the article and finds 5 keywords to use as hashtags in the tweet. It tweets out every 3 hours, at the intervals (EST): 3AM/PM, 6AM/PM, 9AM/PM, 12AM/PM.

### Retweets:
    retweet.py
To retweet, the bot uses the `API.search_tweets` function included in Tweepy with the `result_type` set to _popular_ and the `query` set to _technology_. After retrieving this tweet, the bot retweets it.

### Likes:
    like.py
The liking functionality is similar to how the retweets work, with a different `result_type` and `query`. For liking, the `result_type` is set to _recent_ and `query` is set to _science_. Aftter retreiving the tweet the bot likes it.

### Replies
    reply.py
The reply works by taking the top comment from the top post of today from a specified subreddit. Currently, the bot replies to the following accounts, taking the comment from the corresponding subreddit (`reply_to_user(user, subreddit)`):
* `reply_to_user("elonmusk", "teslamotors")`
* `reply_to_user("MKBHD", "mkbhd")`
* `reply_to_user("neiltyson", "space")`
* `reply_to_user("LinusTech", "LinusTechTips")`
* `reply_to_user("NASAEarth", "EarthPorn")`

# Project Specifications
* This project was created and tested using [Python version 3.10.6](https://www.python.org/downloads/)
* This project uses the [Tweepy](https://pypi.org/project/tweepy/) version 4.10.0 python wrapper to interact with the Twitter API.
* This project uses the [PRAW](https://pypi.org/project/praw/) version 7.6.0 python wrapper to interact with the Reddit API.
* The bot runs all its scheduled tasks on [Heroku](www.heroku.com).


