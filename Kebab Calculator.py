from tkinter import *
import webbrowser
from tkinter import messagebox as mb
from decimal import Decimal

itog = 0  # Кол-во кг
A = 0.6  # Мужчина 90+
B = 0.5  # Мужчины 90-
C = 0.5  # Женщины 70+
D = 0.4  # Женщины 70-
E = 0.3  # Дети

colA = 0
colB = 0
colC = 0
colD = 0
colE = 0


def order():
    webbrowser.open('https://shashlik1.ru/menyu', new=2)


def manmax():
    global a, A, colA
    try:
        a = int(EntryA.get())
        colA = A * a
    except ValueError:
        mb.showerror('Ошибка', "Из-за вашей невнимательности несколько мужчин остались без шашлыка :(")
        EntryA.delete(0, END)


def manmin():
    global b, B, colB
    try:
        b = int(EntryB.get())
        colB = B * b
    except ValueError:
        mb.showerror('Ошибка', "Из-за вашей невнимательности несколько парней остались без шашлыка :(")
        EntryB.delete(0, END)


def womanmax():
    global c, C, colC
    try:
        c = int(EntryC.get())
        colC = C * c
    except ValueError:
        mb.showerror('Ошибка', "Из-за вашей невнимательности несколько женщин остались без шашлыка :(")
        EntryC.delete(0, END)


def womanmin():
    global d, D, colD
    try:
        d = int(EntryD.get())
        colD = D * d
    except ValueError:
        mb.showerror('Ошибка', "Из-за вашей невнимательности несколько девушек остались без шашлыка :(")
        EntryD.delete(0, END)


def children():
    global e, E, colE
    try:
        e = int(EntryE.get())
        colE = E * e
    except ValueError:
        mb.showerror('Ошибка', "Из-за вашей невнимательности несколько детей остались без шашлыка :(")
        EntryE.delete(0, END)


def clean():
    global colA, colB, colC, colD, colE, itog
    EntryA.delete(0, END)
    EntryB.delete(0, END)
    EntryC.delete(0, END)
    EntryD.delete(0, END)
    EntryE.delete(0, END)
    var1.set(0)
    colA = 0
    colB = 0
    colC = 0
    colD = 0
    colE = 0
    itog = 0


def schitat():
    global colA, colB, colC, colD, colE, itog
    manmax()
    manmin()
    womanmin()
    womanmax()
    children()
    ab = Toplevel()
    # ab.geometry('200x150+400+225')
    ab.iconbitmap(r'C:\Users\USER\PycharmProjects\Work\ООП\barb2.ico')
    Label(ab, text="                Вам понадобится                ", font='Arial 12').grid(row=0, column=1,
                                                                                            columnspan=2)
    itog = colA + colB + colC + colD + colE + var1.get()
    Label(ab, text='  ').grid(row=1, column=2)
    Label(ab, text=Decimal(itog).normalize().__round__(1), font='Bold 32').grid(row=2, column=1, columnspan=2)
    Label(ab, text='  ').grid(row=3, column=2)
    Label(ab, text="                кг шашлыка!                ", font='Arial 12').grid(row=4, column=1, columnspan=2)
    Label(ab, text='  ').grid(row=5, column=2)
    abc = Button(ab, text='Oк', width=15, height=2, font='Arial 10', bg='Moccasin', fg='Black',
                 command=ab.destroy).grid(row=6, column=1, columnspan=2)
    Label(ab, text='  ').grid(row=7, column=2)


root = Tk()
root.iconbitmap(r'C:\Users\USER\PycharmProjects\Work\ООП\barb2.ico')
root.title('Калькулятор шашлыка')

Label(root, text='Число мужчин, весом больше 90 кг:        ', font='Arial 12').grid(row=0, column=0)
EntryA = Entry(root, width=15, font='Arial 14', justify="center")
EntryA.grid(row=1, column=0)
Label(root, text='Число мужчин, весом меньше 90 кг:        ', font='Arial 12').grid(row=0, column=1)
EntryB = Entry(root, width=15, font='Arial 14', justify="center")
EntryB.grid(row=1, column=1)
Label(root, text='  ').grid(row=2, column=0)

Label(root, text='Число женщин, весом больше 70 кг:        ', font='Arial 12').grid(row=3, column=0)
EntryC = Entry(root, width=15, font='Arial 14', justify="center")
EntryC.grid(row=4, column=0)
Label(root, text='Число женщин, весом меньше 70 кг:        ', font='Arial 12').grid(row=3, column=1)
EntryD = Entry(root, width=15, font='Arial 14', justify="center")
EntryD.grid(row=4, column=1)
Label(root, text='  ').grid(row=5, column=0, columnspan=2)

Label(root, text='Число детей:', font='Arial 12').grid(row=6, column=0, columnspan=2)
EntryE = Entry(root, width=15, font='Arial 14', justify="center")
EntryE.grid(row=7, column=0, columnspan=2)
Label(root, text='  ').grid(row=8, column=0, columnspan=2)

var1 = IntVar()
var1.set(0)
c1 = Checkbutton(root, text="С нами Семён", font='Arial 12', variable=var1, onvalue=1, offvalue=0)
c1.grid(row=9, column=0, columnspan=2)

Schitat = Button(root, text='Посчитать', width=15, height=2, font='Arial 10', bg='Moccasin', fg='Black',
                 command=schitat).grid(row=11, column=0)
Clean = Button(root, text='Очистить поля', width=15, height=2, font='Arial 10', bg='Moccasin', fg='Black',
               command=clean).grid(row=11, column=1)

button1 = Button(root, text='Купить шашлычок!', width=30, height=2, font='Arial 10', bg='Moccasin', fg='Black',
                 command=order).grid(row=13, column=0, columnspan=4)
Label(root, text='  ').grid(row=10, column=0, columnspan=2)
Label(root, text='  ').grid(row=12, column=0, columnspan=2)
Label(root, text='  ').grid(row=14, column=0, columnspan=2)

root.resizable(False, False)
root.mainloop()
