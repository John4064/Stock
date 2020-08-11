import os

def importAll():
    #Save the stock file into stocks.
    #having the ticker : stockfile
    stocks = {}
    Path = "Stocks/"
    name = ""
    stock = {}
    files = os.listdir(Path)
    for i in files:
        if i.endswith("us.txt") and i.startswith("f"):
            with open(Path + i, 'r') as f:
                name = i[:-7]
                # for line in f:
                # Here you can check (with regex, if, or whatever if the keyword is in the document.)
                # print(Path)
                importData(Path+i)
                stocks[name] = stock
    return stocks
def importData(sName):
    #Come Back To this in order to read all text files at once
    #test ones BAC, HL, NOK
    inFile = open(sName, 'r')
    dates = []
    openL = []
    highL = []
    lowL = []
    closeL = []
    volumeL = []
    #This is just to ignore the first line of the text file
    line = inFile.readline()
    #This sequiantly goes through each line and splits up each statistic
    #then adds it to a list with the designated statistic
    #Same index will generate the same day
    for line in inFile:
        line = line.strip()
        date, start, high, low, close, volume, useless = line.split(',')
        dates.append(date)
        openL.append(float(start))
        highL.append(float(high))
        lowL.append(float(low))
        closeL.append(float(close))
        volumeL.append(int(volume))
        #We just imported all the data from the specific stock file.
        #Now we create tuples of it all and insert it into a dictionary
    #tupD = tuple(dates)
    tupO = tuple(openL)
    tupH = tuple(highL)
    tupL = tuple(lowL)
    tupC = tuple(closeL)
    tupV = tuple(volumeL)
    #Saves the tiker as name in the stock
    stock = {"name": sName[:-7], "dates": tuple(dates), "open":tuple(openL),
              "high":tuple(highL), "low":tuple(lowL), "close":tuple(closeL), "volume":tuple(volumeL)}

    return stock