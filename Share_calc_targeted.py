import tkinter as tk
from tkinter.font import Font
from datetime import datetime
from tkinter import messagebox as mb
import os



global root, canvas1
global windowHeight, windowWidth

wLabel=75
wEntry=175
wButton=150
lLabel=30
lEntry=30
entryWidth=75

class stockWindow:
    def __init__(self):
        self.labels()
        self.entries()
        self.radioButtons()
        self.createWindow()
        self.test_values()
        
    def labels(self):
        self.aLossPercentLabel = tk.Label(root, text="AL(%)")
        self.nsLabel = tk.Label(root, text="Normal Sell")
        self.ssLabel = tk.Label(root, text="Short Sell")
        self.brokerageLabel = tk.Label(root, text="Brokerage(%)")
        self.iaLabel = tk.Label(root, text="Investment Amt (Rs)")
        self.bpLabel = tk.Label(root, text="Base Price (Rs)")
        self.ptLabel = tk.Label(root, text="Profit Target (Rs)")
        self.alLabel = tk.Label(root, text="Acceptable Loss (Rs)")
        self.fpLabel = tk.Label(root, text="Final Price (Rs)",fg='blue')
        self.slvLabel = tk.Label(root, text="Stop loss value (Rs)",fg='blue')
        self.nosLabel = tk.Label(root, text="No. of Shares")
        self.marginLabel = tk.Label(root,text="Broker Margin:")
        self.reqFieldLabel = tk.Label(root,text="Required Fields")
        self.reqFieldsLabel1 = tk.Label(root,text="*",fg="red", font=(None,15))
        self.reqFieldsLabel2 = tk.Label(root,text="*",fg="red", font=(None,15))
        self.reqFieldsLabel3 = tk.Label(root,text="*",fg="red", font=(None,15))
        self.reqFieldsLabel4 = tk.Label(root,text="*",fg="red", font=(None,15))

    def entries(self):
        self.aLossPercentEntry = tk.Entry(root)
        self.brokerageEntry = tk.Entry(root)
        self.iaEntry = tk.Entry(root)
        self.bpEntry = tk.Entry(root)
        self.ptEntry = tk.Entry(root)
        self.alEntry = tk.Entry(root)
        self.slvEntry = tk.Entry(root)
        self.fpEntry = tk.Entry(root)
        self.nosEntry = tk.Entry(root)

    def radioButtons(self):
        self.option = tk.IntVar()
        self.option.set(1)
        self.nsRadioButton = tk.Radiobutton(root, text="Normal Sell",  value=1, variable=self.option)
        self.ssRadioButton = tk.Radiobutton(root, text="Short Sell",  value=2, variable=self.option)        

    def createWindow(self):
        global wLabel, wEntry, wButton, lLabel, lEntry, entryWidth

        canvas1.create_window(100,lLabel,window=self.nsRadioButton)
        canvas1.create_window(200,lLabel,window=self.ssRadioButton)

        canvas1.create_window(10, windowHeight-15, width=10, window=self.reqFieldsLabel4)
        canvas1.create_window(60, windowHeight-20,window=self.reqFieldLabel)

        lLabel = lLabel+60
        canvas1.create_window(wLabel,lLabel,window=self.aLossPercentLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel,lLabel,window=self.brokerageLabel)
        lLabel = lLabel+30        
        canvas1.create_window(wLabel, lLabel, window=self.iaLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.bpLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.ptLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.alLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.slvLabel)
        lLabel = lLabel+30        
        canvas1.create_window(wLabel, lLabel, window=self.fpLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.nosLabel)

        lEntry = lEntry+60
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.aLossPercentEntry)
        self.aLossPercentEntry.insert(0,int(2))
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.brokerageEntry)
        self.brokerageEntry.insert(0,float(0.3))        
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.iaEntry)
        canvas1.create_window(wEntry+50, lEntry+5, width=10, window=self.reqFieldsLabel1)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.bpEntry)
        canvas1.create_window(wEntry+50, lEntry+5, width=10, window=self.reqFieldsLabel2)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.ptEntry)
        canvas1.create_window(wEntry+50, lEntry+5, width=10, window=self.reqFieldsLabel3)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.alEntry)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.slvEntry)
        lEntry = lEntry+30        
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.fpEntry)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.nosEntry)

        button1 = tk.Button(text='Calculate', command=self.getCalculation,bg='green',fg='white')
        canvas1.create_window(wButton, lEntry+50, window=button1)
        lEntry = lEntry+50

        button1 = tk.Button(text='Help', command=self.open_guide,bg='black',fg='white')
        canvas1.create_window(windowWidth-30, windowHeight-20, window=button1)

    def test_values(self):
        self.iaEntry.insert(0,float("{:.2f}".format(50000)))
        self.bpEntry.insert(0,float("{:.2f}".format(30)))
        self.ptEntry.insert(0,float("{:.2f}".format(2000)))

    def open_guide(self):
        os.startfile("share_calc_targeted_help.txt")

    def clear_widget_text(self,widget):
        widget['text'] = ""

    def record_values(self,inValues):
        try:
            f = open('record.csv','a')
            f.write(inValues + "\n")
            f.close()            
            mb.showinfo('Saved', 'values saved successfully in record.csv file!')
        except Exception as e:
            mb.showerror('Failed', e)

    def getCalculation (self):
        global lEntry
        temp = lEntry

        
        #clear lables so that new values dont overlap 
        self.clear_widget_text(self.marginLabel)
        
        #clear entries before reasigning values
        self.slvEntry.delete(0,'end')
        self.nosEntry.delete(0,'end')
        self.alEntry.delete(0,'end')
        
        bp = float(self.bpEntry.get())        
        ia = float(self.iaEntry.get())
        pt = float(self.ptEntry.get())
        
        self.nosEntry.insert(0,int(ia//bp))
        nos = int(self.nosEntry.get())

        alPercent = float(self.aLossPercentEntry.get())

        self.alEntry.insert(0,int((alPercent/100)*ia))
        al = float(self.alEntry.get())        

        if self.option.get() == 1:
            self.fp = ((ia + pt) / nos)
            self.fpEntry.insert(0,float("{:.2f}".format(self.fp)))
        
            self.marginPercent = float(self.brokerageEntry.get())
            self.margin = (((self.marginPercent/100)*bp)+((self.marginPercent/100)*self.fp))*nos

            self.slv = (((bp*nos)+self.margin)-al)/nos
            self.slvEntry.insert(0,float("{:.2f}".format(self.slv)))
            
            self.fpEntry.delete(0,'end')
            self.fp = (((ia + pt) + self.margin) / nos) 
            self.fpEntry.insert(0,float("{:.2f}".format(self.fp)))
        

        if self.option.get() == 2:
            self.fp = ((ia - pt) / nos)
            self.fpEntry.insert(0,float("{:.2f}".format(self.fp)))
        
            self.marginPercent = float(self.brokerageEntry.get())
            self.margin = (((self.marginPercent/100)*bp)+((self.marginPercent/100)*self.fp))*nos

            self.slv = (((bp*nos)-self.margin)+al)/nos
            self.slvEntry.insert(0,float("{:.2f}".format(self.slv)))
            
            self.fpEntry.delete(0,'end')
            self.fp = (((bp*nos)-(pt+self.margin)))/nos
            self.fpEntry.insert(0,float("{:.2f}".format(self.fp)))      
        
        
        self.marginLabel = tk.Label(root,text=str.format("Broker Margin (Rs): {0}",float("{:.2f}".format(self.margin))),fg='red')
        canvas1.create_window(150, temp+40, window=self.marginLabel)
        temp=lEntry

        rv = "D" + str(datetime.now())+ "," + "" + "," + str(ia) + "," + str(bp) + "," + str(self.fp) + "," + str(nos) + "," + str(self.margin) + "," + "" + "," + str(pt) + "," + "Share_calc_targeted"

        button1 = tk.Button(text='Save', command=lambda :self.record_values(rv),bg='black',fg='white')
        canvas1.create_window(windowWidth-70, windowHeight-20, window=button1)
        

if __name__ == "__main__":
    windowHeight = 480
    windowWidth = 300
    root = tk.Tk()
    root.title("Share Calculator")
    canvas1 = tk.Canvas(root, width = windowWidth, height = windowHeight)
    root.configure()
    canvas1.pack()
    stockWindow()
    root.mainloop()
   
