from tkinter import *
import os


def printText():
    os.startfile(r'C:\Users\USER\Desktop\Untitled.mp4')


root = Tk()
button1 = Button(root, text='Magic!', width=10, height=2, font='Arial', bg='Moccasin', fg='Dark Slate Gray', command=printText)
button1.bind('<Button-1>', printText)
root.geometry('300x100+550+350')


button1.pack()
root.mainloop()
