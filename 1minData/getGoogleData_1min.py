import urllib2
import os
import datetime
import collections
import sys
import datetime
import time
import csv
os.chdir(sys.path[0])

def fetchData(ticker):
    
    url = "https://www.google.com/finance/getprices?i=60&p=20d&f=d,o,h,l,c,v&df=cpct&q="+str(ticker)
    f = urllib2.urlopen(url)
    data = f.read()

    filename = ticker+'.csv'
    with open(filename, "wb") as code:
        code.write(data)
for arg in sys.argv[1:]:
    print arg

for ticker in sys.argv[1:]:
    fetchData(ticker)