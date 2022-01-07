from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup as Soup

STAT_IDX = 59
ROW_IDX = 16

STAT_MAP = {1:{'class':'roundy', 'style':'background:#FF5959;', 'width':"16%"},2:{'class':'roundy', 'style':"background:#F5AC78;", 'width':"17%"},
            3:{'class':'roundy', 'style':"background:#FAE078;", 'width':"16%"},4:{'class':'roundy', 'style':"background:#9DB7F5;", 'width':"17%"},
            5:{'class':'roundy', 'style':"background:#A7DB8D;", 'width':"17%"},6:{'class':'roundy', 'style':"background:#FA92B2;", 'width':"17%"}}

class Bulbapedia:

    def __init__(self, name):
        self.name = name
        self.url = 'https://bulbapedia.bulbagarden.net/wiki/_(Pok%C3%A9mon)'
        self._updateUrl()

    def _htmlToStat(self, html):
        return str(html)[STAT_IDX]

    def _updateUrl(self):
        self.url = self.url[:40] + self.name + self.url[40:]

    def findEvs(url):
        response = requests.get(url)
        page_soup = Soup(response.text, "html.parseer")


    def search(self):
        #Opens and grabs the page
        response = requests.get(self.url)
        page = response.text
        #html parsing
        page_soup = Soup(page, 'html.parser')
        #grabs content
        
        div = page_soup.find("div", class_="mw-parser-output")
        table = div.find("table", class_="roundy")
        body = table.tbody
        rows = body.find_all("tr")
        lst = []
        for child in body.children:
            lst.append(child)
               
        temp = lst[ROW_IDX]
        
        statList = []
        for i in range(6):
            stat = temp.find('td', attrs=STAT_MAP[i+1])
            statList.append(self._htmlToStat(stat))

        return self.name+"'s EVs are: "+statList[0]+" Hp, "+statList[1]+" Atk, "+statList[2]+" Def, "+statList[3]+" SpAtk, "+statList[4]+" SpDef, "+statList[5]+" Spd"
        
        