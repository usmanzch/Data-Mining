import urllib2
import datetime
import json
import sys
import time
import sys
import os
from threading import Thread

os.chdir(sys.path[0]) #for task scheduler automation

global dictionary_open
dictionary_open = {}

global dictionary_close
dictionary_close = {}

global dictionary_high
dictionary_high = {}

global dictionary_low
dictionary_low = {}

def fetchMarket(arg):
    position = arg[0]
    symbol = arg[1]
    print symbol
    try:
        exchange = 'NYSE'
        link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
        url = link+"%s:%s" % (exchange, symbol)
        u = urllib2.urlopen(url)
        content = u.read()
        data = json.loads(content[3:])
        info = data[0]

        o = str(info['op'])
        l =  str(info['l'])
        hi = str(info['hi'])
        lo =str(info['lo'])

        if o == '0' or o == '-' or o == '':
            o = "nan"
        if l == '0' or l == '-' or l == '':
            l = "nan"
        if hi == '0' or hi == '-' or hi == '':
            hi = "nan"
        if lo == '0' or lo == '-' or lo == '':
            lo = "nan"

        dictionary_open[position] = o
        dictionary_close[position] = l
        dictionary_high[position] = hi
        dictionary_low[position] = lo
    except:
        try:
            exchange = 'NASDAQ'
            link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
            url = link+"%s:%s" % (exchange, symbol)
            u = urllib2.urlopen(url)
            content = u.read()
            data = json.loads(content[3:])
            info = data[0]

            o = str(info['op'])
            l =  str(info['l'])
            hi = str(info['hi'])
            lo =str(info['lo'])

            if o == '0' or o == '-' or o == '':
                o = "nan"
            if l == '0' or l == '-' or l == '':
                l = "nan"
            if hi == '0' or hi == '-' or hi == '':
                hi = "nan"
            if lo == '0' or lo == '-' or lo == '':
                lo = "nan"

            dictionary_open[position] = o
            dictionary_close[position] = l
            dictionary_high[position] = hi
            dictionary_low[position] = lo
        except:
            print("Could not find stock "+str(symbol)+" on exchange "+str(exchange))
            dictionary_open[position] = "nan"
            dictionary_close[position] = "nan"
            dictionary_high[position] = "nan"
            dictionary_low[position] = "nan"


symbols = ['DISH','BNS','AEE','LVLT','EXPD']
currDate = datetime.datetime.now().strftime('%m/%d/%Y') # left off here

threads = []
for position,symbol in enumerate(symbols):
    arg = [position, symbol]
    t = Thread(target=fetchMarket, args=(arg,))
    threads.append(t)

for x in threads:
    x.start()
for x in threads:
    x.join()
###############################################################
filename = 'TITANIC/TITANIC_Open.csv'
lines = open(filename, 'r').readlines()  

lastDate = lines[-1].split(',')
lastDate = lastDate[0]

if lastDate == currDate:
    del lines[-1] 
open(filename, 'w').writelines(lines) 

with open(filename, 'a+') as file:
    file.write(currDate)
    file.write(",")

with open(filename, 'a+') as file:
    for num in range(0,len(symbols)):
        value = dictionary_open[num];
        value = value.replace(',', '')
        file.write(value) 
        file.write(",")
    file.write('\n')
###############################################################
filename = 'TITANIC/TITANIC_Close.csv'
lines = open(filename, 'r').readlines()

lastDate = lines[-1].split(',')
lastDate = lastDate[0]

if lastDate == currDate: 
    del lines[-1] 
open(filename, 'w').writelines(lines) 

with open(filename, 'a+') as file:
    file.write(currDate)
    file.write(",")

with open(filename, 'a+') as file:
    for num in range(0,len(symbols)):
        value = dictionary_close[num];
        value = value.replace(',', '')
        file.write(value) 
        file.write(",")
    file.write('\n')
###############################################################
filename = 'TITANIC/TITANIC_High.csv'
lines = open(filename, 'r').readlines()

lastDate = lines[-1].split(',')
lastDate = lastDate[0]

if lastDate == currDate: 
    del lines[-1] 
open(filename, 'w').writelines(lines) 

with open(filename, 'a+') as file:
    file.write(currDate)
    file.write(",")

with open(filename, 'a+') as file:
    for num in range(0,len(symbols)):
        value = dictionary_high[num];
        value = value.replace(',', '')
        file.write(value) 
        file.write(",")
    file.write('\n')
###############################################################
filename = 'TITANIC/TITANIC_Low.csv'
lines = open(filename, 'r').readlines()

lastDate = lines[-1].split(',')
lastDate = lastDate[0]

if lastDate == currDate: 
    del lines[-1] 
open(filename, 'w').writelines(lines) 

with open(filename, 'a+') as file:
    file.write(currDate)
    file.write(",")

with open(filename, 'a+') as file:
    for num in range(0,len(symbols)):
        value = dictionary_low[num];
        value = value.replace(',', '')
        file.write(value) 
        file.write(",")
    file.write('\n')