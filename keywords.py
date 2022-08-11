import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import yake

def get_article(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    htmlparse = BeautifulSoup(html, 'html.parser')
    article = ""
    for para in htmlparse.find_all("p"):
        article += para.get_text()
    return article

def get_keywords(article):
    language = "en"
    max_ngram_size = 1
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 10

    kw_extractor = yake.KeywordExtractor(lan=language, 
                                         n=max_ngram_size, 
                                         dedupLim=deduplication_thresold, 
                                         dedupFunc=deduplication_algo, 
                                         windowsSize=windowSize, 
                                         top=numOfKeywords, 
                                         features=None)
    keywords = kw_extractor.extract_keywords(article)

    keyword_list = []
    for kw in keywords:
        keyword_list.append(kw[0])
    
    return keyword_list

