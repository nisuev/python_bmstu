import tkinter as tk
from tkinter import ttk
from re import match
from os import listdir
from PIL import Image
from tkinter import messagebox as box
from back import *


# Функция создания иверсивной картинки
def inverse_pict():
    file = filename.get()
    if len(file) == 0:
        box.showinfo('Error', "No file chosen")
        return
    try:
        image = Image.open(file)
    except FileNotFoundError:
        box.showinfo('Error', "No such file")
        return

    size = list(image.size)
    pixels = list(image.getdata())

    pixels = inverse(size, pixels)
    wen_elif = file[:-4][::-1] + ".bmp"
    image.close()
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(pixels)
    new_image.save(file[:-4][::-1] + ".bmp")
    entry_file["values"] = list(filter(lambda filee: match(r'.*\.bmp', filee), listdir()))
    box.showinfo('New file', f"New file: {wen_elif} was successfully created")


# Функция создания файла с отрисованными линиями
def draw_line(wr_col, wr_lin):
    if wr_col is None:
        box.showinfo('Error', "No choosing color")
        return
    if len(wr_lin) == 0:
        box.showinfo('Error', "No write lines")
        return
    file = filename.get()
    if len(file) == 0:
        box.showinfo('Error', "No file chosen")
        return
    try:
        image = Image.open(file)
    except FileNotFoundError:
        box.showinfo('Error', "No such file")
        return
    size = list(image.size)
    pixels = list(image.getdata())
    pix_mat = []
    for i in range(size[1]):
        pix_mat.append(pixels[size[0] * i: size[0] * (i + 1)])

    line_funcs = {'/': lambda: write_right_line(size, pix_mat, wr_col),
                  '|': lambda: write_up_line(size, pix_mat, wr_col),
                  '\\': lambda: write_left_line(size, pix_mat, wr_col),
                  '-': lambda: write_hor_line(size, pix_mat, wr_col)}

    for i in wr_lin:
        pix_mat = list(line_funcs[i]())
    pixels = []
    for i in range(len(pix_mat)):
        for j in pix_mat[i]:
            pixels.append(j)

    new_file = file[:-4]
    if '_net' in new_file:
        new_file += 't'
    else:
        new_file += '_net'
    image.close()
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(pixels)
    new_image.save(new_file + '.bmp')
    entry_file["values"] = list(filter(lambda filee: match(r'.*\.bmp', filee), listdir()))
    box.showinfo('File', f"New file: {new_file}.bmp was successfully created")
    update()


# Функция обновляет данные после создания нового файла
def update():
    global choose_lin, choose_col, color, lines
    color = None
    lines = ''

    choose_lin.destroy()
    choose_col.destroy()

    choose_col = tk.Label(window, text="-", font=('Calibri', 12, 'bold'), fg='#ffffff', bg='#303030')
    choose_col.grid(row=3, column=3, columnspan=2, padx=5, pady=5)

    choose_lin = tk.Label(window, text="0", font=('Calibri', 12, 'bold'), fg='#ffffff', bg='#303030')
    choose_lin.grid(row=5, column=3, columnspan=2, padx=5, pady=5)


# Функция выбора цвета
def chose_color(num):
    colors = [tuple([255, 0, 0]), tuple([0, 255, 0]), tuple([0, 0, 255]), tuple([255, 255, 255]), tuple([0, 0, 0])]
    str_color = ['Red', 'Green', 'Blue', 'White', 'Black']
    fg_color = ['#ff0000', '#00ff00', '#5061fa', '#ffffff', '#000000']
    global color, choose_col
    color = colors[num]
    choose_col.destroy()
    choose_col = tk.Label(window, text=str_color[num], font=('Calibri', 12, 'bold'), fg=fg_color[num], bg='#303030')
    choose_col.grid(row=3, column=3, columnspan=2, padx=5, pady=5)


# Функция выбора построения линий
def chose_lines(num):
    _lines = ['|', '\\', '-', '/']
    global lines, choose_lin
    if num == 4:
        choose_lin.destroy()
        choose_lin = tk.Label(window, text="0", font=('Calibri', 12, 'bold'), fg='#ffffff', bg='#303030')
        choose_lin.grid(row=5, column=3, columnspan=2, padx=5, pady=5)
        lines = ''
    else:
        if _lines[num] not in lines:
            lines += _lines[num]
            choose_lin.destroy()
            choose_lin = tk.Label(window, text=lines, font=('Calibri', 12, 'bold'), fg='#ffffff', bg='#303030')
            choose_lin.grid(row=5, column=3, columnspan=2, padx=5, pady=5)


def press_key(event):
    if event.char == '\r':
        draw_line(color, lines)
    if event.char == '\x1b':
        window.destroy()


