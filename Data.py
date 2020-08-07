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
    stock = {"name": "bac", "dates": tuple(dates), "open":tuple(openL),
              "high":tuple(highL), "low":tuple(lowL), "close":tuple(closeL), "volume":tuple(volumeL)}
    return stock