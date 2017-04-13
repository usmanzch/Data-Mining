clc;clear;


addpath(genpath('C:\Users\usman\OneDrive\Hedge\1minData'));

[status_getfiles,output] = system('C:\Python27\python.exe "C:\Users\usman\OneDrive\Hedge\1minData\getGoogleData_1min.py" SPY A AAP AAPL AAXJ ABBV ABC ABT ACN ACWI ADBE ADI ADM ADP ADS ADSK AEE AEM AEP AER AET AFL AGN AGU AIG AIV AKAM ALB ALGN ALK ALL ALXN AMBA AME AMGN AMP AMSG AMZN ANET ANTM APA APC APD APH ASML ATVI AVB AVGO AWK AXP BA BABA BAX BBBY BDX BERY BG BHI BIDU BIIB BK BLL BLUE BMRN BMY BRK.B BUD BURL BXP C CAG CAH CAT CAVM CB CBS CCL CE CELG CERN CHD CHKP CHRW CHTR CI CL CLR CLX CMA CMCSA CME CMG CMI CMS CNC COF COL CONE COP COST CP CPB CRI CRM CSC CTRP CTSH CTXS CVS CVX CXO D DATA DD DE DFS DG DGX DHR DIS DISH DKS DLPH DLR DLTR DNKN DOV DOW DPS DRI DTE DUK DVA DVMT DVN DXCM DY EA EAT ECL ED EDU EGN EIX EL EMN EMR ENB EOG EQR EQT ES ESRX ETN ETR EW EXPD EXPE EXR FANG FAST FB FBHS FDX FFIV FIS FISV FL FLR FLT FTV GD GILD GIS GOOG GPN GRMN GRUB GS GSK GWPH HAL HAR HAS HCA HCN HD HES HIG HLF HOG HON HP HRS HSIC HSY IBB IBM ILMN INCY INTU IP IR ITW JAZZ JBHT JNJ JPM JWN K KHC KLAC KMB KMX KO KORS KSS KSU LB LBRDK LDOS LEA LEN LH LLTC LLY LMT LN LNC LNG LNKD LOW LRCX LULU LVLT LVS LYB MA MAA MAC MAN MAR MBLY MCD MCHI MCHP MCK MCO MDLZ MET MJN MMC MMM MNK MNST MO MON MPC MRK MSFT MSI MTB NEE NEM NFLX NFX NKE NLSN NOC NOW NSC NTES NTRS NUE NVDA NVO NVS NWL NXPI O OC OKE OMC ORCL OXY PAG PANW PAYX PCAR PCG PDCE PEG PEP PF PFG PG PH PII PKG PLD PM PNC PNR POST PPG PPS PRGO PRU PSA PSX PVH PX PXD Q QRVO RAI RCL RDS.A RDS.B RDUS REGN RGLD RHT RL RMD ROK ROST RRC RSG RTN RY SAP SBAC SBUX SE SEE SHPG SHW SIG SINA SIX SJM SLB SLCA SLG SNI SO SPG SPGI SPLK SPR SRCL SRE STI STJ STT STZ SWK SWKS SYK SYY T TAP TD TEL TEVA TGT THS TIF TJX TMO TMUS TOT TPX TRGP TRIP TROW TRV TSCO TSLA TSN TSO TSRO TSS TTM TTWO TWLO TWX TXN UAL UHS UL ULTA UN UNH UNP UPS URI USB UTX V VAR VCIT VFC VLO VMC VMW VNO VNTV VRSK VRSN VRTX VTR VZ WAB WB WBA WCN WDAY WDC WEC WFC WHR WLK WLTW WM WMT WRK WSM WUBA WWAV WYN WYNN XEC XEL XLNX XOM XRAY XYL YHOO YUM YY ZBH ZTS');
disp('Downloading 1 min files...');

