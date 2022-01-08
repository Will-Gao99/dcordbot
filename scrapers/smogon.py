from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup as Soup

GEN_LIST = ['rb','gs','rs','dp','bw','xy','sm','ss']
GEN_IDX = 27


class Smogon:

    def __init__(self, name):
        self.name = name
        self.url = 'https://www.smogon.com/dex//pokemon/' + self.name

    def _getBestGen():
        bestGen = ''
        for i in GEN_LIST:
            # For pokemon > gen 1, must implement a way to deal with empty pages
            # e.g. there is no smogon.com/dex/dp/excadrill
