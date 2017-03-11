import urllib2
import datetime
import json
import sys
import time
import threading

global dictionary
dictionary = {}

# hardcoded index components


def fetchMarket(symbol,  position):

    try:
        exchange = 'NYSE'
        link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
        url = link+"%s:%s" % (exchange, symbol)
        u = urllib2.urlopen(url)
    except:
        try:
            exchange = 'NASDAQ'
            link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
            url = link+"%s:%s" % (exchange, symbol)
            u = urllib2.urlopen(url)
            
        except:
            print("Could not find stock "+str(symbol)+" on exchange "+str(exchange))
            
    content = u.read()
    data = json.loads(content[3:])

    info = data[0]

    l = str(info['op'])    # market price 

    dictionary[position] = l



symbols = ['UTX',   'AGN',  'EOG',  'CPB',  'CPG',  'QRVO', 'JWN',  'SBAC', 'JBHT', 'AGU',  'NXPI', 'WAT',  'TAP',  'VRTX', 'BWA',  'UAL',  'WM',   'SPG',  'ENDP', 'GT',   'GS',   'PYPL', 'MJN',  'WRK',  'GG',   'ROP',  'GE',   'GD',   'GIB',  'VAR',  'AMZN', 'GIL',  'BRK-B',    'MAS',  'MAR',  'MAT',  'SNA',  'FOXA', 'SNI',  'XRAY', 'MAC',  'SNP',  'JNJ',  'XYL',  'SNY',  'TSN',  'AFL',  'TSM',  'BEN',  'CMI',  'EL',   'CMG',  'CME',  'CHKP', 'PAYX', 'CMA',  'CMS',  'PCG',  'VLO',  'HUM',  'PCLN', 'TGNA', 'FSLR', 'BABA', 'GRMN', 'FTR',  'K',    'FFIV', 'BLL',  'HCA',  'BLK',  'FTI',  'HCN',  'SIG',  'NFX',  'MA',   'CBG',  'PRGO', 'MO',   'NOC',  'MU',   'CBS',  'HAR',  'SE',   'MS',   'TJX',  'NOV',  'TIF',  'AMGN', 'FB',   'COST', 'FE',   'YHOO', 'CTL',  'DPS',  'DOV',  'DOW',  'MSFT', 'GLW',  'SCHW', 'BSX',  'GGP',  'LFC',  'FCX',  'BDX',  'WHR',  'BBBY', 'MDT',  'HIG',  'FMX',  'F',    'DFS',  'JEC',  'ILMN', 'TOT',  'V',    'AUY',  'FMC',  'MPC',  'TSCO', 'ALL',  'ALK',  'LMT',  'NTT',  'SU',   'MMM',  'SO',   'JNPR', 'MMC',  'LOW',  'WEC',  'ADBE', 'IBM',  'FIS',  'BAX',  'CAT',  'CAJ',  'CAH',  'BAC',  'GIS',  'BAM',  'CAG',  'URI',  'LB',   'MDLZ', 'INCY', 'LM',   'LH',   'PGR',  'BATRA',    'CELG', 'BATRK',    'WLTW', 'A',    'ABC',  'ZION', 'STI',  'STJ',  'STT',  'ABT',  'ABX',  'XOM',  'STX',  'STZ',  'BHI',  'NTAP', 'CERN', 'NCLH', 'PNR',  'PNW',  'ONEOK',    'IVZ',  'PNC',  'FNV',  'GOOGL',    'VFC',  'EIX',  'BXLT', 'EGO',  'GM',   'SAN',  'LMCK', 'AON',  'RY',   'RAI',  'PRU',  'RF',   'RL',   'SAP',  'CHD',  'URBN', 'CHK',  'CHL',  'L',    'HRS',  'HRL',  'MRO',  'MRK',  'HRB',  'IPG',  'NLSN', 'NTES', 'RHT',  'TYC',  'RHI',  'APH',  'ROST', 'APC',  'APA',  'APD',  'ABEV', 'SRE',  'NGG',  'KSS',  'WFM',  'WFC',  'IFF',  'BMRN', 'NVDA', 'KORS', 'AVGO', 'RTN',  'BMO',  'BMY',  'SYMC', 'DISCA',    'ENB',  'OXY',  'SHW',  'ED',   'DISCK',    'EA',   'ORLY', 'DLR',  'CSX',  'TMK',  'EW',   'EQIX', 'ES',   'ANTM', 'MGA',  'LUV',  'MUR',  'WYN',  'LUK',  'ADSK', 'ECA',  'ECL',  'SEE',  'PVH',  'DGX',  'NUE',  'EXPE', 'EXPD', 'UNP',  'UDR',  'ETFC', 'BBL',  'XL',   'IMO',  'R',    'CLX',  'DTE',  'BBY',  'FRT',  'UNH',  'BBT',  'TRIP', 'OMC',  'KO',   'VMC',  'HSBC', 'KR',   'LNC',  'KEY',  'CFG',  'CPGX', 'AEE',  'KLAC', 'BF-B', 'SWK',  'RSG',  'WYNN', 'LBTYA',    'TSLA', 'SWN',  'AAL',  'DD',   'DE',   'LBTYK',    'DUK',  'AAP',  'WBA',  'TGT',  'HBAN', 'POT',  'TSS',  'GILD', 'ATVI', 'AKAM', 'DHI',  'HOLX', 'SLW',  'M',    'MLM',  'INTU', 'ALXN', 'SLF',  'SLG',  'DHR',  'SLB',  'AJG',  'MCO',  'JPM',  'MCD',  'NRG',  'PBCT', 'QSR',  'VTR',  'AXP',  'NFLX', 'EXC',  'AAPL', 'SRCL', 'WU',   'EXR',  'JD',   'WY',   'DCM',  'VNO',  'UNM',  'RIO',  'SPLS', 'AWK',  'HST',  'RIG',  'HSY',  'DLPH', 'TCK',  'CTSH', 'GPN',  'HAL',  'BNS',  'FITB', 'EQR',  'EQT',  'GPC',  'XLNX', 'HAS',  'PH',   'LVLT', 'GPS',  'DRI',  'YUM',  'SYF',  'PHM',  'SYK',  'LEG',  'KIM',  'CCI',  'SYY',  'AEP',  'AES',  'AET',  'EMC',  'EMN',  'HCP',  'ESRX', 'AMAT', 'SWKS', 'CTAS', 'EMR',  'FDX',  'AEM',  'EPD',  'CRM',  'MFC',  'TSO',  'NWSA', 'PX',   'PG',   'CTXS', 'PM',   'EFX',  'C',    'TMUS', 'SIRI', 'FOX',  'QCOM', 'XRX',  'ITW',  'ULTA', 'NVS',  'MOS',  'PSA',  'PSX',  'MON',  'NVO',  'ETR',  'COP',  'HES',  'DVN',  'KMB',  'DO',   'BCE',  'PEP',  'KMI',  'LMCA', 'GWW',  'FISV', 'COG',  'COF',  'COH',  'PEG',  'ETN',  'COL',  'BCR',  'KMX',  'DLTR', 'VRX',  'ZBH',  'DG',   'CI',   'CM',   'CL',   'CB',   'CA',   'CF',   'CP',   'ZTS',  'CHRW', 'TDC',  'SBUX', 'PLD',  'CMCSA',    'MKC',  'PDCO', 'CVX',  'AIZ',  'BXP',  'AIV',  'CVS',  'RCL',  'RCI',  'AYI',  'AIG',  'CVE',  'CVC',  'DIS',  'PPG',  'MNST', 'NSC',  'GAS',  'PPL',  'NDAQ', 'UHS',  'GOOG', 'BBRY', 'IP',   'HPQ',  'IR',   'MTU',  'MCHP', 'IRM',  'MTB',  'VZ',   'JCI',  'HPE',  'PWR',  'OKE',  'CSCO', 'BIIB', 'WDC',  'HBI',  'BA',   'BK',   'BT',   'CCL',  'BP',   'CCJ',  'GSK',  'CTRP', 'ALLE', 'FLIR', 'LYG',  'MYL',  'LYB',  'KHC',  'HSIC', 'D',    'NAVI', 'DVA',  'WMT',  'VRSN', 'T',    'WMB',  'TXT',  'OI',   'VRSK', 'UBS',  'CINF', 'NTRS', 'CXO',  'FLS',  'FLR',  'REGN', 'DEO',  'ESS',  'HD',   'LKQ',  'LLY',  'ROK',  'INTC', 'NWS',  'FL',   'SCG',  'AME',  'AMG',  'MNK',  'LLL',  'NWL',  'AMP',  'TMO',  'AMT',  'LRCX', 'TRI',  'MHK',  'O',    'LVNTA',    'PBA',  'TRP',  'PBI',  'UPS',  'TRV',  'VOD',  'AVY',  'ABBV', 'UL',   'UN',   'UA',   'AVB',  'KSU',  'NEM',  'NEE',  'ACN',  'NI',   'TEL',  'RRC',  'FAST', 'NBL',  'HP',   'QVCA', 'LLTC', 'ADS',  'ADP',  'DNB',  'SJR',  'SJM',  'MCK',  'ADM',  'ADI',  'VIAB', 'XEC',  'XEL',  'BIDU', 'LEN',  'EBAY', 'MET',  'CHTR', 'USB',  'AZN',  'AZO',  'MXIM', 'MSI',  'DISH', 'TWX',  'PCAR', 'TXN',  'DAL',  'TU',   'ORCL', 'TM',   'TD',   'TE',   'PXD',  'AA',   'HOG',  'E',    'PKI',  'CNP',  'CNQ',  'HON',  'ICE',  'AN',   'CSRA', 'HOT',  'CNC',  'TROW', 'ISRG', 'CNI',  'PFE',  'NKE',  'PFG',  'KGC',  'SPGI']


filename = 'TITANIC/TITANIC_Open.csv'

currDate = datetime.datetime.now().strftime('%m-%d-%Y') # left off here

lines = open(filename, 'r').readlines() 
del lines[-1] 
open(filename, 'w').writelines(lines) 

with open(filename, 'a+') as file:
    file.write(currDate)
    file.write(",")

threads = []
for position,symbol in enumerate(symbols):

    thread = threading.Thread(target=fetchMarket,args=(symbol, position))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

with open(filename, 'a+') as file:
    for num in range(0,len(symbols)):
        file.write(dictionary[num]) 
        file.write(",")

        

   