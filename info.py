from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import yake

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

def get_post(subreddit, api):
    top = subreddit.top(time_filter = "day")
    tweet_list = api.user_timeline(user_id="DailyTechnoNews",)
    
    submission = next(top)
    
    #(tweet_text in submission.title) or ("reddit.com" in submission.url)
    tweet_text = (tweet_list[0].text[tweet_list[0].text.find("[")+1:tweet_list[0].text.find("]")]).split("… https:")[0]
    while True:   
        valid = True
        for tweet in tweet_list:
            tweet_text = (tweet.text[tweet.text.find("[")+1:tweet.text.find("]")]).split("… https:")[0]
            if (tweet_text in submission.title) or ("reddit.com" in submission.url):
                submission = next(top)
                valid = False
                break
        if(valid):
            break
        
    return submission