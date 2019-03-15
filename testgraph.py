import json
import requests
import time
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk


LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

# f = Figure(figsize=(5,5), dpi=100)
# a = f.add_subplot(111)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
    
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        frame = StartPage(container, self)
        
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
         
    def show_frame(self, cont):
    
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Network Traffic", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        pullData = open("tester.csv","r").read()
        dataList = pullData.split('\n')
        xPkt = []
        yPkt = []
        xB = []
        yB = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y, i, j = eachLine.split(',')
                xPkt.append(int(x))
                yPkt.append(int(y))
                xB.append(int(i))
                yB.append(int(j))
                
                a.clear()
                a.plot(xPkt)
                a.plot(yPkt)
                a.plot(xB)
                a.plot(yB)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()
        
        # sself.ani = animation.FuncAnimation(f, self.animate, interval=1000)
        
    def animate():
        pullData = open("tester.txt","r").read()
        dataList = pullData.split('\n')
        xPkt = []
        yPkt = []
        xB = []
        yB = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',\"')
                xPkt.append(int(x))
                yPkt.append(int(y))
                
                a.clear()
                a.plot(xPkt, yPkt)

app = SeaofBTCapp()
#ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
