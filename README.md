# Daily-Tech-News

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/ankushmadharha/)

Twitter Account: https://twitter.com/DailyTechnoNews

# Project Description
This is a twitter bot that tweets out technology-related news from the subreddit [r/technews](www.reddit.com/r/technews). It uses the [Tweepy](https://docs.tweepy.org/en/stable/) and [PRAW](https://praw.readthedocs.io/en/stable/) to use the twitter and reddit API's to send and recieve information. Additionally, it uses ChatGPT to create summaries of the articles.

# Functionality

## Tweets:
```py
# Build the tweet content 
article_title = reddit_wrapper.get_top_post_title(time='day', subreddit='technews')
article_url = reddit_wrapper.get_top_post_url(time='day', subreddit='technews')
tweet_content = f'{article_title} {article_url}'

# Tweet out the content
twitter_wrapper.tweet(tweet_content)
```
It tweets out the top article of today from the subreddit [r/technews](www.reddit.com/r/technology). The bot tweets at 6:30 AM EST everyday, and since the time filter is by `day`, duplicates are not a problem.

## Replies:
```py
# Build the reply (summary) using ChatGPT
article = Article(article_url)
article.download()
article.parse()

prompt = f'Summaraize the following article for a tweet, be VERY concise: {article.text}'
reply_content = 'TLDR:\n' + chatgpt.get_response(prompt)
...
# Reply to the tweet
twitter_wrapper.reply_to_recent(reply_content)
```
The bot uses ChatGPT to create a summary of the article, with the max tokens being set to 50 to ensure the reply tweet content does not exceed to tweet character limit.

# Project Specifications
* This project was created and tested using [Python version 3.11.3](https://www.python.org/downloads/).
* This project uses the [Tweepy](https://pypi.org/project/tweepy/) version 4.14.0.
* This project uses the [PRAW](https://pypi.org/project/praw/) version 7.7.0.
* The bot runs automatically using Github Actions.