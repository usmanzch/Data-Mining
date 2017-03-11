#!/usr/bin/env python
import urllib2  # works fine with Python 2.7.9 (not 3.4.+)
import json
import time
import sys
import thread
import datetime
import os

global dictionary
dictionary = {}
 
def fetchMarket(symbol, exchange, position):

    link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
    url = link+"%s:%s" % (exchange, symbol)
    try:
        u = urllib2.urlopen(url)
    except:
       print ("Could not find stock "+str(symbol)+" on exchange "+str(exchange))
       sys.exit()

    content = u.read()
    data = json.loads(content[3:])

    info = data[0]

    l = str(info['l'])    # market price 

    
    dictionary[position] = l



symbols = ['RY', 'TD', 'BNS', 'CNI', 'SU', 'BCE', 'BMO', 'ENB', 'TRP', 'CNQ', 'BAM', 'CM', 'MFC', 'ABX', 'SLF', 'TU', 'CP', 'GG', 'RCI', 'MGA', 'POT', 'FNV', 'TRI', 'AGU', 'AEM', 'CVE', 'PBA', 'GIB', 'SLW', 'QSR', 'IMO', 'CPG', 'SJR', 'GIL', 'ECA', 'VRX', 'TCK', 'KGC', 'AUY', 'CCJ', 'EGO','BBRY']

filename = "TSX_5m.csv"
if os.path.exists(filename) == False:
    with open(filename, 'a+') as file:
            today = datetime.datetime.now().strftime('Date / Time')
            file.write(today)
            for symbol in symbols:
                file.write(",")
                file.write(symbol)
            file.write('\n')



exchange = "NYSE"
currTime = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S') # left off here

    
with open(filename, 'a+') as file:
    file.write(currTime)
    file.write(",")

for position,symbol in enumerate(symbols):
    if symbol == "BBRY":
        exchange = "NASDAQ"

    thread.start_new_thread( fetchMarket, (symbol, exchange,position) )

time.sleep(10)
with open(filename, 'a+') as file:
    for num in range(0,len(symbols)):
        file.write(dictionary[num]) 
        file.write(",")
    file.write('\n')

#print("%s\t%.2f" % (t, l))




