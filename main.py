import Data
import Calc
import tkinter as tk
from tkinter.ttk import Progressbar
#import panda
def error():
    return
class gui():
    def progressBar(self):
        bar = tk.ttk.Progressbar(self.frame)
        bar.place(relwidth=.1, relheight=.5, relx=.88, rely=.2)
        return
    def buttonBar(self):
        # BUTTON BAR
        self.greatB = tk.Button(self.frame, bg='#2980b9', text='Greatest\n Gain', fg='yellow', font=40,
                                command=lambda: [self.updateG(Calc.bestDay(stock))])
        self.greatB.place(relwidth=.15, relheight=.1, relx=0, rely=.2)

        self.PE = tk.Button(self.frame, bg='#2980b9', text='PE', fg='yellow', font=40)
        self.PE.place(relwidth=.15, relheight=.1, relx=0, rely=.3)
        self.beta = tk.Button(self.frame, bg='#2980b9', text='Beta', fg='yellow', font=40)
        self.beta.place(relwidth=.15, relheight=.1, relx=0, rely=.4)
        self.bestO = tk.Button(self.frame, bg='#2980b9', text='Best\nOff Day', fg='yellow', font=40,
                               command=lambda: [self.updateO(Calc.bestOff(stock))])
        self.bestO.place(relwidth=.15, relheight=.1, relx=0, rely=.5)
        # QUIT BUTTON
        self.photo = tk.PhotoImage(file="quit.png")
        self.button2 = tk.Button(self.frame, image=self.photo, command=quit)
        self.button2.place(relwidth=.17, relheight=.06, relx=.82, rely=.01)
        # The Import Button
        self.button = tk.Button(self.frame, bd=5, bg='#2980b9', text='IMPORT', fg='yellow', font=40,
                                command=lambda: self.imp())
        self.button.place(relwidth=.15, relheight=.1, relx=.8, rely=.9)

        return
    def updateO(self,ind):
        num = round(stock["open"][ind]-stock["close"][ind-1],5)
        self.field.delete(1.00,tk.END)
        self.field.insert(1.0,stock["name"]+" had its best off hours trading and \nit occured on the Night/Morning before\n"+stock["dates"][ind]+ " there was a "+str(num)+" gain.")
        return
    def updateG(self,ind):
        num = round(stock["close"][ind] - stock["open"][ind],5)
        self.field.delete(1.00, tk.END)
        self.field.insert(1.0,stock["name"]+" had its greatest day ever trading\n and it happened on "+stock["dates"][ind]+"\n"+" there was a "+str(num)+" gain.")
        return
    def imp(self):
        global stock
        stock = Data.importData('stocks/' + self.entry.get() + '.us.txt')
        return
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)
        # Background COlor
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
        # The above menu to import all NOT RECCOMENDED TO USE
        # menu = tk.Menu(root)
        # new_item = tk.Menu(menu)
        # new_item.add_command(label='Import All',command=Data.importAll)
        # menu.add_cascade(label='Import',menu=new_item)
        # root.config(menu=menu)
        # canvas = tk.Canvas(root,height = 600, width = 400, bg = "cyan")
        # Execution of GUI

        # THIS IS THE PROGRESS BAR IDEA
        # style = tk.ttk.Style()
        # style.theme_use('default')
        # style.configure("black.Horizontal.TPorgressbar", background = 'black')
        # bar = Progressbar(window, length=200,style='black.Horizontal.TProgressbar')


        # bar['value'] = 70
        # bar.pack()


if __name__ == "__main__":
    dan = gui()
