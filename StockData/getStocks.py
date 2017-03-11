import urllib2
import os
import datetime
import collections
import sys
import datetime
import time

# hardcoded index components
tickers = ['JDAS', 'JEF',  'JFBI', 'JHI',  'JJSF', 'JMP',  'JNJ',  'JRN',  'JWA',  'KBH',  'KBR',  'KDE',  'KDN',  'KEA',  'KEI',  'KEY',  'KEYN', 'KEYW', 'KF',   'KFED', 'KFFG', 'KFS',  'KLAC', 'KMB',  'KNBT', 'KNOL', 'KNOT', 'KNSY', 'KNX',  'KNXA', 'KO',   'KONA', 'KRNY', 'KTEC', 'KVHI', 'KWD',  'KZL',  'LABC', 'LAD',  'LANC', 'LBCP', 'LCRY', 'LECO', 'LEG',  'LEGC', 'LEH',  'LFUS', 'LLTC', 'LMT',  'LNCB', 'LOJN', 'LPNT', 'LSBI', 'LUM',  'LXP',  'LYBI', 'MAA',  'MAN',  'MAR',  'MAS',  'MASI', 'MATW', 'MATX', 'MBI',  'MBND', 'MBTF', 'MCBF', 'MCBK', 'MCHX', 'MCRI', 'MCRL', 'MCS',  'MDP',  'MDRX', 'MDST', 'MDT',  'MED',  'MEG',  'MENT', 'MERR', 'METR', 'MFA',  'MFBC', 'MFLO', 'MFLR', 'MFLX', 'MFSF', 'MFW',  'MGA',  'MGI',  'MGM',  'MGPI', 'MGRC', 'MHP',  'MI',   'MIGP', 'MIND', 'MITY', 'MLM',  'MM',   'MMA',  'MMU',  'MNK',  'MNT',  'MOD',  'MOS',  'MOV',  'MOVE', 'MPAC', 'MRTI', 'MS',   'MSBF', 'MSC',  'MSFG', 'MSI',  'MSM',  'MTB',  'MTN',  'MTRX', 'MTSC', 'MTXX', 'MXL',  'NAFC', 'NAHC', 'NAL',  'NATH', 'NBN',  'NBTB', 'NBTF', 'NCC',  'NCS',  'NCX',  'NDAQ', 'NDSN', 'NEBS', 'NEOG', 'NEWP', 'NFBK', 'NFG',  'NFP',  'NFS',  'NHTB', 'NHWK', 'NJR',  'NMIL', 'NNI',  'NOA',  'NOIZ', 'NOOF', 'NPBC', 'NRF',  'NSC',  'NSSC', 'NSTC', 'NTP',  'NTRS', 'NTY',  'NUAN', 'NUE',  'NUTR', 'NVSL', 'NWBI', 'NWE',  'NWFL', 'NXTY', 'NYM',  'OABC', 'OAKF', 'OC',   'OCAS', 'OCC',  'OCCF', 'OCFC', 'ODC',  'OICO', 'OII',  'OKE',  'OKSB', 'OLBK', 'OLN',  'ON',   'ONB',  'ONFC', 'OPHC', 'OPMR', 'OPNT', 'OPY',  'ORBK', 'ORIT', 'OSBK', 'OSIS', 'OVBC', 'PB',   'PBCI', 'PBCP', 'PBCT', 'PBF',  'PBG',  'PBHC', 'PBIP', 'PBNY', 'PCBS', 'PCTI', 'PDCO', 'PEBO', 'PEET', 'PETD', 'PFB',  'PFBC', 'PFDC', 'PFIN', 'PFS',  'PGI',  'PGR',  'PH',   'PII',  'PKBK', 'PKE',  'PKI',  'PKOH', 'PKY',  'PKZ',  'PLBC', 'PLCE', 'PLPC', 'PLT',  'PLUS', 'PLXT', 'PMRY', 'PMTI', 'PNBK', 'PNC',  'PNRG', 'PNY',  'POL',  'PPBI', 'PPD',  'PPO',  'PRE',  'PRI',  'PROV', 'PRSS', 'PRTR', 'PRWT', 'PSEM', 'PSSI', 'PSTA', 'PSTB', 'PTNR', 'PTP',  'PTSI', 'PTV',  'PVSA', 'PWER', 'QADA', 'QCOR', 'QSCG', 'QUOT', 'RAH',  'RBA',  'RBN',  'RBPAA',    'RCKB', 'RDN',  'RE',   'RENT', 'REXI', 'RF',   'RFIL', 'RGA',  'RGEN', 'RHI',  'RIMG', 'RIMM', 'RJET', 'RLI',  'RLRN', 'RMBS', 'RMCF', 'RMD',  'RMIX', 'RNT',  'ROFO', 'ROL',  'ROMA', 'ROME', 'RPFG', 'RRD',  'RRST', 'RS',   'RSC',  'RSH',  'RSO',  'RX',   'SAF',  'SAFM', 'SAR',  'SASR', 'SBBX', 'SBIB', 'SBSI', 'SBY',  'SEE',  'SEH',  'SENEA',    'SERO', 'SF',   'SFBC', 'SFD',  'SFG',  'SFL',  'SFN',  'SFUN', 'SGK',  'SHLM', 'SHRP', 'SIFI', 'SIGM', 'SII',  'SINO', 'SINT', 'SJI',  'SJM',  'SKIL', 'SKYW', 'SLE',  'SLI',  'SLM',  'SM',   'SMCI', 'SMHG', 'SMP',  'SMPL', 'SMSC', 'SNBC', 'SNI',  'SOCB', 'SOLR', 'SOMH', 'SON',  'SONC', 'SONE', 'SOV',  'SPAN', 'SPAR', 'SRCE', 'SRSL', 'SSS',  'STBZ', 'STE',  'STEI', 'STEL', 'STEN', 'STFC', 'STI',  'STLD', 'STMP', 'STND', 'STRT', 'STRZ', 'STT',  'SUN',  'SURW', 'SVLF', 'SVVC', 'SWIR', 'SWZ',  'SYA',  'SYKE', 'SYMM', 'SYNF', 'SYNL', 'SYNO', 'SYX',  'T',    'TAC',  'TACT', 'TAL',  'TALX', 'TBNK', 'TDY',  'TEAM', 'TESS', 'TFC',  'TFSL', 'TG',   'TGI',  'THC',  'THFF', 'THO',  'THRD', 'TIN',  'TKR',  'TLAB', 'TLGD', 'TLMR', 'TNB',  'TNC',  'TOBC', 'TOFC', 'TOL',  'TRA',  'TRB',  'TRI',  'TRNO', 'TROW', 'TRUE', 'TSBK', 'TSRI', 'TSS',  'TSTY', 'TTWO', 'TWIN', 'TWP',  'TXT',  'TYL',  'TZOO', 'UACL', 'UAM',  'UBCD', 'UBFO', 'UBMT', 'UBNK', 'UBSI', 'UCBA', 'UCFC', 'UDR',  'UHS',  'ULBI', 'ULTI', 'UMBF', 'UMPQ', 'UNAM', 'UNH',  'UNP',  'URBN', 'URS',  'USAK', 'USBI', 'USMO', 'USPH', 'UTHR', 'UTMD', 'UTSI', 'UTX',  'UVSP', 'VAL',  'VAR',  'VCI',  'VCLK', 'VFC',  'VHI',  'VIDE', 'VNTV', 'VOL',  'VPFG', 'VPG',  'VRGY', 'VRX',  'VSBN', 'VTAL', 'VTNC', 'VVI',  'WABC', 'WAIN', 'WAUW', 'WAYN', 'WB',   'WBCO', 'WBKC', 'WBMD', 'WBS',  'WCBO', 'WCI',  'WD',   'WEA',  'WEDC', 'WEST', 'WFBC', 'WFC',  'WFD',  'WIBC', 'WINA', 'WIRE', 'WLFC', 'WM',   'WOR',  'WPO',  'WPP',  'WRB',  'WRC',  'WRK',  'WSBC', 'WSFS', 'WSM',  'WTBA', 'WTFC', 'WTNY', 'WTS',  'WWW',  'WY',   'X',    'XRAY', 'YDNT', 'YORW', 'YSI',  'ZBRA', 'ZEUS', 'ZIPR']
# start and end dates
startDate = 'Jan 1, 2005'
endDate  = ''  # 'Jul 10, 2009'

startDate = startDate.replace (" ", "%20")

endDate = endDate.replace (" ", "%20")


# loop over tickers to retrieve price data
adjCloses = collections.defaultdict(dict)
dailyOpens = collections.defaultdict(dict)
dailyCloses = collections.defaultdict(dict)
dailyHighs= collections.defaultdict(dict)
dailyLows = collections.defaultdict(dict)

etf = 0;
for ticker in tickers:
    print('retrieving daily data for {}... \n'.format(ticker))
   

    
    try: 
        indexName = 'NYSE'
        if '.to' in ticker:
            indexName = 'TSE'
            ticker = ticker.replace('.to','')
            print ticker
            print indexName
        if etf == 1:
            indexName = 'NYSEARCA'
            etf = 0;

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
            dailyLows[date][ticker] = dailyLow
            dailyOpens[date][ticker] = dailyOpen
            dailyCloses[date][ticker] = dailyClose
            
        except:
            continue

    os.remove(ticker)
# output the data in a nicely formatted CSV file
indexName = "repurchase_stocks2"
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
print('Completed - find data in {}'.format(filename))