import urllib2
import datetime
import collections


# user input
start = '2000-01-01'

today = datetime.datetime.now().strftime('%Y-%m-%d')

end   =  today

# start and end dates
start = datetime.datetime.strptime(start, '%Y-%m-%d')

end   = datetime.datetime.strptime(end, '%Y-%m-%d')

# hardcoded FX pairs
tickers = ['^GSPC', '^GSPTSE', '^FTSE', '^GDAXI', '^FCHI', '^N225', '^HSI','^IRX']

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
output = open('Index_adjCloses.csv', 'w')
output.write('date,{}\n'.format(','.join(tickers)))
for date in sorted(adjCloses.keys()):
    output.write('{},'.format(date))
    prices = [adjCloses[date].get(ticker, 'nan') for ticker in tickers]
    output.write('{}\n'.format(','.join(prices)))
print('Completed - find data in Index_adjCloses.csv')