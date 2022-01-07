from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup as Soup

class Bulbapedia:
    def __init__(self, name):
        self.name = name
        self.url = 'https://bulbapedia.bulbagarden.net/wiki/_(Pok%C3%A9mon)'
        self._updateUrl()

    def _updateUrl(self):
        self.url = self.url[:40] + '_'.join(self.name.split()[1:]) + self.url[40:]

    def search(self):
        #Opens and grabs the page
        response = requests.get(self.url)
        page = response.text
        #html parsing
        page_soup = Soup(page, 'html.parser')
        #grabs content
        content = page_soup.tbody.findAll("")
        for item in content:
            print(item)
            #info = item.findAll('td')
            #print(item)
            #return EV Spread

    def run(self):
        self.search()
        