import os
from tkinter import *

root = Tk()
root.title("Justine")
root.configure(background='white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")

main= Frame(root)
main.grid()

class start():
    def button():
        b = Button(main, text='Click Me', command=main.onclick,compound=TOP)
        b.pack()
    def onclick():
        os.system('py Justine.py')

if __name__ == '__main__':
    main.mainloop()