tickers = {'SPY','A',	'AAP',	'AAPL',	'AAXJ',	'ABBV',	'ABC',	'ABT',	'ACN',	'ACWI',	'ADBE',	'ADI',	'ADM',	'ADP',	'ADS',	'ADSK',	'AEE',	'AEM',	'AEP',	'AER',	'AET',	'AFL',	'AGN',	'AGU',	'AIG',	'AIV',	'AKAM',	'ALB',	'ALGN',	'ALK',	'ALL',	'ALXN',	'AMBA',	'AME',	'AMGN',	'AMP',	'AMSG',	'AMZN',	'ANET',	'ANTM',	'APA',	'APC',	'APD',	'APH',	'ASML',	'ATVI',	'AVB',	'AVGO',	'AWK',	'AXP',	'BA',	'BABA',	'BAX',	'BBBY',	'BDX',	'BERY',	'BG',	'BHI',	'BIDU',	'BIIB',	'BK',	'BLL',	'BLUE',	'BMRN',	'BMY',	'BRK.B',	'BUD',	'BURL',	'BXP',	'C',	'CAG',	'CAH',	'CAT',	'CAVM',	'CB',	'CBS',	'CCL',	'CE',	'CELG',	'CERN',	'CHD',	'CHKP',	'CHRW',	'CHTR',	'CI',	'CL',	'CLR',	'CLX',	'CMA',	'CMCSA',	'CME',	'CMG',	'CMI',	'CMS',	'CNC',	'COF',	'COL',	'CONE',	'COP',	'COST',	'CP',	'CPB',	'CRI',	'CRM',	'CSC',	'CTRP',	'CTSH',	'CTXS',	'CVS',	'CVX',	'CXO',	'D',	'DATA',	'DD',	'DE',	'DFS',	'DG',	'DGX',	'DHR',	'DIS',	'DISH',	'DKS',	'DLPH',	'DLR',	'DLTR',	'DNKN',	'DOV',	'DOW',	'DPS',	'DRI',	'DTE',	'DUK',	'DVA',	'DVMT',	'DVN',	'DXCM',	'DY',	'EA',	'EAT',	'ECL',	'ED',	'EDU',	'EGN',	'EIX',	'EL',	'EMN',	'EMR',	'ENB',	'EOG',	'EQR',	'EQT',	'ES',	'ESRX',	'ETN',	'ETR',	'EW',	'EXPD',	'EXPE',	'EXR',	'FANG',	'FAST',	'FB',	'FBHS',	'FDX',	'FFIV',	'FIS',	'FISV',	'FL',	'FLR',	'FLT',	'FTV',	'GD',	'GILD',	'GIS',	'GOOG',	'GPN',	'GRMN',	'GRUB',	'GS',	'GSK',	'GWPH',	'HAL',	'HAR',	'HAS',	'HCA',	'HCN',	'HD',	'HES',	'HIG',	'HLF',	'HOG',	'HON',	'HP',	'HRS',	'HSIC',	'HSY',	'IBB',	'IBM',	'ILMN',	'INCY',	'INTU',	'IP',	'IR',	'ITW',	'JAZZ',	'JBHT',	'JNJ',	'JPM',	'JWN',	'K',	'KHC',	'KLAC',	'KMB',	'KMX',	'KO',	'KORS',	'KSS',	'KSU',	'LB',	'LBRDK',	'LDOS',	'LEA',	'LEN',	'LH',	'LLTC',	'LLY',	'LMT',	'LN',	'LNC',	'LNG',	'LNKD',	'LOW',	'LRCX',	'LULU',	'LVLT',	'LVS',	'LYB',	'MA',	'MAA',	'MAC',	'MAN',	'MAR',	'MBLY',	'MCD',	'MCHI',	'MCHP',	'MCK',	'MCO',	'MDLZ',	'MET',	'MJN',	'MMC',	'MMM',	'MNK',	'MNST',	'MO',	'MON',	'MPC',	'MRK',	'MSFT',	'MSI',	'MTB',	'NEE',	'NEM',	'NFLX',	'NFX',	'NKE',	'NLSN',	'NOC',	'NOW',	'NSC',	'NTES',	'NTRS',	'NUE',	'NVDA',	'NVO',	'NVS',	'NWL',	'NXPI',	'O',	'OC',	'OKE',	'OMC',	'ORCL',	'OXY',	'PAG',	'PANW',	'PAYX',	'PCAR',	'PCG',	'PDCE',	'PEG',	'PEP',	'PF',	'PFG',	'PG',	'PH',	'PII',	'PKG',	'PLD',	'PM',	'PNC',	'PNR',	'POST',	'PPG',	'PPS',	'PRGO',	'PRU',	'PSA',	'PSX',	'PVH',	'PX',	'PXD',	'Q',	'QRVO',	'RAI',	'RCL',	'RDS.A',	'RDS.B',	'RDUS',	'REGN',	'RGLD',	'RHT',	'RL',	'RMD',	'ROK',	'ROST',	'RRC',	'RSG',	'RTN',	'RY',	'SAP',	'SBAC',	'SBUX',	'SE',	'SEE',	'SHPG',	'SHW',	'SIG',	'SINA',	'SIX',	'SJM',	'SLB',	'SLCA',	'SLG',	'SNI',	'SO',	'SPG',	'SPGI',	'SPLK',	'SPR',	'SRCL',	'SRE',	'STI',	'STJ',	'STT',	'STZ',	'SWK',	'SWKS',	'SYK',	'SYY',	'T',	'TAP',	'TD',	'TEL',	'TEVA',	'TGT',	'THS',	'TIF',	'TJX',	'TMO',	'TMUS',	'TOT',	'TPX',	'TRGP',	'TRIP',	'TROW',	'TRV',	'TSCO',	'TSLA',	'TSN',	'TSO',	'TSRO',	'TSS',	'TTM',	'TTWO',	'TWLO',	'TWX',	'TXN',	'UAL',	'UHS',	'UL',	'ULTA',	'UN',	'UNH',	'UNP',	'UPS',	'URI',	'USB',	'UTX',	'V',	'VAR',	'VCIT',	'VFC',	'VLO',	'VMC',	'VMW',	'VNO',	'VNTV',	'VRSK',	'VRSN',	'VRTX',	'VTR',	'VZ',	'WAB',	'WB',	'WBA',	'WCN',	'WDAY',	'WDC',	'WEC',	'WFC',	'WHR',	'WLK',	'WLTW',	'WM',	'WMT',	'WRK',	'WSM',	'WUBA',	'WWAV',	'WYN',	'WYNN',	'XEC',	'XEL',	'XLNX',	'XOM',	'XRAY',	'XYL',	'YHOO',	'YUM',	'YY',	'ZBH',	'ZTS'};

