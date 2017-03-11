import urllib2  # works fine with Python 2.7.9 (not 3.4.+)
from bs4 import BeautifulSoup
import json
import time
import sys


def getRatios(symbol, exchange):
    link = 'https://www.google.ca/finance?q='
    url = link+'%s:%s' % (exchange, symbol)
    soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")
    table = soup.find('table', {'class': 'snap-data'})

#####################FIRST HALF OF TABLE##############################
    table_val = table.find_all('td', {'class': 'val'})
    table_vol = table_val[3].string #3 is the vol_and_avg field
    try:
        vol, avvol = table_vol.split('/')
        avvol = avvol.strip('\n')
    except:
        vol = table_vol.strip('\n')
        avvol = '-'

    vol = vol.replace(u',', u'')
    avvol = avvol.replace(u',', u'')
    mktcap = table_val[4].string.strip('\n')
    pe = table_val[5].string.strip('\n')

######################SECOND HALF OF TABLE#############################
    table = table.nextSibling
    table_val = table.find_all('td', {'class': 'val'})

    table_div = table_val[0].string

    try:
        div, div_yield = table_div.split('/')
    except:
        div = '-'
        div_yield='-'
    div_yield=div_yield.strip('\n')
    
    eps = table_val[1].string.strip('\n')
    beta = table_val[3].string.strip('\n')
    data = [vol, avvol, mktcap, pe, div, div_yield, eps, beta]
    sizeData = len(data)
    x = 0
    while x < sizeData:
        data[x] = data[x].replace(u'\xa0\xa0\xa0\xa0-', u'-')
        x+=1
    return data


