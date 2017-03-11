import urllib2
import datetime
import json
import sys
import time
import thread

global dictionary
dictionary = {}

# hardcoded index components


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



symbols = ['XOM','JNJ','GE','T','WFC','JPM','CHL','WMT','PG','VZ','PFE','F','KO','CVX','NVS','BABA','V','FMX','ORCL','HD','DIS','MS','PM','TM','UBS','PEP','IBM','NVO','BAC','UL','UN','TSM','UNH','RIO','C','HSBC','BMY','TOT','MCD','MA','CVS','SNY','MMM','DCM','BP','GSK','ABBV','TJX','SAP','AGN','NKE','UPS','RY','NTT','HON','UTX','ABEV','SNP','BA','TD','LLY','ACN','UNP','LMT','RAI','USB','DEO','AZN','D','LOW','LYG','DHR','MTU','CL','BBL','CAJ','SAN','GS','SPG','AXP','AIG','BNS','LFC','BT','DOW','TMO','DD','EPD','CB','TWX','OXY','NEE','BLK','E','ABT','DUK','NGG','CRM','COP','EMC']
exchange = 'NYSE'
filename = 'NYSE_Close.csv'

currDate = datetime.datetime.now().strftime('%m-%d-%y %H:%M:%S') # left off here


with open(filename, 'a+') as file:
    file.write(currDate)
    file.write(",")

for position,symbol in enumerate(symbols):
    thread.start_new_thread( fetchMarket, (symbol, exchange,position) )

time.sleep(20)
with open(filename, 'a+') as file:
    for num in range(0,len(symbols)):
        file.write(dictionary[num]) 
        file.write(",")

        

   