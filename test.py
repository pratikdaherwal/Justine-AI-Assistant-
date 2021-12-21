import tkinter as tk
from tkinter import ttk
from tkinter import * 
import os

# this is the function called when the button is clicked
def btnClickFunction():
	os.system('py Justinejjjj.py')

root = Tk()

root.geometry('1000x650')
root.configure(background='white')
root.title('Justine')
bg = PhotoImage(file=r"C:\Users\BeingMF\Desktop\piccttt.PNG")
micon=tk.PhotoImage(file=r"C:\Users\BeingMF\Desktop\micicon.png")

label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)

Button(root, text='Click Me', image=micon, bg='#F0F8FF', font=('arial', 35, 'normal'), command=btnClickFunction).place(x=450, y=266)
Button(root, text='Exit', bg='#F0F8FF', font=('arial', 12, 'normal'), command=root.destroy).place(x=482, y=575)

root.mainloop()
