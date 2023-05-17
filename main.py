# IMPORTS
from twitter import TwitterWrapper
from reddit import RedditWrapper
from open_ai import ChatGPT
import time
from newspaper import Article

# Instantiate modules
twitter_wrapper = TwitterWrapper()
reddit_wrapper = RedditWrapper()
chatgpt = ChatGPT()

# Build the tweet content 
article_title = reddit_wrapper.get_top_post_title(time='day', subreddit='technews')
article_url = reddit_wrapper.get_top_post_url(time='day', subreddit='technews')
tweet_content = f'{article_title} {article_url}'

# Tweet out the content
twitter_wrapper.tweet(tweet_content)

time.sleep(5)

try:
    # Build the reply (summary) using ChatGPT
    article = Article(article_url)
    article.download()
    article.parse()

    prompt = f'Summaraize the following article for a tweet, be VERY concise: {article.text}'
    reply_content = 'TLDR:\n' + chatgpt.get_response(prompt)

    last_period_index = reply_content.rfind(".")
    if last_period_index != -1:
        reply_content = reply_content[:last_period_index+1]
except Exception:
    reply_content = "Follow for more tech news!"

# Reply to the tweet
twitter_wrapper.reply_to_recent(reply_content)
