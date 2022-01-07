from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup as Soup

class Bulbapedia:
    def __init__(self, name):
        self.name = name
        self.url = 'https://bulbapedia.bulbagarden.net/wiki/_(Pok%C3%A9mon)'

    def keywords_search_words(self, user_message):
        words = user_message.split()[1:]
        keywords = '_'.join(words)
        self.url = self.url[:40] + keywords +self.url[40:]

    def search(self):
#Opens and grabs the page
        response = requests.get(self.url)
        page = response.text
#html parsing
        page_soup = Soup(page, 'html.parser')
#grabs content
        content = page_soup.tbody.findAll("")
        with open("text.txt", "w", encoding="utf-8") as f:
             f.write(page_soup.prettify())
             f.close()
        for item in content:
            print(page_soup.prettify())
            #info = item.findAll('td')
            #print(item)
            #return EV Spread

    def run(self):
        self.keywords_search_words(self.name)
        self.search()
        