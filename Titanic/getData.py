import urllib2
import os
import datetime
import collections
import sys
import datetime
import time

# hardcoded index components
tickers = ['XOM','JNJ','GE','T','WFC','JPM','CHL','WMT','PG','VZ','PFE','F','KO','CVX','NVS','BABA','V','FMX','ORCL','HD','DIS','MS','PM','TM','UBS','PEP','IBM','NVO','BAC','UL','UN','TSM','UNH','RIO','C','HSBC','BMY','TOT','MCD','MA','CVS','SNY','MMM','DCM','BP','GSK','ABBV','TJX','SAP','AGN','NKE','UPS','RY','NTT','HON','UTX','ABEV','SNP','BA','TD','LLY','ACN','UNP','LMT','RAI','USB','DEO','AZN','D','LOW','LYG','DHR','MTU','CL','BBL','CAJ','SAN','GS','SPG','AXP','AIG','BNS','LFC','BT','DOW','TMO','DD','EPD','CB','TWX','OXY','NEE','BLK','E','ABT','DUK','NGG','CRM','COP','EMC', #NYSE
           'RY', 'TD', 'BNS', 'CNI', 'SU', 'BCE', 'BMO', 'ENB', 'TRP', 'CNQ', 'BAM', 'CM', 'MFC', 'ABX', 'SLF', 'TU', 'CP', 'GG', 'RCI', 'MGA', 'POT', 'FNV', 'TRI', 'AGU', 'AEM', 'CVE', 'PBA', 'GIB', 'SLW', 'QSR', 'IMO', 'CPG', 'SJR', 'GIL', 'ECA', 'VRX', 'TCK', 'KGC', 'AUY', 'CCJ', 'EGO','BBRY',#TSX in US markets
           'YHOO',	'MXIM',	'NCLH',	'MDLZ',	'SRCL',	'TSCO',	'DISH',	'AMZN',	'ALXN',	'BMRN',	'ENDP',	'GOOG',	'CHTR',	'CSCO',	'INTC',	'MSFT',	'NVDA',	'CTSH',	'ISRG',	'EBAY',	'INCY',	'PCLN',	'ILMN',	'AKAM',	'JD',	'TXN',	'KHC',	'BATRA',	'BATRK',	'GOOGL',	'NFLX',	'WDC',	'ADP',	'LMCA',	'LMCK',	'WBA',	'STX',	'ADBE',	'AMGN',	'CSX',	'AAPL',	'ADSK',	'DISCK',	'CMCSA',	'LBTYK',	'AVGO',	'CA',	'PCAR',	'QVCA',	'COST',	'REGN',	'SWKS',	'ATVI',	'AMAT',	'BBBY',	'CELG',	'EXPE',	'CERN',	'NTES',	'DISCA',	'AAL',	'VIAB',	'FOX',	'EA',	'ESRX',	'ULTA',	'FAST',	'HSIC',	'TRIP',	'FISV',	'FB',	'GILD',	'BIIB',	'LRCX',	'LLTC',	'SBAC',	'VRTX',	'PAYX',	'ADI',	'PYPL',	'QCOM',	'MAR',	'ROST',	'SBUX',	'VOD',	'SYMC',	'WFM',	'XLNX',	'INTU',	'MNST',	'ORLY',	'CHKP',	'TSLA',	'CTRP',	'LVNTA',	'NXPI',	'MAT',	'SIRI',	'MU',	'BIDU',	'MYL',	'TMUS',	'VRSK',	'DLTR',	'FOXA',	'NTAP',	'CTXS',	'LBTYA', #Nasdaq 100
           'ABT','ABBV','ACN','ATVI','AYI','ADBE','AAP','AES','AET','AFL','AMG','A','GAS',
    'APD','AKAM','ALK','AA','AGN','ALXN','ALLE','ADS','ALL','GOOGL','GOOG','MO','AMZN',
    'AEE','AAL','AEP','AXP','AIG','AMT','AWK','AMP','ABC','AME','AMGN','APH','APC','ADI',
    'AON','APA','AIV','AAPL','AMAT','ADM','AJG','AIZ','T','ADSK','ADP','AN','AZO','AVGO',
    'AVB','AVY','BHI','BLL','BAC','BK','BCR','BXLT','BAX','BBT','BDX','BBBY','BRK-B','BBY',
    'BIIB','BLK','HRB','BA','BWA','BXP','BSX','BMY','BF-B','CHRW','CA','CVC','COG','CPB',
    'COF','CAH','HSIC','KMX','CCL','CAT','CBG','CBS','CELG','CNC','CNP','CTL','CERN','CF',
    'SCHW','CHK','CVX','CMG','CB','CHD','CI','XEC','CINF','CTAS','CSCO','C','CTXS','CLX',
    'CME','CMS','COH','KO','CTSH','CL','CPGX','CMCSA','CMA','CAG','CXO','COP','ED','STZ',
    'GLW','COST','CCI','CSRA','CSX','CMI','CVS','DHI','DHR','DRI','DVA','DE','DLPH','DAL',
    'XRAY','DVN','DO','DLR','DFS','DISCA','DISCK','DG','DLTR','D','DOV','DOW','DPS','DTE',
    'DD','DUK','DNB','ETFC','EMN','ETN','EBAY','ECL','EIX','EW','EA','EMC','EMR','ENDP',
    'ETR','EOG','EQT','EFX','EQIX','EQR','ESS','EL','ES','EXC','EXPE','EXPD','ESRX','EXR',
    'XOM','FFIV','FB','FAST','FRT','FDX','FIS','FITB','FSLR','FE','FISV','FLIR','FLS','FLR',
    'FMC','FTI','FL','F','BEN','FCX','FTR','GPS','GRMN','GD','GE','GGP','GIS','GM','GPC',
    'GILD','GPN','GS','GT','GWW','HAL','HBI','HOG','HAR','HRS','HIG','HAS','HCA','HCP','HP',
    'HES','HPE','HOLX','HD','HON','HRL','HST','HPQ','HUM','HBAN','ITW','ILMN','IR','INTC',
    'ICE','IBM','IP','IPG','IFF','INTU','ISRG','IVZ','IRM','JEC','JBHT','JNJ','JCI','JPM',
    'JNPR','KSU','K','KEY','KMB','KIM','KMI','KLAC','KSS','KHC','KR','LB','LLL','LH','LRCX',
    'LM','LEG','LEN','LVLT','LUK','LLY','LNC','LLTC','LKQ','LMT','L','LOW','LYB','MTB','MAC',
    'M','MNK','MRO','MPC','MAR','MMC','MLM','MAS','MA','MAT','MKC','MCD','MCK','MJN','WRK',
    'MDT','MRK','MET','KORS','MCHP','MU','MSFT','MHK','TAP','MDLZ','MON','MNST','MCO','MS',
    'MOS','MSI','MUR','MYL','NDAQ','NOV','NAVI','NTAP','NFLX','NWL','NFX','NEM','NWSA','NWS',
    'NEE','NLSN','NKE','NI','NBL','JWN','NSC','NTRS','NOC','NRG','NUE','NVDA','ORLY','OXY',
    'OMC','OKE','ONEOK','ORCL','OI','PCAR','PH','PDCO','PAYX','PYPL','PNR','PBCT','PEP','PKI',
    'PRGO','PFE','PCG','PM','PSX','PNW','PXD','PBI','PNC','RL','PPG','PPL','PX','CFG','PCLN',
    'PFG','PG','PGR','PLD','PRU','PEG','PSA','PHM','PVH','QRVO','PWR','QCOM','DGX','RRC','RTN',
    'O','RHT','REGN','RF','RSG','RAI','RHI','ROK','COL','ROP','ROST','RCL','R','CRM','SCG','SLB',
    'SNI','STX','SEE','SRE','SHW','SIG','SPG','SWKS','SLG','SJM','SNA','SO','LUV','SWN','SE',
    'SPGI','STJ','SWK','SPLS','SBUX','HOT','STT','SRCL','SYK','STI','SYMC','SYF','SYY','TROW',
    'TGT','TEL','TE','TGNA','TDC','TSO','TXN','TXT','HSY','TRV','TMO','TIF','TWX','TJX','TMK',
    'TSS','TSCO','RIG','TRIP','FOXA','FOX','TSN','TYC','UDR','ULTA','USB','UA','UNP','UAL','UNH',
    'UPS','URI','UTX','UHS','UNM','URBN','VFC','VLO','VAR','VTR','VRSN','VRSK','VZ','VRTX','VIAB',
    'V','VNO','VMC','WMT','WBA','DIS','WM','WAT','ANTM','WFC','HCN','WDC','WU','WY','WHR','WFM',
    'WMB','WLTW','WEC','WYN','WYNN','XEL','XRX','XLNX','XL','XYL','YHOO','YUM','ZBH','ZION','ZTS'] #s&p 500 


