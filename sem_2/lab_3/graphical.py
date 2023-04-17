from back import *
import tkinter as tk
from re import match
from os import listdir
from tkinter import ttk
from tkinter import messagebox as box

# Константа для хранения цвета.
COLOR_BG = "#121212"
COLOR_TXT = "#ffffff"


# Процедура для вызова функции шифрования с необходимыми аргументами.
def encode_command():
    try:
        encode_file = filename.get()
        message = entry_input_message.get()
        if len(message) == 0:
            box.showinfo('Error', "No message to encode")
            return
        encode(encode_file, message)
        combobox_filename["values"] = list(filter(lambda file: match(r'.*\.bmp', file), listdir()))
        box.showinfo('Code', "Message successfully encode")
    except:
        box.showinfo('Error', "No encode/decode file")


# Процедура для вызова функции дешифрования с необходимыми аргументами.
def decode_command():
    try:
        entry_output_message.insert(0, decode(filename.get()))
    except:
        box.showinfo('Error', "No encode/decode file")


# Процедура для очистки полей.
def update(_):
    entry_input_message.delete(0, tk.END)
    entry_output_message.delete(0, tk.END)


# Создания окна.
window = tk.Tk()
window.title("Steganography")
window["bg"] = COLOR_BG
window.resizable(None, None)

# Интерфейс.
label_input_filename = tk.Label(window, text="Encoding picture: ", font=('Calibri', 12, 'bold'), fg=COLOR_TXT,
                                bg=COLOR_BG)
label_input_filename.grid(row=0, column=0, padx=5, pady=5)

file_list = list(filter(lambda file: match(r'.*\.bmp', file), listdir()))
filename = tk.StringVar()

combobox_filename = ttk.Combobox(textvariable=filename, values=file_list)
combobox_filename.bind("<<ComboboxSelected>>", update)
combobox_filename.grid(row=0, column=1, padx=5, pady=5)

label_input_message = tk.Label(window, text="Input message: ", font=('Calibri', 12), fg=COLOR_TXT, bg=COLOR_BG)
label_input_message.grid(row=1, column=0, padx=5, pady=5)

entry_input_message = tk.Entry(window)
entry_input_message.grid(row=1, column=1, padx=5, pady=5)

label_output_message = tk.Label(window, text="Encoding message:", font=('Calibri', 12), fg=COLOR_TXT, bg=COLOR_BG)
label_output_message.grid(row=2, column=0, padx=5, pady=5)

entry_output_message = tk.Entry(window)
entry_output_message.grid(row=2, column=1, padx=5, pady=5)

encode_button = tk.Button(window, text="Encode message", font=('Calibri', 12, 'bold'), fg=COLOR_TXT, bg="#04700f",
                          command=encode_command)
encode_button.grid(row=4, column=0, stick='wens')

decode_button = tk.Button(window, text="Decode message", font=('Calibri', 12, 'bold'), fg=COLOR_TXT, bg="#700404",
                          command=decode_command)
decode_button.grid(row=4, column=1, stick='wens')

window.mainloop()
