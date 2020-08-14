import Data
import tkinter as tk
from tkinter.ttk import Progressbar
#import panda

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
def greatestGain(stocks):
    for x in range(len(stocks)):
        for g in range(len(stocks[x]["high"])):
            if(stocks[x]["high"][g]>25):
                print(stocks[x]["high"][g])
def hello():
    print("hello!")
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relx=.5, rely=0.1, relwidth=0.75, relheight=.6, anchor='n')
    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=.3,relx=.2,rely=.5)
    menu = tk.Menu(root)
    new_item = tk.Menu(menu)
    new_item.add_command(label='Import All',command=Data.importAll)
    menu.add_cascade(label='Import',menu=new_item)
    root.config(menu=menu)
    #canvas = tk.Canvas(root,height = 600, width = 400, bg = "cyan")
    #Execution of GUI
    root.mainloop()


    #THIS IS THE PROGRESS BAR IDEA
   # style = tk.ttk.Style()
    #style.theme_use('default')
    #style.configure("black.Horizontal.TPorgressbar", background = 'black')
    #bar = Progressbar(window, length=200,style='black.Horizontal.TProgressbar')
   # bar['value'] = 70
    #bar.pack()
