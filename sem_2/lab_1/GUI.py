import tkinter as ttk
from calculation import *


def add_label():
    title = 'Информационное поле\n--------------------------------------\n'
    txt = 'Автор: Нисуев Нису Феликсович ИУ7-22Б\nКалькулятор\nтроично-симметричной с/с вида (i,0,1)\n'
    end = '--------------------------------------'
    label = ttk.Label(window, text=title+txt+end, font=('Arial', 12), fg='#ffffff', bg='#000000')
    label.grid(columnspan=4)
    labels_list.append(label)


def destroy_label():
    if labels_list:  # удалить последнюю
        labels_list.pop().destroy()


labels_list = []


# Функция для записи дробной части
def flt_part():
    value = calc.get()
    if value.count('+'):
        values = value.split('+')
    elif value.count('-'):
        values = value.split('-')
    else:
        values = [value]

    if values[-1].count('.') != 0 or len(values[-1]) == 0:
        return
    calc.delete(0, ttk.END)
    calc.insert(0, value + '.')


#  Функция удаления 1-ого элемента
def dell_last():
    value = calc.get()
    value = value[:-1]
    calc.delete(0, ttk.END)
    calc.insert(0, value)
    if len(value) == 0:
        calc.insert(0, '0')


# Функция удаления строки
def del_all():
    calc.delete(0, ttk.END)
    calc.insert(0, '0')


# Функция для записи чисел
def calc_num(digit):
    value = calc.get()
    if len(value) == 0:
        value = '0'
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, ttk.END)
    calc.insert(0, value + digit)


# Функция для записи алгеброических описаний операций
def calc_operation(operation):
    value = calc.get()
    if len(value) == 0:
        value = '0'
    if value[-1] in '-+' or value[-1] == '.':
        value = value[:-1]
    if value.count('+') or value.count('-'):
        return
    calc.delete(0, ttk.END)
    calc.insert(0, value + operation)


# Функция подсчета
def calc_result():
    value = calc.get()
    if value.count('+'):
        sign = '+'
        values = value.split('+')
    elif value.count('-'):
        sign = '-'
        values = value.split('-')
    else:
        values = [value]

    if len(values) == 1:
        return

    if sign == '+':
        ans = trial_sum(values[0], values[-1])
    if sign == '-':
        ans = trial_sub(values[0], values[-1])
    calc.delete(0, ttk.END)
    calc.insert(0, ans)


# Функция работы с кнопками
def make_operation(operation):
    operators = '+-'
    result = '='
    nums = 'i01'
    flt = '.'
    del_commad = ['C', 'DEL']
    if operation == result:
        return ttk.Button(text=operation, bg='#3d0101', fg='#ffffff', bd=0, font=('Arial', 20),
                          command=lambda: calc_result())
    if operation in operators:
        return ttk.Button(text=operation, bg='#3d0101', fg='#ffffff', bd=0, font=('Arial', 20),
                          command=lambda: calc_operation(operation))
    if operation in nums:
        return ttk.Button(text=operation, bg='#1f1f1f', fg='#ffffff', bd=0, font=('Arial', 20),
                          command=lambda: calc_num(operation))
    if operation == flt:
        return ttk.Button(text=operation, bg='#1f1f1f', fg='#ffffff', bd=0, font=('Arial', 20),
                          command=lambda: flt_part())
    if operation in del_commad:
        if operation == 'C':
            return ttk.Button(text=operation, bg='#737373', fg='#000000', bd=0, font=('Arial', 20),
                              command=lambda: del_all())
        if operation == 'DEL':
            return ttk.Button(text=operation, bg='#737373', fg='#000000', bd=0, font=('Arial', 20),
                              command=lambda: dell_last())


# Ввод с клавиатуры
def press_key(event):
    nums = 'i01'
    operations = '+-'
    if event.keysym == 'Shift_R' or event.keysym == 'Shift_L':
        return
    if event.char in nums:
        calc_num(event.char)
    if event.char in operations:
        calc_operation(event.char)
    if event.char in '.':
        flt_part()
    if event.char == '\r' or event.char == '=':
        calc_result()
    if event.char in '\x08':
        dell_last()
    if event.char == '\x1b':
        window.destroy()
    if event.char == 'h':
        if len(labels_list) < 1:
            add_label()
        else:
            destroy_label()


# Создание окна калькулятора
window = ttk.Tk()
window.title("Калькулятор троично-симметричной ОС")
window.resizable(None, None)
window['bg'] = '#000000'

window.bind('<Key>', press_key)  # Бинд ввода с клавиатуры

# Создание окна ввода
calc = ttk.Entry(window, justify=ttk.RIGHT, font=('Arial', 28), width=15, bg='#000000', fg='#ffffff', bd=0)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='wens', padx=5, pady=5)

# Форматирование кнопок удаления
make_operation('C').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_operation('DEL').grid(row=1, column=1, columnspan=2, stick='wens', padx=5, pady=5)

# Форматирование кнопок цифр
make_operation('i').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_operation('0').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_operation('1').grid(row=2, column=2, stick='wens', padx=5, pady=5)

# Форматирование кнопки для создания дробного числа
make_operation('.').grid(row=3, column=1, stick='wens', padx=5, pady=5)

# Форматирование кнопок операций
make_operation('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation('=').grid(row=3, column=3, stick='wens', padx=5, pady=5)


# Форматирование колонок
for col in range(4):
    window.grid_columnconfigure(col, minsize=80)

# Форматирование рядов
for row in range(4):
    window.grid_rowconfigure(row, minsize=80)

window.mainloop()
