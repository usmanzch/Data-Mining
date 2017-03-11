import urllib2
import datetime
import collections

# user input
start = '2005-01-01'
end   = '2016-08-10'

# start and end dates
start = datetime.datetime.strptime(start, '%Y-%m-%d')
end   = datetime.datetime.strptime(end, '%Y-%m-%d')

# List of 50 ETF (there's an excel spreadsheet in List_ETF.xlsx)
tickers = ['RY.to',	'TD.to',	'BNS.to',	'CNR.to',	'SU.to',	'BCE.to',	'BMO.to',	'ENB.to',	'TRP.to',	'CNQ.to',	'BAM-A.to',	'CM.to',	'ABX.to',	'CP.to',	'T.to',	'SLF.to',	'ATD-B.to',	'RCI-B.to',	'G.to',	'MG.to',	'FNV.to',	'WCN.to',	'POT.to',	'GIB-A.to',	'SLW.to',	'TRI.to',	'AEM.to',	'FFH.to',	'AGU.to',	'L.to',	'NA.to',	'PPL.to',	'QSR.to',	'IFC.to',	'FTS.to',	'MRU.to',	'DOL.to',	'CPG.to',	'SJR-B.to',	'VRX.to',	'IMO.to',	'CSU.to',	'POW.to',	'CTC-A.to',	'OTC.to',	'TCK-B.to',	'SAP.to',	'REI-UN.to',	'IPL.to',	'GWO.to',	'GIL.to',	'SNC.to',	'ARX.to',	'EMA.to',	'KEY.to',	'PWF.to',	'TOU.to',	'BPY-UN.to',	'HR-UN.to',	'THO.to',	'CCL-B.to',	'OCX.to',	'PEY.to',	'CIX.to',	'DGC.to',	'WN.to',	'ALA.to',	'VET.to',	'PSK.to',	'VII.to',	'IAG.to',	'CU.to',	'SRU-UN.to',	'H.to',	'BEP-UN.to',	'CAR-UN.to',	'RBA.to',	'PAA.to',	'FTT.to',	'FR.to',	'REF-UN.to',	'ACO-X.to',	'EMP-A.to',	'STN.to',	'QBR-B.to',	'MX.to',	'DH.to',	'CGX.to',	'IGM.to',	'ENF.to',	'MDA.to',	'CAD.to',	'AP-UN.to',	'WFT.to',	'WJA.to',	'TIH.to',	'MBT.to',	'WSP.to',	'NPI.to',	'BCB.to',	'FCR.to',	'MFI.to',	'LNR.to',	'PKI.to',	'AYA.to',	'TXG.to',	'TFI.to',	'FSV.to',	'CWB.to',	'BEI-UN.to',	'DSG.to',	'SJ.to',	'SCL.to',	'GRT-UN.to',	'CIG.to',	'CPX.to',	'HCG.to',	'NFI.to',	'PBH.to',	'MAG.to',	'CCA.to',	'LB.to',	'RUS.to',	'NWC.to',	'MST-UN.to',	'X.to',	'BYD-UN.to',	'EDV.to',	'MIC.to',	'OSB.to',	'WPK.to',	'CHE-U.to',	'UNS.to',	'KXS.to',	'ITP.to',	'NVU-UN.to',	'DII-B.to',	'ESL.to',	'AD.to',	'CXR.to',	'BAD.to',	'DOO.to',	'BNE.to',	'BBU-UN.to']
# loop over tickers to retrieve price data
adjCloses = collections.defaultdict(dict)
for ticker in tickers:
    print('retrieving daily ajdusted closes for {}... \n'.format(ticker))
    url = 'http://ichart.finance.yahoo.com/table.csv?s={}'.format(ticker)
    url += '&a={:02d}&b={:02d}&c={:02d}'.format(start.month-1, start.day, start.year)
    url += '&d={:02d}&e={:02d}&f={:02d}'.format(end.month-1, end.day, end.year)
    url += '&g=d&ignore=.csv'
    try:
        csv_handle = urllib2.urlopen(url)
    except:
        print('Unable to get data for {} from Yahoo, skipping...\n'.format(ticker))
        continue
    csv_handle.readline() #skip header
    for row in csv_handle:
        fields = row.strip().split(',')
        date = fields[0]
        adjClose = fields[-1]
        adjCloses[date][ticker] = adjClose

# output the data in a nicely formatted CSV file
output = open('TSX_ADJclose.csv', 'w')
output.write('date,{}\n'.format(','.join(tickers)))
for date in sorted(adjCloses.keys()):
    output.write('{},'.format(date))
    prices = [adjCloses[date].get(ticker, 'nan') for ticker in tickers]
    output.write('{}\n'.format(','.join(prices)))
print('Completed - find data in ETF_adjCloses.csv')