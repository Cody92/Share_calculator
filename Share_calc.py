import tkinter as tk
import os
from datetime import datetime
from tkinter import messagebox as mb

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
        self.createWindow()
        self.test_values()
        
    def labels(self):
        self.aLossPercentLabel = tk.Label(root, text="AL(%)")
        self.brokerageLabel = tk.Label(root, text="Brokerage(%)")
        self.iaLabel = tk.Label(root, text="Investment Amt (Rs)")
        self.bpLabel = tk.Label(root, text="Base Price (Rs)")
        self.fpLabel = tk.Label(root, text="Final Price (Rs)")
        self.slvLabel = tk.Label(root, text="Stop loss value (Rs)",fg='blue')
        self.npnlLabel = tk.Label(root, text="No Profit No Loss (Rs)")
        self.alLabel = tk.Label(root, text="Acceptable Loss (Rs)")
        self.nosLabel = tk.Label(root, text="No. of Shares")
        self.marginLabel = tk.Label(root,text=str.format("Broker Margin:"))
        self.plLabel = tk.Label(root, text= str.format("Profit/Loss :"))
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
        self.fpEntry = tk.Entry(root)
        self.slvEntry = tk.Entry(root)
        self.npnlEntry = tk.Entry(root)
        self.alEntry = tk.Entry(root)
        self.nosEntry = tk.Entry(root)

    def createWindow(self):
        global wLabel, wEntry, wButton, lLabel, lEntry, entryWidth

        canvas1.create_window(50,lLabel,window=self.aLossPercentLabel)
        canvas1.create_window(175,lLabel,window=self.brokerageLabel)

        canvas1.create_window(10, windowHeight-15, width=10, window=self.reqFieldsLabel4)
        canvas1.create_window(60, windowHeight-20,window=self.reqFieldLabel)

        lLabel = lLabel+60        
        canvas1.create_window(wLabel, lLabel, window=self.iaLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.bpLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.fpLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.slvLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.npnlLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.alLabel)
        lLabel = lLabel+30
        canvas1.create_window(wLabel, lLabel, window=self.nosLabel)

        canvas1.create_window(100, lEntry, width=50, window=self.aLossPercentEntry)
        self.aLossPercentEntry.insert(0,int(2))  
        
        canvas1.create_window(250, lEntry, width=50, window=self.brokerageEntry)
        self.brokerageEntry.insert(0,float(0.3))
        
        lEntry = lEntry+60
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.iaEntry)
        canvas1.create_window(wEntry+50, lEntry+5, width=10, window=self.reqFieldsLabel1)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.bpEntry)
        canvas1.create_window(wEntry+50, lEntry+5, width=10, window=self.reqFieldsLabel2)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.fpEntry)
        canvas1.create_window(wEntry+50, lEntry+5, width=10, window=self.reqFieldsLabel3)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.slvEntry)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.npnlEntry)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.alEntry)
        lEntry = lEntry+30
        canvas1.create_window(wEntry, lEntry, width=entryWidth, window=self.nosEntry)

        calcButton = tk.Button(text='Calculate', command=self.getCalculation,bg='green',fg='white')
        canvas1.create_window(wButton, lEntry+50, window=calcButton)
        lEntry = lEntry+50

        helpButton = tk.Button(text='Help', command=self.open_guide,bg='black',fg='white')
        canvas1.create_window(windowWidth-30, windowHeight-20, window=helpButton)

        helpButton = tk.Button(text='SCTargeted', command=self.openShareCalcTargeted,bg='black',fg='white')
        canvas1.create_window(windowWidth-90, windowHeight-20, window=helpButton)

    def open_guide(self):
        os.startfile("share_calc_help.txt")

    def openShareCalcTargeted(self):
        import subprocess
        subprocess.Popen("python Share_calc_targeted.py")

    def record_values(self,inValues):
        try:
            f = open('record.csv','a')
            f.write(inValues + "\n")
            f.close()            
            mb.showinfo('Saved', 'values saved successfully in record.csv file!')
        except Exception as e:
            mb.showerror('Failed', e)
        

    def clear_widget_text(self,widget):
        widget['text'] = ""

    def test_values(self):
        self.iaEntry.insert(0,float("{:.2f}".format(50000)))
        self.bpEntry.insert(0,float("{:.2f}".format(30)))
        self.fpEntry.insert(0,float("{:.2f}".format(35)))

    def getCalculation (self):
        global lEntry
        temp = lEntry

        #clear lables so that new values dont overlap 
        self.clear_widget_text(self.marginLabel)
        self.clear_widget_text(self.plLabel)
        
        #clear entries before reasigning values
        self.slvEntry.delete(0,'end')
        self.alEntry.delete(0,'end')
        self.nosEntry.delete(0,'end')
        self.npnlEntry.delete(0,'end')
        
        bp = float(self.bpEntry.get())
        fp = float(self.fpEntry.get())
        ia = float(self.iaEntry.get())
        
        self.nosEntry.insert(0,int(ia//bp))

        nos = int(self.nosEntry.get())
        alPercent = float(self.aLossPercentEntry.get())

        self.alEntry.insert(0,int((alPercent/100)*ia))

        al = float(self.alEntry.get())        
        marginPercent = float(self.brokerageEntry.get())
        margin = (((marginPercent/100)*bp)+((marginPercent/100)*fp))*nos
        self.npnlEntry.insert(0,float("{:.2f}".format(((bp*nos)+margin)/nos)))
        self.marginLabel = tk.Label(root,text=str.format("Broker Margin (Rs): {0}",float("{:.2f}".format(margin))),fg='red')
        self.slvEntry.insert(0,float("{:.2f}".format((((bp*nos)+margin)-(al))/nos)))
        canvas1.create_window(150, temp+40, window=self.marginLabel)
        temp = temp + 40
        pl = float("{:.2f}".format(((fp-bp)*nos)-margin))
        self.plLabel = tk.Label(root, text= str.format("Profit/Loss (Rs) : {0}".format(pl)),fg='darkgreen')
        canvas1.create_window(150, temp+20, window=self.plLabel)
        temp=lEntry

        rv = "D" + str(datetime.now())+ "," + "," + str(ia) + "," + str(bp) + "," + str(fp) + "," + str(nos) + "," + str(margin) + "," + str(pl) + "," + "" +"," + "Share_calc"
        
        button1 = tk.Button(text='Save', command=lambda :self.record_values(rv),bg='black',fg='white')
        canvas1.create_window(windowWidth-150, windowHeight-20, window=button1)
        

if __name__ == "__main__":
    windowHeight = 450
    windowWidth = 300
    root = tk.Tk()
    root.title("Share Calculator")
    canvas1 = tk.Canvas(root, width = windowWidth, height = windowHeight)
    root.configure(background='red')
    canvas1.pack()
    stockWindow()
    root.mainloop()
   
