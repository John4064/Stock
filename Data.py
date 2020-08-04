def importData():
    inFile = open("bac.us.txt", 'r')
    dates = []
    openL = []
    highL = []
    lowL = []
    closeL = []
    volumeL = []
    line = inFile.readline()
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
    tupD = tuple(dates)
    tupO = tuple(openL)
    tupH = tuple(highL)

    print(len(tupD))