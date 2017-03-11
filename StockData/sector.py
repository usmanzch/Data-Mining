import urllib2  # works fine with Python 2.7.9 (not 3.4.+)
from bs4 import BeautifulSoup
import json
import time
import sys
import re

def getRatios(symbol):
    try:
        exchange ='NYSE'
        link = 'https://www.google.ca/finance?q='
        url = link+'%s:%s' % (exchange, symbol)
        url2 = "http://www.google.com/finance/historical?q="+str(exchange)+"%3A"+str(symbol)+"&startdate=&enddate=&output=csv"
        f = urllib2.urlopen(url2)
    except:
        try:
            exchange ='NASDAQ'
            link = 'https://www.google.ca/finance?q='
            url = link+'%s:%s' % (exchange, symbol)
            url2 = "http://www.google.com/finance/historical?q="+str(exchange)+"%3A"+str(symbol)+"&startdate=&enddate=&output=csv"
            f = urllib2.urlopen(url2)       
        except:
            print('Unable to get data for {} from google, skipping...\n'.format(symbol))
    try:
        soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")
        data = soup.find('a', {'id': 'sector'})
        for sector in data:
            sector = sector
            sector = sector.replace(",", "")

        data = data.nextSibling.nextSibling
        for industry in data:
            industry = industry.replace(" - NEC", "")
            industry = industry.replace(",", "")
    except:
        sector = "null"
        industry = "null"

        


    
    return (sector,industry)


