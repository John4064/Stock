import Data
#This Checks to see the greatest gain from the opening of the day to the closing
#Returns a list of indexs of the specified days
def bestDay(stock):
    ind = 0
    max = -48392839232
    for x in range(len(stock["open"])):
        difference = stock["close"][x] - stock["open"][x]
        if (difference > max):
           # print(max, " DIFFERENCE IS ", difference)
            max = difference
            ind = x
        #if (x == len(stock) - 1):
            #print(ind)
    return ind
#This is a function who determines who had the best gain in the off hours of stock market
def bestOff(stock):
    ind = 0
    max = -423829
    #iterates through the list start from 1->legnth and checks the night before close and the current opening
    #then calculates the off hours trading and figures out which is the best day
    for x in range(1,len(stock["open"])):
        if(stock["open"][x]-stock["close"][x-1] >max):
            ind = x
            max = stock["open"][x]-stock["close"][x-1]
    return ind
def volatility(stock):
    # This checks out volatile the stock is during trading day
    # First version we check which day has most volaitly
    # second version we check how often the stock flucuates +-5% during a day of trading
    ind = 0
    max = 0

    #for x in range(len(stock)):
     #   if(abs(stock["high"][x]-stock["low"][x])>max):
      #      ind = x
       #     max = abs(stock["high"][x]-stock["low"][x])
    return ind
def volaitility2(stocks):
    #this could do the ranking of the volaitility of all the stocks
    num = 0.0
    return num
def greatestGain(stocks):
    for x in range(len(stocks)):
        for g in range(len(stocks[x]["high"])):
            if(stocks[x]["high"][g]>25):
                print(stocks[x]["high"][g])
if __name__ == "__main__":
    bac = Data.importData("bac.us.txt")
    hl = Data.importData("hl.us.txt")
    nok = Data.importData("nok.us.txt")
    stocks = {"name":"bac", ""}
    #greatestGain(stocks)
    #I think a dictionary would be thhe best method for storing stocks
    #this way u can easily search by ticker rather than index
    #thus resulting in a faster searchup time for these
