from tkinter import *
from charcountf import CharacterCounter

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.labels(0)
        self.usertxt()
        self.asc_desc()
        self.buttons()
        self.results()
        self.confirm_clear()


    def labels(self, char_sum):  
        Label(self, text="SUM OF CHARACTERS: {}           ".format(char_sum), font='Ubuntu 12 bold').grid(row=32, column=1,sticky=W) 
        Label(self, text="  ").grid(row=0, column=0)
        Label(self, text="  ").grid(row=0, column=3)
        Label(self, text="RESULTS: ",font='Ubuntu 12 bold').grid(row=1, column=4, sticky=W)
        Label(self, text="Enter yout text here and confirm:").grid(row=1, column=1, sticky=W)


    def usertxt(self):
        self.usrtxt=Text(self, width=50, height=30, wrap=WORD)
        self.usrtxt.grid(row=2, column=1, rowspan=30, columnspan=2)


    def buttons(self):
        Button(self, text='Confirm', command=self.confirm).grid(row=1,column=2, sticky=E)
        Button(self, text='Clear', command=self.confirm_clear).grid(row=1,column=1, sticky=E)

        
    def results(self):
        self.outputtxt=Text(self, width=20, height=30, wrap=WORD)
        self.outputtxt.grid(row=2, rowspan=30, column=4)


    def asc_desc(self):
        self.var=BooleanVar()
        self.var.set(True)
        Radiobutton(self, text='ascending', variable=self.var, value=False, command=self.confirm).grid(row=3, column=5, sticky =W)
        Radiobutton(self, text='descending', variable=self.var, value=True, command=self.confirm).grid(row=4, column=5, sticky =W)


    def confirm(self):
        txt = CharacterCounter((self.usrtxt.get("0.0", END))[:-1]) #[:-1] removes from the text 'enter character' introduced by GUI
        self.outputtxt.delete(0.0, END)
        self.outputtxt.insert(0.0, txt.chartxtcount(self.var.get()))
        self.char_sum=str(txt.lenght_of_text)
        self.labels(self.char_sum)


    def confirm_clear(self):
        self.usrtxt.delete(0.0, END)
        self.char_sum=0
        self.labels(self.char_sum)

root = Tk()
root.title('Character Count Tool 2.0')
root.geometry("800x600")
app = Application(root)


root.mainloop()
