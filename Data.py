import os
import main
def importAll():
    #Save the stock file into stocks.
    #having the ticker : stockfile
    stocks = {}
    Path = "Stocks/"
    name = ""
    stock = {}
    total= 0
    files = os.listdir(Path)
    for i in files:
        #Glitched since there all upper case now
        if i.endswith(".csv"):
            with open(Path + i, 'r') as f:
                name = i[:-4]
                # for line in f:
                # Here you can check (with regex, if, or whatever if the keyword is in the document.)
                # print(Path)
                #print(name)
                #if(name != 'ADP' and name != 'AEM'and name != 'AFB'):
                #    print(name)
                importData(Path + i)
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
        #print(line)
        date, start, high, low, close, adjC, volume = line.split(',')
        #THIS IS TO CHECK IF THE DATA IS There
        if (start == ''):
            print("Ignored this day due to no trading")
        else:
            # start = open just open is a keyword in python
            dates.append(date)
            openL.append(float(start))
            highL.append(float(high))
            lowL.append(float(low))
            closeL.append(float(close))
            # adjC is the adjusted close
            adjCL.append(float(adjC))
            volumeL.append(float(volume))

        #This determines if the data is an integer or float
        #depending on the stock it will change due to how
        #the dataset saved it
        #We just imported all the data from the specific stock file.
        #Now we create tuples of it all and insert it into a dictionary
    #Saves the tiker as name in the stock
    stock = {"name": sName[7:-4], "dates": tuple(dates), "open":tuple(openL),
              "high":tuple(highL), "low":tuple(lowL), "close":tuple(closeL), "adj":tuple(adjCL),"volume":tuple(volumeL)}
    return stock