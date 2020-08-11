import Data
import tkinter as tk


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
    return num
def greatestGain(stocks):
    for x in range(len(stocks)):
        for g in range(len(stocks[x]["high"])):
            if(stocks[x]["high"][g]>25):
                print(stocks[x]["high"][g])
def damn():
    print("DICK WAD")
    return
if __name__ == "__main__":
    gui = tk.Tk()
    gui.geometry("800x600")
    gui.resizable(width=False, height=False)
    frame = tk.Frame(gui, bg ="blue")
    frame.pack()
    bottomframe = tk.Frame(gui)
    bottomframe.pack(side=tk.BOTTOM)
    leftFrame = tk.Frame(gui)
    leftFrame.pack(side=tk.LEFT)
    rightFrame = tk.Frame(gui)
    rightFrame.pack(side=tk.RIGHT)

    button = tk.Button(frame,text = "QUIT", bg = "cyan",fg ="gray",command=quit,bd = 6)
    button.pack(side=tk.LEFT)
    button1 = tk.Button(bottomframe, text="DAN", bg="cyan", fg="gray", command=quit, bd=6)
    button1.pack(side=tk.LEFT)




    w = tk.Menubutton(leftFrame,text="DICK",relief = tk.RAISED, bitmap="@quit.xbm",bg="cyan")
    w.menu = tk.Menu(w,tearoff = 0)
    w.grid()

    dan = tk.IntVar()
    ketch= tk.IntVar()
    w.menu.add_checkbutton(label="dan", variable=dan)
    w.menu.add_checkbutton(label="ketch", variable=ketch,command=quit)
    w.pack()
    #Execution of GUI
    gui.mainloop()