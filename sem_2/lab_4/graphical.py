from back import *
import tkinter as tk
from tkinter import messagebox as box

WIDTH = HEIGHT = 500


def result() -> None:
    global label_result
    label_result.destroy()
    if len(Point.points) < 2:
        box.showinfo("ERROR", "Введено меньше двух точек")
    else:
        center, radius = calculate(canvas)
        Point.draw(center.x, center.y, canvas, COLORS["CENTER"])
        Circle.draw(center, radius, canvas)
        label_result = tk.Label(window, text='Center: ({}, {}), R: {:.4g}'.format(center.x, center.y, radius),
                                font=('Calibri', 12))
        label_result.grid(row=4, column=0, columnspan=4)


def click(event: tk.Event) -> None:
    draw_point(event.x, event.y)


# Отрисовка точки, используя координаты.
def add_point() -> None:
    try:
        x, y = int(entry_input_x.get()), int(entry_input_y.get())

        if 0 <= x <= WIDTH + 1 and 0 <= y <= HEIGHT + 1:
            draw_point(x, y)
        else:
            box.showinfo("ERROR", "Координаты точки выходят за рамки поля 500х500")

    except ValueError:
        box.showinfo("ERROR", "Некорректный ввод координат")

    entry_input_x.delete(0, tk.END)
    entry_input_y.delete(0, tk.END)
    window.focus()


def draw_point(x: int, y: int) -> None:
    Point(x, y, canvas)


def clear() -> None:
    canvas.delete("all")
    Point.points.clear()
    global label_result
    label_result.destroy()
    label_result = tk.Label(window, text='Center: ?, R: ?', font=('Calibri', 12))
    label_result.grid(row=4, column=0, columnspan=4)


def move(event: tk.Event) -> None:
    entry_coordinate_x.delete(0, tk.END)
    entry_coordinate_x.insert(0, str(event.x))
    entry_coordinate_y.delete(0, tk.END)
    entry_coordinate_y.insert(0, str(event.y))


def info():
    text = '''    На плоскости задано множество точек.
    Найти центр и радиус круга минимальной площади,
    содержащего эти точки.'''

    box.showinfo('Работа программы', text)


def press_key(event):
    if event.char == '\r' or event.char == '=':
        result()
    if event.char == 'c':
        clear()


# Создание окна
# --------------------------------------------------------------------------
window = tk.Tk()
window.resizable(None, None)
window.title('Circles')
# --------------------------------------------------------------------------


# Основное меню
# --------------------------------------------------------------------------
# Меню
mainmenu = tk.Menu(window)
window.config(menu=mainmenu)

mainmenu.add_command(label='Programm info', command=lambda: info())
mainmenu.configure()
# --------------------------------------------------------------------------


# Интерфейс
# --------------------------------------------------------------------------
label_input_x = tk.Label(window, text='x:', font=('Calibri', 12))
label_input_x.grid(row=0, column=0)

entry_input_x = tk.Entry(window)
entry_input_x.grid(row=0, column=1, padx=5, pady=5)

label_input_y = tk.Label(window, text='y:', font=('Calibri', 12))
label_input_y.grid(row=1, column=0)

entry_input_y = tk.Entry(window)
entry_input_y.grid(row=1, column=1, padx=5, pady=5)

button_add_point = tk.Button(window, text="Add point", font=('Calibri', 12), command=add_point)
button_add_point.grid(row=0, column=2, stick='wens', padx=5, pady=5)

button_clear_canvas = tk.Button(window, text="Clear", font=('Calibri', 12), command=clear)
button_clear_canvas.grid(row=0, column=3, stick='wens', columnspan=2, padx=5, pady=5)

button_result = tk.Button(window, text="Result", font=('Calibri', 12), bg="#737373", command=result)
button_result.grid(row=1, column=2, columnspan=2, stick='wens', padx=5, pady=5)

label_result = tk.Label(window, text='Center: ?, R: ?', font=('Calibri', 12))
label_result.grid(row=4, column=0, columnspan=4)

label_coordinate_x = tk.Label(window, text="x.coordinate:")
label_coordinate_x.grid(row=2, column=0, padx=5, pady=5)

entry_coordinate_x = tk.Entry(window, width=15)
entry_coordinate_x.grid(row=2, column=1, padx=5, pady=5)

label_coordinate_y = tk.Label(window, text="y.coordinate:")
label_coordinate_y.grid(row=2, column=2, padx=5, pady=5)

entry_coordinate_y = tk.Entry(window, width=15)
entry_coordinate_y.grid(row=2, column=3, padx=5, pady=5)

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="#212121")
canvas.grid(row=3, column=0, columnspan=4, stick='wens', padx=5, pady=5)

canvas.bind("<Button-1>", click)
canvas.bind("<Motion>", move)

window.bind('<Key>', press_key)  # Бинд ввода с клавиатуры
# --------------------------------------------------------------------------

# запуск обработчика обытий
window.mainloop()
