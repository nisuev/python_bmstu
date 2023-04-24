# Дано множество точек найти найти такие три точки на которых можно построить треугольник
# включающий в себя максимальное кол-во остальных точек

import tkinter as tk
from def_back import *
from tkinter import messagebox as box


def add_point() -> None:
    x, y = int(entry_input_x.get()), int(entry_input_y.get())
    draw_point(x, y)

    entry_input_x.delete(0, tk.END)
    entry_input_y.delete(0, tk.END)
    window.focus()


def draw_point(x: int, y: int) -> None:
    Point(x, y, canvas)


def clear() -> None:
    canvas.delete("all")
    Point.points.clear()


def click(event: tk.Event) -> None:
    draw_point(event.x, event.y)


def result() -> None:
    if len(Point.points) < 4:
        box.showinfo("ERROR", "Введено недостаточное количество точек")
    else:
        points = calculate(canvas)
        for point in points:
            Point.draw(point.x, point.y, canvas, COLORS["VERTECS"])
        for i in range(-1, 2):
            canvas.create_line(points[i].x, points[i].y,
                               points[i + 1].x, points[i + 1].y,
                               fill=COLORS["LINE"])


window = tk.Tk()

window.resizable(None, None)
window.title('Def')
window["bg"] = "#212121"

label_input_x = tk.Label(window, text='x:', font=('Calibri', 12), bg="#212121", fg="#ffffff")
label_input_x.grid(row=0, column=0)

entry_input_x = tk.Entry(window)
entry_input_x.grid(row=0, column=1, padx=5, pady=5)

label_input_y = tk.Label(window, text='y:', font=('Calibri', 12), bg="#212121", fg="#ffffff")
label_input_y.grid(row=1, column=0)

entry_input_y = tk.Entry(window)
entry_input_y.grid(row=1, column=1, padx=5, pady=5)

button_add_point = tk.Button(window, text="Add point", font=('Calibri', 12),
                             bg="#212121", fg="#ffffff", command=add_point)
button_add_point.grid(row=0, column=2, stick='wens', padx=5, pady=5)

button_clear_canvas = tk.Button(window, text="Clear", font=('Calibri', 12),
                                bg="#212121", fg="#ffffff", command=clear)
button_clear_canvas.grid(row=0, column=3, stick='wens', columnspan=2, padx=5, pady=5)

button_result = tk.Button(window, text="Result", font=('Calibri', 12), bg="#b8860b", command=result)
button_result.grid(row=1, column=2, columnspan=2, stick='wens', padx=5, pady=5)

canvas = tk.Canvas(window, width=500, height=500, bg="#b8860b")
canvas.grid(row=3, column=0, columnspan=4, stick='wens', padx=5, pady=5)

canvas.bind("<Button-1>", click)

window.mainloop()
