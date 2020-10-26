import Data
#This Checks to see the greatest gain from the opening of the day to the closing
#Returns a list of indexs of the specified days
def newDeviation(stock):
    # we add up all the percentages then divide by the length
    per = 0
    sum = 0
    for x in range(len(stock)):
        per = ((stock["Close"][x]-stock["Adj Close"][x]) / stock["Close"][x])*100
        #print(per)
        sum =per+sum
    return sum/len(stock)

def newBestDay(stock):
    ind = 0
    max = -48392839232
    for x in range(len(stock)):
        difference = stock["Close"][x] - stock["Open"][x]
        if (difference > max):
           # print(max, " DIFFERENCE IS ", difference)
            max = difference
            ind = x
        #if (x == len(stock) - 1):
            #print(ind)
    return ind
#This is a function who determines who had the best gain in the off hours of stock market
def newBestOff(stock):
    ind = 0
    max = -423829
    #iterates through the list start from 1->legnth and checks the night before close and the current opening
    #then calculates the off hours trading and figures out which is the best day
    for x in range(1,len(stock)):
        if(stock["Open"][x]-stock["Close"][x-1] >max):
            ind = x
            max = stock["Open"][x]-stock["Close"][x-1]
    return ind
def newAvgV(stock):
    sum=0
    for x in range(len(stock)):
        sum = sum+stock['Volume'][x]
    return (sum/len(stock))