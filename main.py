import tkinter as tk
from tkinter import ttk
from tkinter import * 
import os

def btnClickFunction():
	os.system('py Justinejjjj.py')

root = Tk()

root.geometry('1000x650')
root.configure(background='white')
root.resizable(width=False, height=False)
root.title('Justine AI Assistant')
root.iconbitmap('images\\Voiceassistant.ico')
bg = PhotoImage(file=r"images\\piccttt.PNG")
micon=tk.PhotoImage(file=r"images\\noun_mic.png")
ex=tk.PhotoImage(file=r"images\\exit.png")
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)

Button(root, text='Click Me', image=micon, bg='#acc1bf', font=('arial', 35, 'normal'), command=btnClickFunction, borderwidth=0).place(x=478, y=290)
Button(root, text='Exit', image=ex, bg='white', font=('arial', 12, 'normal'), command=root.destroy, borderwidth=0).place(x=482, y=570)

root.mainloop()