from tkinter import *

root = Tk()
root["bg"] = "medium purple"
Label(text="Введите задуманное число", font="Arial 16").grid(row=0, column=0)
e1 = Entry(width=10).grid(row=0, column=1, sticky=W)
b1 = Button(text="Запустить бинарный поиск", width=24, height=3, bg='LightBlue3').grid(row=1, pady=20, columnspan=3, column=0)
Label(text="Предлагаемый вариант:", font="Arial 16").grid(row=2, column=0, sticky=W)
b2 = Button(text="Больше", width=15, height=3, bg='khaki3').grid(row=3, pady=20, sticky=W, columnspan=3, column=0)
b3 = Button(text="Меньше", width=15, height=3, bg='khaki3').grid(row=3, pady=20, columnspan=3, column=0)
b4 = Button(text="Угадал", width=15, height=3, bg='khaki3').grid(row=3, pady=20, sticky=E, columnspan=3, column=0)
Label(text="Количество попыток:", font="Arial 16").grid(row=4, column=0, sticky=W)
b5 = Button(text="Об алгоритме", width=30, height=3, bg='DarkSeaGreen1').grid(row=5, pady=20, sticky=W, columnspan=2,
                                                                              column=0)
b6 = Button(text="Очистить", width=14, height=3, bg='DarkSeaGreen1').grid(row=5, pady=20, sticky=E, columnspan=3,
                                                                          column=0)


def __init__(self):
    self.a = 0
    self.b = 1000
    c = int(e1.get())
    self.mid = 0
    self.k = 0
    return self.mid


def bolshe(self):
    self.a = mid
    self.mid = (self.a + self.b) // 2
    return self.mid


def menshe(self):
    self.b = mid
    self.mid = (self.a + self.b) // 2
    return self.mid


root.mainloop()

