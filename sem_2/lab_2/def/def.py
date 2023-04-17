import tkinter as tk
from math import *


def f(x):
    return eval(input_func.get())


def half_root(a, b, eps):
    # метод половинного деления
    iter = 0
    while (b - a) / 2 > eps:
        if iter == 10:
            return 0
        c = (a + b) / 2
        if f(c) == 0:
            return f(c), c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter += 1
    return f((a + b) / 2), (a + b) / 2


def start():
    beg, end, eps = float(input_beg.get()), float(input_end.get()), float(input_eps.get())
    ans = half_root(beg, end, eps)
    x = tk.Label(window, text='x: {:<9.4g}\nf(x): {:<9.4g}'.format(ans[0], ans[1]), bg='#212121', fg='#b8860b')
    x.grid(row=3, column=0, columnspan=4, sticky='we')


window = tk.Tk()
window.resizable(None, None)
window.title('defenition')
window['bg'] = '#b8860b'

func_col = tk.Label(window, text='f(x):', bg='#b8860b', fg='#212121')
func_col.grid(row=0, column=0)

col_beg = tk.Label(window, text='begin:', bg='#b8860b', fg='#212121')
col_beg.grid(row=0, column=1)

name_end = tk.Label(window, text='end:', bg='#b8860b', fg='#212121')
name_end.grid(row=0, column=2)

name_eps = tk.Label(window, text='eps:', bg='#b8860b', fg='#212121')
name_eps.grid(row=0, column=3)

# Создание полей ввода значений
input_func = tk.Entry(window, bg='#212121', fg='#b8860b')
input_func.grid(row=1, column=0)

input_beg = tk.Entry(window, bg='#212121', fg='#b8860b')
input_beg.grid(row=1, column=1)

input_end = tk.Entry(window, bg='#212121', fg='#b8860b')
input_end.grid(row=1, column=2)

input_eps = tk.Entry(window, bg='#212121', fg='#b8860b')
input_eps.grid(row=1, column=3)

enter_button = tk.Button(text='find root', bg='#212121', fg='#b8860b', bd=0, font=('Calibri', 12, 'bold'),
                         command=lambda: start())
enter_button.grid(row=2, column=0, columnspan=6, sticky='we')
window.mainloop()
