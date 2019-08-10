from tkinter import *
import charcountf

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.label1()
        self.labels()
        self.user_text()
        self.usrtxtdisp()
        self.asc_desc()
        self.buttons()
        self.results()
        self.confirm_clear()
    def label1(self,lab='SUM OF CHARACTERS: 0'):      
        Label(self, text=lab, font='Ubuntu 12 bold').grid(row=32, column=1,sticky=W)       
    def labels(self,lab='xxx'):    
        Label(self, text="  ").grid(row=0, column=0)
        Label(self, text="  ").grid(row=0, column=3)
        Label(self, text="RESULTS: ",font='Ubuntu 12 bold').grid(row=1, column=4, sticky=W)
        Label(self, text="Enter yout text here and confirm:").grid(row=0, column=1, sticky=E)
    def user_text(self):
        self.usrtxt=Entry(self)
        self.usrtxt.grid(row=0, column=2, sticky=E)
    def usrtxtdisp(self):
        self.usrtxtdis=Text(self, width=50, height=30, wrap=WORD)
        self.usrtxtdis.grid(row=2, column=1, rowspan=30, columnspan=2)
        self.usrtxtdis.delete(0.0, END)
        self.usrtxtdis.insert(0.0, '...the text will be displayed here...')
    def buttons(self):
        Button(self, text='Confirm', command=self.confirm).grid(row=1,column=2, sticky=E)
        Button(self, text='Clear', command=self.confirm_clear).grid(row=1,column=1, sticky=E)
    def results(self):
        self.outputtxt=Text(self, width=20, height=30, wrap=WORD)
        self.outputtxt.grid(row=2, rowspan=30, column=4)
    def asc_desc(self):
        self.var=BooleanVar()
        self.var.set(True)
        self.rad1=Radiobutton(self, text='ascending', variable=self.var, value=False, command=self.confirm).grid(row=3, column=5, sticky =W)
        self.rad2=Radiobutton(self, text='descending', variable=self.var, value=True, command=self.confirm).grid(row=4, column=5, sticky =W)
    def confirm(self):
        txt=self.usrtxt.get()
        self.usrtxtdis.delete(0.0, END)
        if txt:
            self.usrtxtdis.insert(0.0, txt)
        else:
            self.usrtxtdis.insert(0.0, '...the text will be displayed here...')
        self.outputtxt.delete(0.0, END)
        self.outputtxt.insert(0.0, charcountf.chartxtcount(txt, self.var.get()))
        y="SUM OF CHARACTERS: %s"%(str(len(txt))+'        ')
        self.label1(y)
    def confirm_clear(self):
        self.usrtxt.delete(0, END)
        self.usrtxtdis.delete(0.0, END)
        self.usrtxtdis.insert(0.0, '...the text will be displayed here...')

root = Tk()
root.title('Character Count Tool 1.0')
root.geometry("800x600")
app = Application(root)


root.mainloop()