tickers = ['AAPL',   'PG',   'AMZN', 'FB',   'BABA', 'WFC',  'MSFT', 'NFLX', 'JPM',  'GOOG', 'XOM',  'C',    'T',    'CHTR', 'AGN',  'CRM',  'GILD', 'JNJ',  'BMY',  'CVX',  'DIS',  'V',    'MRK',  'VZ',   'NVDA', 'HD',   'TSLA', 'WMT',  'MDVN', 'CMCSA',    'CVS',  'NKE',  'NXPI', 'BRK.B',    'ORCL', 'KO',   'MON',  'IBM',  'AVGO', 'YHOO', 'SLB',  'MCD',  'GS',   'UNH',  'PEP',  'HON',  'BIDU', 'BA',   'SBUX', 'AMGN', 'APC',  'CMG',  'PM',   'CAT',  'IBB',  'BIIB', 'LOW',  'AIG',  'HAL',  'COST', 'ATVI', 'MA',   'UTX',  'ABBV', 'MO',   'CELG', 'YUM',  'CTSH', 'OXY',  'TGT',  'APA',  'NTES', 'ACN',  'COP',  'WYNN', 'DOW',  'MET',  'ABT',  'MMM',  'WBA',  'LMT',  'MCK',  'MAR',  'SE',   'UNP',  'VLO',  'MDLZ', 'PXD',  'TXN',  'WDC',  'USB',  'SO',   'EOG',  'TWX',  'FDX',  'DG',   'LLY',  'ADBE', 'LRCX', 'TEVA', 'REGN', 'LYB',  'CBS',  'NEE',  'UAL',  'APD',  'AXP',  'SWKS', 'EXPE', 'LNKD', 'HES',  'PNC',  'ULTA', 'NEM',  'TMO',  'DHR',  'SPG',  'CTRP', 'UPS',  'CCL',  'DVN',  'TSN',  'TJX',  'DUK',  'RDS.A',    'MPC',  'TWLO', 'DVMT', 'PRU',  'CL',   'LVS',  'ACIA', 'COF',  'DE',   'ESRX', 'GIS',  'DLTR', 'HCA',  'STZ',  'RAI',  'BK',   'TAP',  'PANW', 'SHW',  'AET',  'KHC',  'EA',   'NWL',  'RTN',  'PSX',  'ILMN', 'BAX',  'ANTM', 'STJ',  'SHPG', 'TSO',  'RRC',  'GD',   'BHI',  'CXO',  'KMB',  'DD',   'EMR',  'VMW',  'ZTS',  'SYY',  'ITW',  'D',    'CMI',  'PSA',  'ABC',  'KLAC', 'CAH',  'AEP',  'NOC',  'VFC',  'PPG',  'PRGO', 'ALXN', 'ENB',  'CB',   'BUD',  'TRV',  'CAG',  'STT',  'TSCO', 'PCG',  'PX',   'ADI',  'VMC',  'DFS',  'RCL',  'CLR',  'ETN',  'STI',  'NVS',  'NVO',  'URI',  'TSRO', 'FIS',  'DLR',  'VTR',  'SRE',  'INTU', 'CME',  'WM',   'DISH', 'NSC',  'LVLT', 'WWAV', 'IP',   'JWN',  'RHT',  'EL',   'SYK',  'KSS',  'IR',   'DTE',  'EQR',  'XEL',  'CI',   'TMUS', 'ZBH',  'ADP',  'AAP',  'ED',   'ADSK', 'VRTX', 'HIG',  'NUE',  'BDX',  'LULU', 'ROST', 'HCN',  'WHR',  'INCY', 'DLPH', 'LB',   'FANG', 'K',    'RDS.B',    'ALL',  'MNST', 'PH',   'MJN',  'PEG',  'HP',   'EW',   'PII',  'PLD',  'MMC',  'KMX',  'KSU',  'AVB',  'HSY',  'FLT',  'SWK',  'HOG',  'ADS',  'XLNX', 'XEC',  'SIG',  'WDAY', 'PAYX', 'GWPH', 'SPGI', 'MCHP', 'CLX',  'EIX',  'CPB',  'DVA',  'PCAR', 'DPS',  'AFL',  'GSK',  'MBLY', 'NOW',  'WEC',  'SINA', 'LEN',  'SJM',  'HAS',  'KORS', 'TIF',  'DRI',  'NLSN', 'NFX',  'AKAM', 'FAST', 'ETR',  'FL',   'CHKP', 'TRIP', 'UHS',  'CP',   'EQT',  'FISV', 'LLTC', 'BMRN', 'TRGP', 'BBBY', 'ADM',  'OMC',  'OKE',  'AEM',  'TROW', 'EMN',  'TPX',  'DOV',  'CERN', 'SRCL', 'ES',   'DKS',  'GPN',  'WLTW', 'ROK',  'BLL',  'MCO',  'ECL',  'ALK',  'PDCE', 'TOT',  'ALB',  'ACWI', 'O',    'CSC',  'PVH',  'MNK',  'WB',   'CTXS', 'MCHI', 'MSI',  'CHRW', 'APH',  'CMA',  'BLUE', 'LNG',  'QRVO', 'MTB',  'BXP',  'CNC',  'HSIC', 'WRK',  'LNC',  'AEE',  'Q',    'LH',   'SBAC', 'UN',   'MAA',  'XRAY', 'AMP',  'CMS',  'A',    'PNR',  'SPLK', 'TEL',  'DGX',  'TTWO', 'VRSN', 'PFG',  'WSM',  'EXR',  'YY',   'AWK',  'JBHT', 'CHD',  'VCIT', 'DXCM', 'LEA',  'FBHS', 'CE',   'LDOS', 'BURL', 'VNTV', 'SAP',  'SLG',  'NTRS', 'WCN',  'THS',  'SIX',  'AMBA', 'SLCA', 'MAC',  'AME',  'VNO',  'AGU',  'AAXJ', 'TSS',  'GRUB', 'FFIV', 'RSG',  'RL',   'ASML', 'BERY', 'CRI',  'ALGN', 'JAZZ', 'PKG',  'AER',  'WYN',  'WAB',  'POST', 'FTV',  'UL',   'AMSG', 'PF',   'VAR',  'SNI',  'SEE',  'BG',   'CAVM', 'DNKN', 'WLK',  'HLF',  'HRS',  'RMD',  'EGN',  'GRMN', 'VRSK', 'LBRDK',    'EDU',  'FLR',  'WUBA', 'COL',  'XYL',  'OC',   'TD',   'EAT',  'RDUS', 'AIV',  'PPS',  'HAR',  'RY',   'ANET', 'RGLD', 'DY',   'PAG',  'CONE', 'DATA', 'SPR',  'EXPD', 'TTM',  'LN',   'MAN']

metrics = ['Sector', 'Industry']
filename = 'SectorIndustry'
output = open(filename, 'w')
output.write('Metrics,{}\n'.format(','.join(tickers)))
for metric in metrics:
    output.write(metric)
    output.write('\n')
output.close()

for ticker in tickers:
    print ticker
    (sector, industry)= getRatios(ticker)
    print sector
    print industry
    
    
    



    
    ########################DATA COMING IN NICE AND GOOD###############################
    
    with open(filename, "r") as file:
        lines = file.readlines()
    file.close()
    
    lines = map(lambda s: s.strip(), lines)
    
 
    
    lines[0] = lines[0] + '\n'
    lines[1] = lines[1]+','+sector +'\n'
    lines[2] = lines[2]+','+industry+ '\n'
    

    sizeLines = len(lines)
    

    output = open(filename, 'w')
    x = 0
    while x < sizeLines:
       
        output.write(lines[x])

        x += 1 

    output.close()