for file=1:size(tickers,2)
    list(file) = strcat(tickers(file),'.csv');
end
interval = 60; % 60 for 1 min data, 300 for 5 min data

%loop though each file
FullDates = 0;

for x=1:size(list,2);
    try
    [num,txt,raw] = xlsread(list{1,x});
    catch
        continue
    end
    raw = raw(8:end,:);
    try
        TimeStamp = num(:,1);
    catch
        continue;
    end
    Open =  num(:,5);
    High =  num(:,3);
    Low =  num(:,4);
    Close =  num(:,2);
    Volume =  num(:,6);
    
    timeNan = find(isnan(TimeStamp) == 1);
    CleanDate = 0;
    for y=1:size(timeNan,1);
        
        date = raw{timeNan(y),1};
        correctDateCheck = strfind(date,'a');
        if isempty(correctDateCheck)
            continue;
        end
        date = strrep(date, 'a','');
        date = str2num(date);
        
        CleanDate(timeNan(y),1) = date;
        currTime = date ;
        
        try
            for z = timeNan(y) + 1:timeNan(y+1) -1;
                adjTime = currTime + (num(z,1)*interval);
                CleanDate(z,1) = adjTime;
            end
        catch
            for z = timeNan(y) + 1: timeNan(y)+1000; %fix this later
                try
                    adjTime = currTime + (num(z,1)*interval);
                    CleanDate(z,1) = adjTime;
                catch
                end
            end
        end
    end
    
    
    if (x ==1);
        FullDates = CleanDate;
        TableOpen(:,x) = Open(:,x);
        TableClose(:,x) = Close(:,x);
        TableHigh(:,x) = High(:,x);
        TableLow(:,x) = Low(:,x);
        TableVol(:,x) = Volume(:,x);
    else
        %create table of by matching FullDates with each CleanDate generated by file
        position = find(ismember(FullDates,CleanDate) == 1);
        
        for y = 1:size(position,1);
            TableOpen(position(y,1),x) = Open(y,1);
            TableClose(position(y,1),x) = Close(y,1);
            TableHigh(position(y,1),x) = High(y,1);
            TableLow(position(y,1),x) = Low(y,1);
            TableVol(position(y,1),x) = Volume(y,1);
        end
        
    end
    disp(x);
end
%this loop converts CleanDate (double) to a string, so it is readable
DatesString = cell(0,0);
for y = 1:size(FullDates,1)
    dateInStr = datetime( FullDates(y,1), 'ConvertFrom', 'posixtime' );
    DatesString{y,1} =  datestr( dateInStr);
end

TableOpen(find(TableOpen == 0))   = NaN;
TableClose(find(TableOpen == 0)) = NaN;
TableHigh(find(TableOpen == 0))   = NaN;
TableLow(find(TableOpen == 0))     = NaN;
TableVol(find(TableOpen == 0))     = NaN;

for x = 1:size(list,2)
    list{1,x} = strrep(list{1,x},'.csv','');
end

% k = findstr(DateString{:}, '13:30');
d = datetime('today','Format','yyyy-MM-dd');
d = datevec(d);

year = num2str(d(1));
month = num2str(d(2));
day = num2str(d(3));


filename = strcat('OneMinData_',  year,'-',month,'-',day , '.xlsx');

xlswrite(filename,TableOpen,1,'C2')
xlswrite(filename,TableClose,2,'C2')
xlswrite(filename,TableHigh,3,'C2')
xlswrite(filename,TableLow,4,'C2')
xlswrite(filename,TableVol,5,'C2')


xlswrite(filename,DatesString,1,'B2')
xlswrite(filename,DatesString,2,'B2')
xlswrite(filename,DatesString,3,'B2')
xlswrite(filename,DatesString,4,'B2')
xlswrite(filename,DatesString,5,'B2')

xlswrite(filename,FullDates,1,'A2')
xlswrite(filename,FullDates,2,'A2')
xlswrite(filename,FullDates,3,'A2')
xlswrite(filename,FullDates,4,'A2')
xlswrite(filename,FullDates,5,'A2')

xlswrite(filename,list,1,'C1')
xlswrite(filename,list,2,'C1')
xlswrite(filename,list,3,'C1')
xlswrite(filename,list,4,'C1')
xlswrite(filename,list,5,'C1')

delete('C:\Users\usman\OneDrive\Hedge\1minData\*.csv');