tickers = list(set(tickers)) # get unique elements in list
# start and end dates
startDate = 'Jan 1, 2016'
endDate  = ''  # 'Jul 10, 2009'

startDate = startDate.replace (" ", "%20")

endDate = endDate.replace (" ", "%20")


# loop over tickers to retrieve price data
adjCloses = collections.defaultdict(dict)
dailyOpens = collections.defaultdict(dict)
dailyCloses = collections.defaultdict(dict)
dailyHighs= collections.defaultdict(dict)
dailyLows = collections.defaultdict(dict)

for ticker in tickers:
    print('retrieving daily data for {}... \n'.format(ticker))
   

   
    try: 
        indexName = 'NYSE'
        url = "http://www.google.com/finance/historical?q="+str(indexName)+"%3A"+str(ticker)+"&startdate="+str(startDate)+"&enddate="+str(endDate)+"&output=csv"
        f = urllib2.urlopen(url)
        data = f.read()
        with open(ticker, "wb") as code:
            code.write(data)
     

    except:
        try:
            indexName = 'NASDAQ'
            url = "http://www.google.com/finance/historical?q="+str(indexName)+"%3A"+str(ticker)+"&startdate="+str(startDate)+"&enddate="+str(endDate)+"&output=csv"
            f = urllib2.urlopen(url)
            data = f.read()
            with open(ticker, "wb") as code:
                code.write(data)
        except:  
            print('Unable to get data for {} from google, skipping...\n'.format(ticker))
            continue
    


    with open(ticker, 'r')as final:
        csv_handle = final.readlines()[::-1]

    del csv_handle[-1]
   
    for row in csv_handle:
       
        fields = row.strip().split(',')

        datefields = fields[0].strip().split('-')
        try:
            datestr = datefields[2]+"/"+datefields[1]+"/"+datefields[0]
            
            datefinal = datetime.datetime.strptime(datestr, '%y/%b/%d').strftime('%y/%m/%d')

            
            date = datefinal
            dailyOpen = fields[1]
            dailyHigh = fields[2]
            dailyLow = fields[3]
            dailyClose = fields[4]

            dailyHighs[date][ticker] = dailyHigh
            dailyLows[date][ticker] = dailyClose
            dailyOpens[date][ticker] = dailyOpen
            dailyCloses[date][ticker] = dailyClose
            
        except:
            continue

    os.remove(ticker)
