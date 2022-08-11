import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_article(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    htmlparse = BeautifulSoup(html, 'html.parser')
    article = ""
    for para in htmlparse.find_all("p"):
        article += para.get_text()
    return article