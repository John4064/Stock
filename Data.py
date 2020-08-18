import os
import main
def importAll():
    #Save the stock file into stocks.
    #having the ticker : stockfile
    stocks = {}
    Path = "Stocks/"
    name = ""
    stock = {}
    files = os.listdir(Path)
    for i in files:
        #Glitched since there all upper case now
        if i.endswith(".csv") and i.startswith("f"):
            with open(Path + i, 'r') as f:
                name = i[7:-4]
                # for line in f:
                # Here you can check (with regex, if, or whatever if the keyword is in the document.)
                # print(Path)
                importData(Path+i)
                stocks[name] = stock
    return stocks
def importData(sName):
    #Come Back To this in order to read all text files at once
    #test ones BAC, HL, NOK
    try:
        inFile = open(sName, 'r')
    except:
        print("File name Error")
    dates = []
    openL = []
    highL = []
    lowL = []
    closeL = []
    adjCL = []
    volumeL = []
    #This is just to ignore the first line of the text file
    line = inFile.readline()
    #This sequiantly goes through each line and splits up each statistic
    #then adds it to a list with the designated statistic
    #Same index will generate the same day
    for line in inFile:
        line = line.strip()
        date, start, high, low, close, adjC, volume = line.split(',')
        dates.append(date)
        #start = open just open is a keyword in python
        openL.append(float(start))
        highL.append(float(high))
        lowL.append(float(low))
        closeL.append(float(close))
        #adjC is the adjusted close
        adjCL.append(float(adjC))
        volumeL.append(int(volume))
        #We just imported all the data from the specific stock file.
        #Now we create tuples of it all and insert it into a dictionary
    #Saves the tiker as name in the stock
    stock = {"name": sName[7:-4], "dates": tuple(dates), "open":tuple(openL),
              "high":tuple(highL), "low":tuple(lowL), "close":tuple(closeL), "adj":tuple(adjCL),"volume":tuple(volumeL)}
    print(sName[7:-4])
    return stock