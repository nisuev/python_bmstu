import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as box
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from back import *
import numpy as np


# Функция работы вычислений
def start():
    # Проверка ввода функции
    funct = input_func.get()  # Функция
    try:
        if len(funct) == 0: 1 / 0
        fa(funct, 1)
    except:
        box.showinfo("Error", "Incorrect function")
        return
    # Получение значений
    try:
        a, b, h, n_max, eps = float(input_a.get()), float(input_b.get()), float(input_h.get()),\
            int(input_n_max.get()), float(input_eps.get())
    # Проверка на корректность ввода
    except:
        box.showinfo("Error", "Incorrect input")
        return
    if a > b:
        box.showinfo("Error", "b must be great or equal to a")
        return
    if h <= 0:
        box.showinfo("Error", "Incorrect range of h")
        return
    if eps < 0:
        box.showinfo("Error", "Incorrect range of eps")
        return
    if n_max < 0:
        box.showinfo("Error", "Incorrect range of N")
        return
    intervals = find_intervals(funct, a, b, h)  # Интервалы
    if intervals == 0:
        box.showinfo("Error", "Interval does not belong D(f)")
        return
    tables = tables_rows(funct, intervals, eps, n_max)  # Строки таблицы

    # Создание таблицы
    table = ttk.Treeview(window, columns=("num", "int", "x*", "fx*", "N", "code"), show="headings")
    table.grid(row=3, column=0, columnspan=6)
    headers = ["№ root", "interval", "x'", "f(x')", "N", "code"]
    table['columns'] = headers
    for i, header in enumerate(headers):
        table.heading(i, text=header, anchor=tk.CENTER)

    for header in headers:
        table.heading(header, text=header, anchor=tk.CENTER)
    for row in tables:
        table.insert("", tk.END, values=row)
    graph(a, b, funct)


# график
def graph(a, b, funct):
    plot = Figure()
    xy = plot.add_subplot()
    Ox = np.linspace(a, b, int((b - a) * 1000))

    Oy = np.array([f(funct, x) for x in Ox])
    diff1 = np.diff(Oy)
    diff2 = np.diff(diff1)

    zero = np.abs(Oy) < 1e-3
    extra = np.abs(diff1) < 1e-5
    infl = np.abs(diff2) < 1e-8

    xy.scatter(Ox[zero], Oy[zero], marker='o', color='#a60303', s=20, label="zeros")
    xy.scatter(Ox[:-1][extra], Oy[:-1][extra], marker='x', color='#248201', s=40, label="extremes")
    xy.scatter(Ox[:-2][infl], Oy[:-2][infl], marker='|', color='#ba32a4', s=40, label="inflection points")

    xy.plot(Ox, Oy, color="#000000")

    xy.legend()
    xy.grid()
    xy.set_ylabel(funct)
    xy.set_xlabel("x")
    grafic = FigureCanvasTkAgg(plot, window)
    grafic.draw()
    grafic.get_tk_widget().grid(row=6, column=0, rowspan=3, columnspan=6, stick='wnes')


# Информационное поле
def info():
    box.showinfo('Error codes',
                 "0 - root's found: OK\n"
                 "1 - too many iterations\n"
                 "2 - out of the interval\n"
                 "3- devision by zero f`(x)")


# Информация об авторе
def avtor():
    info = tk.Tk()
    info.title("info")
    txt = 'Autor: Nisuev Nisu Felixsovich IU7-22B\n' + \
          '-' * 38 + '\n' \
          'root table and graphic'
    label = tk.Label(info, text=txt, font=('Arial', 12), fg='#ffffff', bg='#2a2b2e')
    label.grid()
    info.mainloop()


# Нажатия на клавиши
def press_key(event):
    if event.char == '\r':
        start()
    if event.char == 'h':
        avtor()


# Создание окна
window = tk.Tk()
window.resizable(None, None)
window['bg'] = '#2e2e2e'

window.bind('<Key>', press_key)  # Бинд ввода с клавиатуры

# заголовок
window.title('func')

# Меню
mainmenu = tk.Menu(window)
window.config(menu=mainmenu)

mainmenu.add_command(label='Code info', command=lambda: info())
mainmenu.configure(bg='#2a2b2e', font='Arial', fg='#e6e9f0')

mainmenu.add_command(label='About programm', command=lambda: avtor())
mainmenu.configure(bg='#2a2b2e', font='Arial', fg='#e6e9f0')

# создание наименований полей ввода
func_col = tk.Label(window, text='f(x):', bg='#2e2e2e', fg='#ffffff')
func_col.grid(row=0, column=0)

col_a = tk.Label(window, text='a:', bg='#2e2e2e', fg='#ffffff')
col_a.grid(row=0, column=1)

name_b = tk.Label(window, text='b:', bg='#2e2e2e', fg='#ffffff')
name_b.grid(row=0, column=2)

name_h = tk.Label(window, text='h:', bg='#2e2e2e', fg='#ffffff')
name_h.grid(row=0, column=3)

name_n_max = tk.Label(window, text='n_max:', bg='#2e2e2e', fg='#ffffff')
name_n_max.grid(row=0, column=4)

name_eps = tk.Label(window, text='eps:', bg='#2e2e2e', fg='#ffffff')
name_eps.grid(row=0, column=5)

# Создание полей ввода значений
input_func = tk.Entry(window)
input_func.grid(row=1, column=0)

input_a = tk.Entry(window)
input_a.grid(row=1, column=1)

input_b = tk.Entry(window)
input_b.grid(row=1, column=2)

input_h = tk.Entry(window)
input_h.grid(row=1, column=3)

input_n_max = tk.Entry(window)
input_n_max.grid(row=1, column=4)

input_eps = tk.Entry(window)
input_eps.grid(row=1, column=5)

# Кнопка старт
enter_button = tk.Button(text='start', bg='#8ab1ff', fg='#2e2e2e', bd=5, font=('Arial', 12, 'bold'),
                         command=lambda: start())
enter_button.grid(row=2, column=0, columnspan=6, stick='we')

# Отрисовка изначальной таблицы
table = ttk.Treeview(window, columns=("num", "int", "x*", "fx*", "N", "code"), show="headings")
table.grid(row=3, column=0, columnspan=6)
headers = ["№ root", "interval", "x'", "f(x')", "N", "code"]
table['columns'] = headers
for i, header in enumerate(headers):
    table.heading(i, text=header, anchor=tk.CENTER)

for header in headers:
    table.heading(header, text=header)

# Форматирование колонок
for col in range(6):
    window.grid_columnconfigure(col, minsize=30)

# Форматирование рядов
for row in range(2):
    window.grid_rowconfigure(row, minsize=30)

# запуск обработчика обытий
window.mainloop()
