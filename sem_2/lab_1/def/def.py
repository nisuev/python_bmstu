# Из двоичной в десятичную и обратно

import tkinter as ttk


def to_dec():
    num = calculate.get()
    length = len(num) - 1
    dec_num = 0
    flag = None
    for i in num:
        if i not in '01':
            flag = True
            break
        dec_num += int(i) * (2 ** length)
        length -= 1
    if flag:
        return
    calculate.delete(0, ttk.END)
    if dec_num == 0:
        calculate.insert(0, '0')
    else:
        calculate.insert(0, str(dec_num))


def to_bin():
    num = calculate.get()
    num = int(num)
    bin_num = ''
    while num > 0:
        bin_num = str(num % 2) + bin_num
        num //= 2
    calculate.delete(0, ttk.END)
    if bin_num:
        calculate.insert(0, bin_num)
    else:
        calculate.insert(0, '0')


def num_add(digit):
    value = calculate.get()
    if len(value) == 0:
        value = '0'
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calculate.delete(0, ttk.END)
    calculate.insert(0, value + digit)


def dell():
    value = calculate.get()
    value = value[:-1]
    calculate.delete(0, ttk.END)
    if len(value) == 0:
        calculate.insert(0, 0)
    else:
        calculate.insert(0, value)


def press_key(event):
    if event.char.isdigit():
        num_add(event.char)
    if event.char == '\x1b':
        win.destroy()
    if event.char == '\x08':
        dell()


win = ttk.Tk()
win['bg'] = '#ffffff'

calculate = ttk.Entry(win, justify=ttk.RIGHT, font=('Arial', 25))
calculate.insert(0, 0)
calculate.grid(row=0, column=0, columnspan=2)

in_10 = ttk.Button(win, text='2 to 10',  bg='#7a7a7a', fg='#000000', font=('Arial', 15), bd=5,
                   command=lambda: to_dec())
in_10.grid(row=1, column=0, sticky='we')

in_2 = ttk.Button(win, text='10 to 2',  bg='#7a7a7a', fg='#000000', font=('Arial', 15), bd=5,
                  command=lambda: to_bin())
in_2.grid(row=1, column=1, sticky='we')
win.title('Calculator')
win.bind('<Key>', press_key)
win.mainloop()
