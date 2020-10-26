import os
import main
import pandas as pd

def updatedImport(sName):
    try:
        stock = pd.read_csv(sName)
    except:
        print("File name Error")
    #NEED TO FIX SNAME
    #Check Github Change 10/24
    return stock
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
        #print(i)
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
                stock =updatedImport(Path + i)
                stocks[name] = stock
def test():
    names = []
    files = os.listdir("stocks/")
    for x in files:
        if x.endswith(".csv"):
            names.append(x[:-4])
    return names
    return stocks
def importData(sName):
    #This is an outdated import data function I used when I saved it with tuples and dictionaries
    #Now Obselete
    #Kept just to display
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
        #THIS IS TO CHECK IF THE DATA IS There
        if (start == ''):
            print("Ignored this day due to no trading!")
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