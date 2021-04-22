from tkinter import *
import webbrowser
from tkinter import messagebox as mb

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

def manmax():
    global a, A, colA
    a = int(EntryA.get())
    colA = A * a


def manmin():
    global b, B, colB
    b = int(EntryB.get())
    colB = B * b


def womanmax():
    global c, C, colC
    c = int(EntryC.get())
    colC = C * c

def womanmin():
    global d, D, colD
    d = int(EntryD.get())
    colD = D * d


def children():
    global e, E, colE
    e = int(EntryE.get())
    colE = E * e


def order():
    webbrowser.open('https://shashlik1.ru/menyu', new=2)


def clean():
    global colA, colB, colC, colD, colE, itog
    EntryA.delete(0, END)
    EntryB.delete(0, END)
    EntryC.delete(0, END)
    EntryD.delete(0, END)
    EntryE.delete(0, END)
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
    ab.geometry('200x150')
    ab['bg'] = 'grey'
    Label(ab, text="Вам понадобится").pack(expand=1)
    itog = colA + colB + colC + colD + colE
    Label(ab, text=str(itog)).pack(expand=2)



root = Tk()
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

button1 = Button(root, text='Купить шашлычок!', width=30, height=2, font='Arial 10', bg='Moccasin', fg='Black',
                 command=order).grid(row=11, column=0, columnspan=4)  # Расположить в самом низу
Label(root, text='  ').grid(row=10, column=0, columnspan=2)

Schitat = Button(root, text='Посчитать', width=15, height=2, font='Arial 10', bg='Moccasin', fg='Black',
                 command=schitat).grid(row=9, column=0)
Clean = Button(root, text='Очистить поля', width=15, height=2, font='Arial 10', bg='Moccasin', fg='Black',
               command=clean).grid(row=9, column=1)

# Label(root, text=str(itog), font='Arial 12').grid(row=10, column=0, columnspan=2) #ДОБАВИТЬ В ОТДЕЛЬНОЕ ОКНО РЕЗУЛЬТАТ ШАШЛЫКА


root.mainloop()
