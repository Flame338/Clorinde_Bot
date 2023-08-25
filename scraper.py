import requests 
from bs4 import BeautifulSoup

def scrape() -> str:
    res = genshin_scrape()
    res = res + star_scrape()
    return res

def genshin_scrape() -> str:
    res = ''
    region = ['EU', 'NA', 'SEA']
    req = requests.get("https://www.gensh.in/events/promotion-codes")

    soup = BeautifulSoup(req.content, "lxml")

    for idx in range(0,3):
        temp = soup.find(attrs={"class" : "promocode mr-1"})
        res = res + region[idx] + " : " + temp.get_text() + "\n"
    return res

def HI3_scrape() -> str:
    res = ''
    return res

def star_scrape() ->str: 
    res = ''
    req = requests.get("https://honkai.gg/codes/")

    soup = BeautifulSoup(req.content, "lxml")
    content_extr = soup.find("table")
    table = content_extr.find("tbody")
    table1 = table.find_all("td")
    for i in table1:
        if (len(i.get_text()) == 12) and (i.get_text() != 'Prime Gaming'):
            res = res + i.get_text() + "\n"
    return res 
