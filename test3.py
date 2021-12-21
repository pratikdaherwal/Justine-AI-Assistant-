import tkinter as tk
from tkinter import *
import os
from tkinter.constants import TOP


def onclick():
    os.system('py Justinejjjj.py')

if __name__=='__main__':
    r = tk.Tk()
    r.title('Justine')
    r.iconbitmap('images\\youtube-ios-app.ico')
    r.geometry("980x568+90+90")
    r.resizable(width=False, height=False)
    pic= tk.PhotoImage(file=r"C:\Users\BeingMF\Desktop\pujhkuiicttt.png")
    micon=tk.PhotoImage(file=r"C:\Users\BeingMF\Desktop\micicon.png")
    a=tk.Label(r,text="fddefer", image=pic).pack(side=TOP)
    spacer1 = tk.Label(r, text="")
    spacer1.pack()
    spacer2 = tk.Label(r, text="")
    spacer2.pack()
    button = tk.Button(r, text='Click Me', image=micon, command=onclick)
    button.pack()
    spacer3 = tk.Label(r, text="")
    spacer3.pack()
    spacer4 = tk.Label(r, text="")
    spacer4.pack()
    b = tk.Button(r, text='Exit', width=6, command=r.destroy)
    b.pack()

r.mainloop()