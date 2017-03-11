import urllib2  # works fine with Python 2.7.9 (not 3.4.+)
from bs4 import BeautifulSoup
import json
import time
import sys


url = 'http://www.investing.com/indices/us-spx-500-futures'

req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen( req )
soup = BeautifulSoup(con, "lxml")
table = soup.find('td', {'class': 'lastNum pid-8839-last'})


for data in table:
	data = data.replace(',', '')
    filename = 'SnP500Futures.csv'
    with open(filename, 'w') as file:
        file.write('S&P 500 Future,')
        file.write(data)

