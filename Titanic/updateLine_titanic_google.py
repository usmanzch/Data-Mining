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
        if o == '0' or o == '-' or o == '':
            o = "nan"
        if l == '0' or l == '-' or l == '':
            l = "nan"
        dictionary_open[position] = o
        dictionary_close[position] = l
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
            if o == '0' or o == '-' or o == '':
                o = "nan"
            if l == '0' or l == '-' or l == '':
                l = "nan"
            dictionary_open[position] = o
            dictionary_close[position] = l
        except:
            print("Could not find stock "+str(symbol)+" on exchange "+str(exchange))
            dictionary_open[position] = "nan"
            dictionary_close[position] = "nan"



symbols = ['AGN',	'JBHT',	'CPB',	'QRVO',	'SBAC',	'EOG',	'AGU',	'NXPI',	'CP',	'TAP',	'VRTX',	'AAPL',	'SPG',	'FIS',	'GIS',	'MJN',	'ROP',	'GD',	'VAR',	'AMZN',	'MAR',	'SNA',	'SNI',	'XRAY',	'MAC',	'SNP',	'JNJ',	'TSN',	'TSO',	'CMI',	'CMG',	'CME',	'CHKP',	'DTE',	'NKE',	'PCG',	'VLO',	'HUM',	'PCLN',	'BABA',	'GRMN',	'K',	'FFIV',	'BLL',	'HCA',	'BLK',	'HCN',	'SIG',	'MA',	'PRGO',	'MO',	'NOC',	'CBS',	'NDAQ',	'UHS',	'TJX',	'AMGN',	'FB',	'COST',	'DPS',	'FL',	'DOW',	'MSFT',	'BDX',	'WHR',	'BXP',	'MDT',	'FMX',	'DFS',	'JEC',	'ILMN',	'V',	'TSCO',	'ALL',	'ALK',	'LMT',	'MMM',	'SO',	'MMC',	'CTSH',	'SWKS',	'ADBE',	'IBM',	'CAT',	'CAH',	'GS',	'LB',	'INCY',	'LH',	'CELG',	'WLTW',	'VZ',	'ABC',	'STJ',	'ANTM',	'XOM',	'STZ',	'CERN',	'RSG',	'PNW',	'PNC',	'FNV',	'GOOGL',	'VFC',	'XLNX',	'AON',	'RY',	'PRU',	'RL',	'SAP',	'AYI',	'CHL',	'URI',	'HRS',	'MRK',	'NLSN',	'NTES',	'RHT',	'APH',	'ROST',	'APC',	'APD',	'KSU',	'NGG',	'IFF',	'BMRN',	'NVDA',	'AVGO',	'RTN',	'BMO',	'PKI',	'AFL',	'EL',	'PAYX',	'OXY',	'SHW',	'ED',	'ORLY',	'DLR',	'EW',	'ES',	'STT',	'WYN',	'ADSK',	'ECL',	'PVH',	'DGX',	'NUE',	'EXPE',	'EXPD',	'UNP',	'DUK',	'R',	'CLX',	'FRT',	'UNH',	'TRIP',	'OMC',	'VMC',	'ITW',	'KLAC',	'SWK',	'PNR',	'WYNN',	'TSLA',	'DG',	'DD',	'DE',	'AAP',	'WBA',	'TGT',	'BIIB',	'AKAM',	'MLM',	'INTU',	'ALXN',	'SLG',	'DHR',	'YUM',	'MCO',	'MCK',	'MCD',	'VTR',	'AXP',	'NFLX',	'WM',	'SRCL',	'EXR',	'VNO',	'AWK',	'HSY',	'DLPH',	'WEC',	'GPN',	'BNS',	'EQR',	'EQT',	'GPC',	'HAR',	'HAS',	'CTXS',	'LVLT',	'SYK',	'LEG',	'SYY',	'AEP',	'CL',	'AET',	'EMN',	'ESRX',	'AEE',	'CTAS',	'EMR',	'FDX',	'AEM',	'CRM',	'PX',	'PG',	'PH',	'PM',	'EFX',	'MHK',	'QCOM',	'ULTA',	'NVS',	'PSA',	'PSX',	'MON',	'MCHP',	'ETR',	'KMB',	'PEP',	'GWW',	'FISV',	'COF',	'TMK',	'ETN',	'COL',	'BCR',	'KMX',	'DLTR',	'ZBH',	'CI',	'CM',	'SRE',	'CB',	'WAT',	'ZTS',	'CHRW',	'SBUX',	'PLD',	'CMCSA',	'MKC',	'CVX',	'AIZ',	'EIX',	'CVS',	'RCL',	'LOW',	'CHD',	'AIG',	'DIS',	'PPG',	'MNST',	'NSC',	'GAS',	'GOOG',	'IR',	'MTB',	'UTX',	'BA',	'DRI',	'CCI',	'TIF',	'ALLE',	'LYB',	'KHC',	'HSIC',	'D',	'DVA',	'BF.B',	'WMT',	'VRSN',	'VRSK',	'CINF',	'NTRS',	'CXO',	'BMY',	'HP',	'FLR',	'REGN',	'DEO',	'HD',	'LLY',	'ROK',	'BRK.B',	'DOV',	'SCG',	'AMG',	'MNK',	'LLL',	'NWL',	'AMP',	'TMO',	'AMT',	'LRCX',	'O',	'UPS',	'TRV',	'AVY',	'AVB',	'NEE',	'ACN',	'TEL',	'SLB',	'LLTC',	'ADS',	'ADP',	'DNB',	'GILD',	'SJM',	'JPM',	'ADI',	'XEC',	'BIDU',	'CHTR',	'AZO',	'MSI',	'DISH',	'TWX',	'PCAR',	'TXN',	'HES',	'TM',	'PXD',	'HOG',	'ESS',	'HON',	'ICE',	'ABBV',	'HOT',	'CNC',	'TROW',	'ISRG',	'CNI',	'EQIX',	'SPGI']

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

#check lines[-1] see if it is the current date
#if the line start with todays date delete it
#else append to it directly

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