import requests
import pandas as pd
from bs4 import BeautifulSoup

def keywords():
    def getdata(url):
        r = requests.get(url)
        return r.text
    
    htmldata = getdata("https://www.newsweek.com/ceos-linkedin-crying-selfie-about-layoffs-backlash-1732677")
    soup = BeautifulSoup(htmldata, "html.parser")
    data = ""
    for data in soup.find_all("p"):
        print(data.get_text())