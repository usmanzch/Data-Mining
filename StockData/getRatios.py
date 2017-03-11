import urllib2  # works fine with Python 2.7.9 (not 3.4.+)
from bs4 import BeautifulSoup
import json
import time
import sys
import requests


def getRatios(symbol, exchange):
    link = 'https://www.google.ca/finance?q='
    url = link+'%s:%s' % (exchange, symbol)
    req = urllib2.Request('https://www.google.ca/finance?q=AAPL:NASDAQ', headers={ 'User-Agent': 'Mozilla/5.0' })
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html, "lxml")
    print soup
    table = soup.find('table', {'class': 'gf-table'})
    
    table_val = table.find_all('td', {'class': 'hilite'})
    print table_val


tickers = ['aapl', 'ge']

for ticker in tickers:
    size = len(ticker)
    if size <= 3:
        indexName = 'NYSE'
    if size > 3:
        indexName = 'NASDAQ'

    getRatios(ticker,indexName)
    i = raw_input()