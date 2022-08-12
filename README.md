# Daily-Tech-News

## Project Description
This is a simple python script that uses tweepy and praw to interact with the twitter and reddit API's respectively. It takes the top post of today off the following subreddits, depending on which post is most popular:
- [r/apple](https://www.reddit.com/r/apple/)
- [r/technology](https://www.reddit.com/r/technology/)

If the bot has already tweeted out the top post from these subs, or the top post does not contain a url, it will take the top post from [r/technews](https://www.reddit.com/r/technews/).

The bot will tweet out the title of the post and the associated article link. It will also find 5 keywords in the article to use as hashtags within the tweet. It will post everyday at 9AM EST.

Twitter: https://twitter.com/DailyTechnoNews

