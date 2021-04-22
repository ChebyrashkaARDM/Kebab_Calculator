from tkinter import *
from tkinter import messagebox as mb


def Proizvedenie():
    a = int(EntryA.get())
    b = int(EntryB.get())
    result = str(a * b)
    EntryC.delete(0, END)
    EntryC.insert(0, result)


def Delenie():
    a = int(EntryA.get())
    b = int(EntryB.get())
    if b == 0:
        mb.showerror('Ошибка', 'На 0 делить нельзя')
    else:
        result = str(a / b)
        EntryC.delete(0, END)
        EntryC.insert(0, result)


def Summ():
    a = int(EntryA.get())
    b = int(EntryB.get())
    result = str(a + b)
    EntryC.delete(0, END)
    EntryC.insert(0, result)


def Minus():
    a = int(EntryA.get())
    b = int(EntryB.get())
    result = str(a - b)
    EntryC.delete(0, END)
    EntryC.insert(0, result)


def Clean():
    EntryA.delete(0, END)
    EntryB.delete(0, END)
    EntryC.delete(0, END)


root = Tk()
#root.geometry('500x250+400+200')
root.title('Калькулятор')
Label(root, text='Первое число:').grid(row=0, sticky=W)
Label(root, text='Второе число:').grid(row=1, sticky=W)


EntryA = Entry(root, width=10, font='Arial 20', justify="center")
EntryB = Entry(root, width=10, font='Arial 20', justify="center")
EntryC = Entry(root, width=20, font='Arial 20', justify="center", state="normal")
EntryA.grid(row=0, column=1, columnspan=3, sticky=E)
EntryB.grid(row=1, column=1, columnspan=3, sticky=E)
EntryC.grid(row=2, columnspan=4)


but1 = Button(root, text='Произведение', command=Proizvedenie)
but2 = Button(root, text='Сумма', command=Summ)
but3 = Button(root, text='Частное', command=Delenie)
but4 = Button(root, text='Вычитание', command=Minus)
but5 = Button(root, text='Очистить', command=Clean)


but1.grid(row=3, column=0, sticky='W')
but2.grid(row=3, column=1, sticky='W')
but3.grid(row=3, column=2, sticky='W')
but4.grid(row=3, column=3, sticky='W')
but5.grid(row=4, column=0, columnspan=4)


root.mainloop()
