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

