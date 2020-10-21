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
#This calculates through all of the stocks, Test Function not real
def greatestGain(stocks):
    for x in range(len(stocks)):
        for g in range(len(stocks[x]["high"])):
            if(stocks[x]["high"][g]>25):
                print(stocks[x]["high"][g])
#In Progress not completed
def beta(stock,year):
    #We Need to calculate correlation and deviation
    #Using a one year Correlation to start
    #218 for the last year
    sum=0
    for x in range(len(stock['dates'])):
        if(year in stock['dates'][x]):
            sum= sum+1
    print(sum)
    return

#This calculates the standard deviation between the close and adj close
def deviation(stock):
    # we add up all the percentages then divide by the length
    per = 0
    sum = 0
    for x in range(len(stock["close"])):
        #print(stock["close"][x]-stock["adj"][x])
        per = ((stock["close"][x]-stock["adj"][x]) / stock["close"][x])*100
        #print(per)
        sum =per+sum
    sum = sum/len(stock["close"])
    return sum

def avgV(stock):
    sum=0
    for x in range(len(stock['volume'])):
        sum = sum+stock['volume'][x]
    return (sum/len(stock['volume']))
#UPDATED FUNCTIONS FOR DATA FRAME
def newavgV(stock):
    sum=0
    for g in range(len(stock.index)):
        sum = sum+stock['Volume'][g]
    return (sum/(len(stock.index)))
    #need to test with unit testing but amzn it works right
def newDeviation(stock):
    # we add up all the percentages then divide by the length
    per = 0
    sum = 0
    for x in range(len(stock.index)):
        per = ((stock["Close"][x]-stock["Adj Close"][x]) / stock["Close"][x])*100

        #print(per)
        sum =per+sum
    return sum/len(stock.index)
