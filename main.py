import Data
import Calc
import tkinter as tk
from tkinter.ttk import Progressbar
class gui():
    def progressBar(self):

        self.bar = tk.ttk.Progressbar(self.frame)
        self.bar.place(relwidth=.1, relheight=.5, relx=.88, rely=.2)
        return
    def buttonBar(self):
        self.style = tk.ttk.Style()
        self.style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth='4')
        # BUTTON BAR
        self.greatB = tk.Button(self.frame, bg='#2980b9', text='Greatest\n Gain', fg='yellow', font=40,
                                command=lambda: [self.updateG(Calc.bestDay(stock))])
        self.greatB.place(relwidth=.15, relheight=.1, relx=0, rely=.6)

        self.AVG = tk.Button(self.frame, text='Average\nVolume', fg='yellow', bg='#2980b9', font=40,
                             command = lambda:[self.updateA(Calc.avgV(stock))])
        self.AVG.place(relwidth=.15, relheight=.1, relx=0, rely=.7)
        self.cDevi = tk.Button(self.frame, bg='#2980b9', text='Closed\nDeviation', fg='yellow', font=40,
                               command=lambda: [self.updateD(Calc.deviation(stock))])
        self.cDevi.place(relwidth=.15, relheight=.1, relx=0, rely=.8)
        self.bestO = tk.Button(self.frame, bg='#2980b9', text='Best\nOff Day', fg='yellow', font=40,
                               command=lambda: [self.updateO(Calc.bestOff(stock))])
        self.bestO.place(relwidth=.15, relheight=.1, relx=0, rely=.9)
        # QUIT BUTTON

        #self.button2 = tk.Button(self.frame, bg='#2980b9',fg='yellow',text='QUIT',font=40,command=quit)
        #self.button2.place(relwidth=.15, relheight=.1, relx=.8, rely=0)
        # The Import Button
        self.Ibutton = tk.Button(self.frame, bd=5, bg='#2980b9', text='IMPORT', fg='yellow', font=40,
                                command=lambda: self.imp())
        self.Ibutton.place(relwidth=.15, relheight=.1, relx=.8, rely=.9)

        return
    def updateD(self,per):
        per = round(per,3)
        if(per>0):
            self.field.delete(1.00, tk.END)
            self.field.insert(1.0, stock["Name"] + " has an average deviation of\n" + str(
                per) + "% decrease between the closing price and the adjusted closing price.")
        else:
            self.field.delete(1.00, tk.END)
            self.field.insert(1.0, stock["Name"] + " has an average deviation of\n" + str(
                per) + "% increase between the closing price and the adjusted closing price.")

        return
    # updates the field for GUI about best average volume
    def updateA(self,avg):
        avg = round(avg,2)
        self.field.delete(1.00, tk.END)
        self.field.insert(1.0, stock["Name"] + " has an average trading volume of\n"+str(avg))

        return
    #updates the field for GUI about best Off hours
    def updateO(self,ind):
        num = round(stock["Open"][ind]-stock["Close"][ind-1],2)
        self.field.delete(1.00,tk.END)
        self.field.insert(1.0,stock["Name"]+" had its best off hours trading and \nit occured on the Night/Morning before\n"+stock["Date"][ind]+ " there was a "+str(num)+" gain.")
        return

    # updates the field for GUI about best day
    def updateG(self,ind):
        num = round(stock["Close"][ind] - stock["Open"][ind],5)
        self.field.delete(1.00, tk.END)
        self.field.insert(1.0,stock["Name"]+" had its greatest day ever trading \nand it happened on "+stock["Dates"][ind]+" there" " \n"+"was a "+str(num)+" gain.")
        return
    #To tell if it is imported properly and sets the stock as the global stock variable
    def imp(self):
        global stock
        self.field.delete(1.00, tk.END)
        try:
            #stock = Data.importData('stocks/' + self.entry.get() + '.csv')
            stock= Data.updatedImport('stocks/' + self.entry.get() + '.csv')
            self.field.insert(1.0,"IMPORT SUCCESSFUL!")
        except:
            self.field.insert(1.0,"Unexpected Error, Contact Author.")
        return
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)
        # Background Color
        self.frame1 = tk.Frame(self.root, bd=5, bg='#2980b9')
        self.frame1.place(relx=.5, rely=0, relwidth=1, relheight=1, anchor='n')
        # The main frame which stuff is placed on
        self.frame = tk.Frame(self.root, bd=5, bg='#d6eaf8')
        self.frame.place(relx=.5, rely=0.05, relwidth=0.85, relheight=.9, anchor='n')
        # This is the string variable for the entry
        self.info = tk.StringVar(self.frame, value="dan")

        # Label Above Entry with instructions
        self.tickLab = tk.Label(self.root, bg='#d6eaf8', fg="#2980b9", text="ENTER THE STOCK TICKER HERE")
        self.tickLab.place(relx=.5, rely=0.80, relwidth=0.22, relheight=.05, anchor='n')
        self.title = tk.Label(self.root, bg='#d6eaf8', fg="#2980b9", text="Stock Analysis", font=60)
        self.title.place(relx=.5, rely=0.10, relwidth=0.13, relheight=.025, anchor='n')
        self.instru = tk.Label(self.frame,justify=tk.LEFT, bg='#d6eaf8', fg="#2980b9", text="         Instructions:\nAt the bottom enter the\ndesired stock ticker.\nOn the bottom left you\ncan find hotkey buttons\nfor desired calculations.\nGreatest gain for a day\nAvg Volume Traded\nClosed Deviation is how\nmuch the adjusted close\ndiffers from closed\nBest gain in the off hours\n", font=40)
        self.instru.place(relx=0,rely=.05,relwidth=.275,relheight=.5)
        # Entry for ticker name
        self.entry = tk.Entry(self.frame, font=40, bg='#2980b9', fg='yellow')
        self.entry.place(relwidth=0.5, relheight=.1, relx=.25, rely=.9)
        # Display Text
        self.field = tk.Text(self.frame, bg='#2980b9', fg='yellow', bd=5)
        self.field.place(relwidth=.5, relheight=.2, relx=.25, rely=.6)
        #This is the progress bar
        self.progressBar()
        self.buttonBar()
        self.root.mainloop()

if __name__ == "__main__":
    stock = Data.updatedImport("stocks/aa.csv")
    ostock = Data.importData("stocks/aa.csv")
    print(Calc.bestOff(ostock))
    print(Calc.newBestOff(stock))

    #names = Data.test()
    #print(names)

    #root = gui()