window = tk.Tk()
window.resizable()
window.title("Image")
window["bg"] = '#303030'
window.resizable(None, None)

window.bind('<Key>', press_key)  # Бинд ввода с клавиатуры

label_file = tk.Label(window, text="Base picture: ", font=('Calibri', 12, 'bold'), fg='#ffffff',
                      bg='#303030')
label_file.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

file_list = list(filter(lambda file: match(r'.*\.bmp', file), listdir()))
filename = tk.StringVar()

entry_file = ttk.Combobox(textvariable=filename, values=file_list)
entry_file.grid(row=0, column=3, columnspan=2, padx=5, pady=5)

inv_button = tk.Button(window, text="inverse image", font=('Calibri', 12, 'bold'), fg='#303030', bg='#ffffff', bd=2,
                       command=inverse_pict)
inv_button.grid(row=1, column=0, columnspan=5, stick='wens')

# Кнопки цветов
# -------------------------------------------------------------------------------------------------------
color = None

red_button = tk.Button(window, text="Red", font=('Calibri', 12, 'bold'), fg='#000000', bg="#ff0000", bd=5,
                       command=lambda: chose_color(0))
red_button.grid(row=2, column=0)

green_button = tk.Button(window, text="Green", font=('Calibri', 12, 'bold'), fg='#000000', bg="#00ff00", bd=5,
                         command=lambda: chose_color(1))
green_button.grid(row=2, column=1)

blue_button = tk.Button(window, text="Blue", font=('Calibri', 12, 'bold'), fg='#000000', bg="#5061fa", bd=5,
                        command=lambda: chose_color(2))
blue_button.grid(row=2, column=2)

white_button = tk.Button(window, text="White", font=('Calibri', 12, 'bold'), fg='#000000', bg="#ffffff", bd=5,
                         command=lambda: chose_color(3))
white_button.grid(row=2, column=3, stick='wens')

red_button = tk.Button(window, text="Black", font=('Calibri', 12, 'bold'), fg='#ffffff', bg="#000000", bd=5,
                       command=lambda: chose_color(4))
red_button.grid(row=2, column=4, stick='wens')

# Выбранный цвет
# -------------------------------------------------------------------------------------------------------------
col = tk.Label(window, text="Color: ", font=('Calibri', 12, 'bold'), fg='#ffffff', bg='#303030')
col.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

choose_col = tk.Label(window, text="-", font=('Calibri', 12, 'bold'), fg='#ffffff', bg='#303030')
choose_col.grid(row=3, column=3, columnspan=2, padx=5, pady=5)

# -------------------------------------------------------------------------------------------------------------


# Кнопки линий
# -------------------------------------------------------------------------------------------------------
lines = ''

up_button = tk.Button(window, text="||", font=('Calibri', 12, 'bold'), fg='#ffffff', bg="#303030", bd=2,
                      command=lambda: chose_lines(0))
up_button.grid(row=4, column=0, sticky='wsen')

left_button = tk.Button(window, text="\\\\", font=('Calibri', 12, 'bold'), fg='#ffffff', bg="#303030", bd=2,
                        command=lambda: chose_lines(1))
left_button.grid(row=4, column=1, sticky='wsen')

hor_button = tk.Button(window, text="--", font=('Calibri', 12, 'bold'), fg='#ffffff', bg="#303030", bd=2,
                       command=lambda: chose_lines(2))
hor_button.grid(row=4, column=2, sticky='wsen')

right_button = tk.Button(window, text="//", font=('Calibri', 12, 'bold'), fg='#ffffff', bg="#303030", bd=2,
                         command=lambda: chose_lines(3))
right_button.grid(row=4, column=3, sticky='wsen')

clr_button = tk.Button(window, text="Clear", font=('Calibri', 12, 'bold'), fg='#ffffff', bg="#303030", bd=2,
                       command=lambda: chose_lines(4))
clr_button.grid(row=4, column=4, sticky='wsen')

# Выбранные линии
# -------------------------------------------------------------------------------------------------------------
lin = tk.Label(window, text="Lines: ", font=('Calibri', 12, 'bold'), fg='#ffffff', bg='#303030')
lin.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

choose_lin = tk.Label(window, text="0", font=('Calibri', 12, 'bold'), fg='#ffffff', bg='#303030')
choose_lin.grid(row=5, column=3, columnspan=2, padx=5, pady=5)

# -------------------------------------------------------------------------------------------------------------

draw_button = tk.Button(window, text="New picture", font=('Calibri', 12, 'bold'), fg='#ffffff', bg="#303030",
                        command=lambda: draw_line(color, lines))
draw_button.grid(row=6, column=0, columnspan=5, stick='wens')

window.mainloop()
