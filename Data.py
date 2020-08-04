class Market():
    def importData(self):
        inFile = open("bac.us.txt", 'r')
        dates = []
        openL = []
        highL =[]
        lowL =[]
        closeL =[]
        volumeL =[]
        line = inFile.readline()
        for line in inFile:
            line = line.strip()
            date,start,high,low,close,volume,useless = line.split(',')
            dates.append(dates)
            openL.append(float(start))
            highL.append(float(high))
            lowL.append(float(low))
            closeL.append(float(close))
            volumeL.append(int(volume))
        #for x in range(len(date)):
       #     if name == names[x]:
                # fix if doesnt match
        #        balance = bals[x]
        #        return

    def __init__(self):

        self.importData()
        # add create if not a returning customer
        return

stocks = Market()