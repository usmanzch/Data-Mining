load  20080825-20160812-Cleaned.mat
tickersMain = tickers;

fileList = {'OneMinData_10_07_2016.xlsx' , 'OneMinData_2016-10-11.xlsx', 'OneMinData_2016-10-14.xlsx', 'OneMinData_2016-10-21.xlsx', 'OneMinData_2016-10-26.xlsx', 'OneMinData_2016-10-28.xlsx', 'OneMinData_2016-11-4.xlsx','OneMinData_2016-11-18.xlsx'};

for file = 1:size(fileList,2)
    file
    if file == 1
        [num,~,raw] = xlsread(fileList{1,file},1);
        newtickers = raw(1,3:end);
        newdata.Open = num(:,3:end);
        
        newDates =  num(:,1);

        for x = 1: size(newDates,1);
            dateInStr(x,1) = datetime( newDates(x,1), 'ConvertFrom', 'posixtime' );
        end
        
        [num,~,~] = xlsread(fileList{1,file},2);
        newdata.Close = num(:,3:end);
        [num,~,~] = xlsread(fileList{1,file},3);
        newdata.High = num(:,3:end);
        [num,~,~] = xlsread(fileList{1,file},4);
        newdata.Low = num(:,3:end);
        [num,~,~] = xlsread(fileList{1,file},5);
        newdata.Vol = num(:,3:end);
        
        for x=1:size(newtickers,2)
            [~,pos] = ismember(newtickers(1,x),tickersMain);
            if pos ==0
                continue
            end
            newBlock.Open(:,pos) = newdata.Open(:,x);
            newBlock.Close(:,pos) = newdata.Close(:,x);
            newBlock.High(:,pos) = newdata.High(:,x);
            newBlock.Low(:,pos) = newdata.Low(:,x);
            newBlock.Vol(:,pos) = newdata.Vol(:,x);
            
        end
        
        Data.Open =  newBlock.Open;
        Data.Close = newBlock.Close;
        Data.High = newBlock.High;
        Data.Low =  newBlock.Low;
        Data.Vol = newBlock.Vol;
        Dates = dateInStr;
        
    elseif file ~= 1
        %---------------------------------------------------------------
        
        [num,~,raw] = xlsread(fileList{1,file},1);
        newtickers = raw(1,3:end);
        newdata.Open = num(:,3:end);
        
        newDates =  num(:,1);
        clear dateInStr
        for x = 1: size(newDates,1);
            dateInStr(x,1) = datetime( newDates(x,1), 'ConvertFrom', 'posixtime' );
        end
        
        [num,~,~] = xlsread(fileList{1,file},2);
        newdata.Close = num(:,3:end);
        [num,~,~] = xlsread(fileList{1,file},3);
        newdata.High = num(:,3:end);
        [num,~,~] = xlsread(fileList{1,file},4);
        newdata.Low = num(:,3:end);
        [num,~,~] = xlsread(fileList{1,file},5);
        newdata.Vol = num(:,3:end);
        
        clear newBlock
        for x=1:size(newtickers,2)
            [~,pos] = ismember(newtickers(1,x),tickersMain);
            if pos ==0
                continue
            end
            newBlock.Open(:,pos) = newdata.Open(:,x);
            newBlock.Close(:,pos) = newdata.Close(:,x);
            newBlock.High(:,pos) = newdata.High(:,x);
            newBlock.Low(:,pos) = newdata.Low(:,x);
            newBlock.Vol(:,pos) = newdata.Vol(:,x);
            
        end
        
        Data.Open=  vertcat(Data.Open, newBlock.Open);
        Data.Close = vertcat(Data.Close, newBlock.Close);
        Data.High = vertcat(Data.High, newBlock.High);
        Data.Low =  vertcat(Data.Low, newBlock.Low);
        Data.Vol = vertcat(Data.Vol, newBlock.Vol);
        Dates = vertcat(Dates,dateInStr);
        
    end
end

[UniqueDates,iU, iD]  = unique(Dates, 'stable');
Data.Open = Data.Open(iU,:);
Data.Close =  Data.Close(iU,:);
Data.High =  Data.High(iU,:);
Data.Low =  Data.Low(iU,:);
Data.Vol =  Data.Vol(iU,:);

save('GoogleData.mat' , 'Data','UniqueDates');