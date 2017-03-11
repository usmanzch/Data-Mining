import urllib2
import os
import sys

def fetchData(ticker):
    
    url = "https://www.google.com/finance/getprices?i=300&p=60d&f=d,o,h,l,c,v&df=cpct&q="+str(ticker)
    f = urllib2.urlopen(url)
    data = f.read()

    filename = ticker+'.csv'
    with open(filename, "wb") as code:
        code.write(data)

tickers = ['aapl','goog','tsla']
for ticker in tickers:
    fetchData(ticker)
    print 'Downloading data for:' + str(ticker)

x = raw_input() #this pauses the screen by making you press a keyboard input