tickers = ['UTX',   'AGN',  'EOG',  'CPB',  'QRVO', 'JWN',  'SBAC', 'JBHT', 'NXPI', 'TAP',  'VRTX', 'BWA',  'UAL',  'WM',   'SPG',  'ENDP', 'GT',   'GS',   'PYPL', 'MJN',  'WRK',  'ROP',  'GE',   'GD',   'VAR',  'AMZN', 'NTAP', 'MAS',  'MAR',  'MAT',  'SNA',  'FOXA', 'SNI',  'XRAY', 'MAC',  'SNP',  'JNJ',  'XYL',  'SNY',  'TSN',  'AFL',  'TSM',  'BEN',  'CMI',  'EL',   'CMG',  'CME',  'CHKP', 'DTE',  'NKE',  'CMS',  'PCG',  'VLO',  'HUM',  'PCLN', 'FSLR', 'GRMN', 'FTR',  'K',    'FFIV', 'BLL',  'HCA',  'BLK',  'FTI',  'HCN',  'SIG',  'NFX',  'MA',   'CBG',  'MO',   'NOC',  'MU',   'CBS',  'HAR',  'SE',   'MS',   'TJX',  'NOV',  'TIF',  'AMGN', 'COST', 'FE',   'CTL',  'ADBE', 'DOV',  'DOW',  'MSFT', 'GLW',  'SCHW', 'BSX',  'GGP',  'LFC',  'FCX',  'BDX',  'WHR',  'EIX',  'HIG',  'FMX',  'F',    'DFS',  'JEC',  'ILMN', 'TOT',  'V',    'FMC',  'MPC',  'TSCO', 'ALL',  'ALK',  'LMT',  'NTT',  'MMM',  'SO',   'JNPR', 'MMC',  'WEC',  'DPS',  'IBM',  'FIS',  'BAX',  'CAT',  'CAJ',  'CAH',  'BAC',  'GIS',  'CAG',  'URI',  'LB',   'MDLZ', 'INCY', 'LM',   'LH',   'PGR',  'BATRA',    'CELG', 'BATRK',    'WLTW', 'A',    'ABC',  'ZION', 'STI',  'STJ',  'STT',  'ABT',  'XOM',  'STX',  'STZ',  'BHI',  'CERN', 'NCLH', 'PNR',  'PNW',  'IVZ',  'PNC',  'GOOGL',    'VFC',  'GM',   'SAN',  'LMCK', 'AON',  'RY',   'RAI',  'PRU',  'RF',   'RL',   'SAP',  'CHD',  'URBN', 'CHK',  'CHL',  'L',    'HRS',  'HRL',  'MRO',  'MRK',  'HRB',  'IPG',  'NTES', 'RHT',  'TYC',  'RHI',  'APH',  'ROST', 'APC',  'APA',  'APD',  'SRE',  'NGG',  'KSS',  'WFC',  'IFF',  'BMRN', 'NVDA', 'AVGO', 'RTN',  'BMY', 'DISCA',    'PAYX', 'OXY',  'SHW',  'ED',   'DISCK',    'EA',   'ORLY', 'DLR',  'CSX',  'TMK',  'EW',   'ES',   'LUV',  'MUR',  'WYN',  'LUK',  'ADSK', 'ECL',  'SEE',  'PVH',  'DGX',  'NUE',  'EXPE', 'EXPD', 'UNP',  'UDR',  'ETFC', 'BBL',  'XL',   'R',    'CLX',  'CMA',  'BBY',  'FRT',  'UNH',  'BBT',  'TRIP', 'OMC',  'KO',   'VMC',  'KR',   'LNC',  'KEY',  'AEE',  'KLAC', 'SWK',  'RSG',  'WYNN', 'LBTYA',    'TSLA', 'SWN',  'DG',   'DD',   'DE',   'LBTYK',    'DUK',  'AAP',  'TGT',  'HBAN', 'BIIB', 'TSS',  'ATVI', 'AKAM', 'DHI',  'HOLX', 'M',    'MLM',  'INTU', 'ALXN', 'SLG',  'DHR',  'SLB',  'AJG',  'MCO',  'JPM',  'MCD',  'NRG',  'PBCT', 'VTR',  'AXP',  'NFLX', 'EXC',  'AAPL', 'SRCL', 'WU',   'EXR',  'WY',   'DCM',  'VNO',  'UNM',  'RIO',  'SPLS', 'AWK',  'HST',  'RIG',  'HSY',  'CTSH', 'GPN',  'HAL',  'BNS',  'FITB', 'EQR',  'EQT',  'GPC',  'XLNX', 'HAS',  'PH',   'LVLT', 'GPS',  'DRI',  'YUM',  'SYF',  'PHM',  'SYK',  'LEG',  'KIM',  'SYY',  'AEP',  'AES',  'AET',  'EMC',  'EMN',  'HCP',  'ESRX', 'AMAT', 'SWKS', 'CTAS', 'EMR',  'FDX',  'EPD',  'CRM',  'TSO',  'NWSA', 'PX',   'PG',   'CTXS', 'PM',   'EFX',  'C',    'TMUS', 'SIRI', 'QCOM', 'XRX',  'ITW',  'ULTA', 'NVS',  'MOS',  'PSA',  'PSX',  'MON',  'NVO',  'ETR',  'COP',  'DVN',  'KMB',  'DO',   'PEP',  'KMI',  'GWW',  'FISV', 'COG',  'COF',  'COH',  'PEG',  'ETN',  'COL',  'BCR',  'KMX',  'DLTR', 'ZBH',  'CI',   'CL',   'CB',   'CA',   'CF',   'WAT',  'ZTS',  'CHRW', 'TDC',  'SBUX', 'PLD',  'CMCSA',    'MKC',  'PDCO', 'CVX',  'AIZ',  'BXP',  'AIV',  'CVS',  'RCL',  'LOW',  'AYI',  'AIG',  'DIS',  'PPG',  'MNST', 'NSC',  'PPL',  'NDAQ', 'UHS',  'GOOG', 'IP',   'HPQ',  'IR',   'MTU',  'MCHP', 'MTB',  'VZ',   'JCI',  'HPE',  'PWR',  'OKE',  'CSCO', 'WDC',  'HBI',  'BA',   'BK',   'BT',   'CCL',  'BP',   'GSK',  'CTRP', 'FLIR', 'LYG',  'LYB',  'HSIC', 'D',    'NAVI', 'DVA',  'WMT',  'VRSN', 'T',    'WMB',  'TXT',  'OI',   'VRSK', 'UBS',  'CINF', 'NTRS', 'CXO',  'FLS',  'FLR',  'REGN', 'DEO',  'E',    'HD',   'LLY',  'ROK',  'INTC', 'FL',   'SCG',  'AME',  'AMG',  'MNK',  'LLL',  'NWL',  'AMP',  'TMO',  'LRCX', 'MHK',  'O',    'LVNTA',    'YHOO', 'PBI',  'UPS',  'TRV',  'VOD',  'AVY',  'UL',   'UN',   'UA',   'AVB',  'KSU',  'NEM',  'NEE',  'ACN',  'NI',   'TEL',  'RRC',  'FAST', 'NBL',  'HP',   'QVCA', 'LLTC', 'ADS',  'ADP',  'DNB',  'GILD', 'BBBY', 'SJM',  'MCK',  'ADM',  'ADI',  'VIAB', 'XEC',  'XEL',  'BIDU', 'LEN',  'EBAY', 'MET',  'CHTR', 'USB',  'AZN',  'AZO',  'MSI',  'DISH', 'TWX',  'PCAR', 'TXN',  'DAL',  'HES',  'ORCL', 'TM',   'TD',   'PXD',  'AA',   'HOG',  'ESS',  'PKI',  'CNP',  'HON',  'ICE',  'AN',   'HOT',  'CNC',  'TROW', 'ISRG', 'PFE',  'PFG']

metrics = ['Vol', 'AvgVol', 'MktCap', 'P/E', 'Div', 'DivYield', 'EPS', 'Beta']
filename = 'Dividend'
output = open(filename, 'w')
output.write('Metrics,{}\n'.format(','.join(tickers)))
for metric in metrics:
    output.write(metric)
    output.write('\n')
output.close()

for ticker in tickers:
    size = len(ticker)
    if size <= 3:
        indexName = 'NYSE'
    if size > 3:
        indexName = 'NASDAQ'
    print ticker
    data= getRatios(ticker,indexName)
    
    
    



    
    ########################DATA COMING IN NICE AND GOOD###############################
    
    with open(filename, "r") as file:
        lines = file.readlines()
    file.close()
    
    lines = map(lambda s: s.strip(), lines)
    
 
    
    lines[0] = lines[0] + '\n'
    lines[1] = lines[1]+','+data[0] +'\n'
    lines[2] = lines[2]+','+data[1]+ '\n'
    lines[3] = lines[3]+','+data[2]+ '\n'
    lines[4] = lines[4]+','+data[3]+'\n'
    lines[5] = lines[5]+','+data[4]+'\n'
    lines[6] = lines[6]+','+data[5]+'\n'
    lines[7] = lines[7]+','+data[6]+'\n'
    lines[8] = lines[8]+','+data[7]+'\n'

    sizeLines = len(lines)
    

    output = open(filename, 'w')
    x = 0
    while x < sizeLines:
       
        output.write(lines[x])

        x += 1 

    output.close()




