from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import yake
import praw

def get_article(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urlopen(req).read()
    except:
        return ""
    htmlparse = BeautifulSoup(html, 'html.parser')
    article = ""
    for para in htmlparse.find_all("p"):
        article += para.get_text()
    return article

def get_keywords(article):
    kw_extractor = yake.KeywordExtractor(lan="en", 
                                         n=1, 
                                         dedupLim=0.9, 
                                         dedupFunc="seqm", 
                                         windowsSize=1, 
                                         top=7, 
                                         features=None)
    keywords = kw_extractor.extract_keywords(article)

    keyword_list = []
    for kw in keywords:
        if kw[0].isalnum():
            keyword_list.append(kw[0])
    return keyword_list

def get_top_post(subreddit, api):
    status = api.user_timeline(screen_name="DailyTechnoNews", count=1)
    top = subreddit.top(time_filter = "day", limit = 10)
    recent_tweet_title = status[0].text[status[0].text.find("[")+1:status[0].text.find("]")]
    if(status):
        for submission in top:
            if(recent_tweet_title == submission.title) or ("www.reddit.com" in submission.url):
                continue
            else:
                return submission
    else:
        for submission in top:
            return submission