# output the data in a nicely formatted CSV file
indexName = "TITANIC"
if os.path.isdir(indexName) == False:
    os.makedirs(indexName)
os.chdir(indexName)


filename = indexName+'_Open.csv'
output = open(filename, 'w')
output.write('date,{}\n'.format(','.join(tickers)))
for date in sorted(dailyOpens.keys()):

    cleanDate = datetime.datetime.strptime(date, '%y/%m/%d').strftime('%m/%d/%Y')

    output.write('{},'.format(cleanDate))
    prices = [dailyOpens[date].get(ticker, 'nan') for ticker in tickers]
    for position,price in enumerate(prices):
        if price == '-':
            prices[position] = 'nan'
    
    output.write('{}\n'.format(','.join(prices)))
output.write('\n');
print('Completed - find data in {}'.format(filename))

filename = indexName+'_Close.csv'
output = open(filename, 'w')
output.write('date,{}\n'.format(','.join(tickers)))
for date in sorted(dailyCloses.keys()):
    cleanDate = datetime.datetime.strptime(date, '%y/%m/%d').strftime('%m/%d/%Y')
    output.write('{},'.format(cleanDate))
    prices = [dailyCloses[date].get(ticker, 'nan') for ticker in tickers]
    for position,price in enumerate(prices):
        if price == '-':
            prices[position] = 'nan'
    output.write('{}\n'.format(','.join(prices)))
output.write('\n');
print('Completed - find data in {}'.format(filename))

filename = indexName+'_High.csv'
output = open(filename, 'w')
output.write('date,{}\n'.format(','.join(tickers)))
for date in sorted(dailyHighs.keys()):
    cleanDate = datetime.datetime.strptime(date, '%y/%m/%d').strftime('%m/%d/%Y')
    output.write('{},'.format(cleanDate))
    prices = [dailyHighs[date].get(ticker, 'nan') for ticker in tickers]
    for position,price in enumerate(prices):
        if price == '-':
            prices[position] = 'nan'
    output.write('{}\n'.format(','.join(prices)))
output.write('\n');
print('Completed - find data in {}'.format(filename))

filename = indexName+'_Low.csv'
output = open(filename, 'w')
output.write('date,{}\n'.format(','.join(tickers)))
for date in sorted(dailyLows.keys()):
    cleanDate = datetime.datetime.strptime(date, '%y/%m/%d').strftime('%m/%d/%Y')
    output.write('{},'.format(cleanDate))
    prices = [dailyLows[date].get(ticker, 'nan') for ticker in tickers]
    for position,price in enumerate(prices):
        if price == '-':
            prices[position] = 'nan'
    output.write('{}\n'.format(','.join(prices)))
output.write('\n');
print('Completed - find data in {}'.format(filename))
