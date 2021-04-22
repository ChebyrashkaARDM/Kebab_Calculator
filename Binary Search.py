from tkinter import *
from tkinter import messagebox as mb

min = -1
max = 1001
mid = 500
count = 1


def start():
    global a, LabelB, CountLabel
    try:
        a = int(NumEntry.get())
        LabelB = Label(root, text='      ', width=10, font='Arial 12').grid(row=2, column=1)
        LabelB = Label(root, text=str(mid), width=10, font='Arial 12').grid(row=2, column=1)
        CountLabel = Label(root, text='        ', width=10, font='Arial 12').grid(row=4, column=1)
        CountLabel = Label(root, text=str(count), width=10, font='Arial 12').grid(row=4, column=1)
    except ValueError:
        mb.showerror('Error', "It's not an integer number")
        NumEntry.delete(0, END)


def Up():
    global min, max, mid, count, LabelB, CountLabel
    min = mid
    mid = (min + max) // 2
    LabelB = Label(root, text='      ', width=10, font='Arial 12').grid(row=2, column=1)
    LabelB = Label(root, text=str(mid), width=10, font='Arial 12').grid(row=2, column=1)
    count += 1
    CountLabel = Label(root, text='        ', width=10, font='Arial 12').grid(row=4, column=1)
    CountLabel = Label(root, text=str(count), width=10, font='Arial 12').grid(row=4, column=1)
    if int(a) > max or int(a) < min:
        mb.showerror('Error', "Think again")
        LabelB = Label(root, text='      ', font='Arial 18', width=23).grid(row=2, column=1)
        LabelB = Label(root, text=str(mid), font='Arial 18', width=23).grid(row=2, column=1)
        CountLabel = Label(root, text='        ', width=10, font='Arial 12').grid(row=4, column=1)
        min = -1
        max = 1001
        mid = 500
        count = 1


def Down():
    global min, max, mid, count, LabelB, CountLabel
    max = mid
    mid = (min + max) // 2
    LabelB = Label(root, text='     ', width=10, font='Arial 12').grid(row=2, column=1)
    LabelB = Label(root, text=str(mid), width=10, font='Arial 12').grid(row=2, column=1)
    count += 1
    CountLabel = Label(root, text='        ', width=10, font='Arial 12').grid(row=4, column=1)
    CountLabel = Label(root, text=str(count), width=10, font='Arial 12').grid(row=4, column=1)
    if int(a) > max or int(a) < min:
        mb.showerror('Error', "Think again")
        LabelB = Label(root, text='     ', width=10, font='Arial 12').grid(row=2, column=1)
        CountLabel = Label(root, text='        ', width=10, font='Arial 12').grid(row=3, column=1)
        min = -1
        max = 1000
        mid = 500
        count = 1


def Equal():
    global a, mid, LabelB, CountLabel
    if int(a) == int(mid):
        mb.showinfo(title='Win!', message='Congratulations!')
        LabelB = Label(root, text='       ', width=10, font='Arial 12').grid(row=2, column=1)
        CountLabel = Label(root, text='        ', width=10, font='Arial 12').grid(row=4, column=1)
    else:
        mb.showinfo(title='Oops!', message="It's wrong!")


def Clean():
    global min, max, mid, count, LabelB, CountLabel
    count = 1
    min = -1
    max = 1001
    mid = 500
    NumEntry.delete(0, END)
    LabelB = Label(root, text='       ', width=10, font='Arial 12').grid(row=2, column=1)
    CountLabel = Label(root, text='        ', width=10, font='Arial 12').grid(row=4, column=1)


def About():
    ab = Toplevel()
    ab.geometry('200x150')
    ab['bg'] = 'grey'
    Label(ab, text="Binary search").pack(expand=1)


root = Tk()
root.title('Binary Search')

Label(root, text='Enter your number:', font='Arial 18', width=23).grid(row=0, column=0)
NumEntry = Entry(root, width=15, font='Arial 14')
NumEntry.grid(row=0, column=1, columnspan=3)

start = Button(root, text='Start', height=2, width=20, font='Arial 8', command=start).grid(row=1, column=1, columnspan=3)

Label(root, text='Suggestion:', font='Arial 18', width=23).grid(row=2, column=0, columnspan=3, sticky=W)
Label(root, text='Count:', font='Arial 18', width=23).grid(row=4, column=0, columnspan=3, sticky=W)
CountLabel = Label(root, width=10, font='Arial 12').grid(row=4, column=1)

LabelB = Label(root, width=10, font='Arial 12').grid(row=2, column=1)

Equality = Button(root, text='Guessed', height=2, width=20, font='Arial 8', command=Equal).grid(row=3, column=0, sticky='W')
Menshe = Button(root, text='Less', height=2, width=20, font='Arial 8', command=Down).grid(row=3, column=1, sticky='E')
Bolshe = Button(root, text='More', height=2, width=20, font='Arial 8', command=Up).grid(row=3, column=2, sticky='E')

but1 = Button(root, text='About', height=4, width=15, font='Arial 8', command=About).grid(row=5, column=0, sticky='W')
but2 = Button(root, text='Clean', height=4, width=20, font='Arial 8', command=Clean).grid(row=5, column=1, sticky='W')

root.mainloop()
