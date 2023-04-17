import sympy as sp
from math import *


# Функция
def f(function: str, x: float or int) -> float or int:
    try:
        return eval(function)
    except:
        None


# Производная функции
def dif_f(func: str) -> str:
    return sp.diff(func, 'x')


# Функции для проверки фуннкции на наличие точки разрыва второго порядка
def fa(funct, x):
    try:
        f(funct, x)
    except ZeroDivisionError:
        return 0


# Поиск интервалов
def find_intervals(funct: str, beg: float, end: float, dels: float) -> list[tuple]:
    x_0 = beg
    x_1 = x_0 + dels
    inter = []

    if fa(funct, beg) == 0:
        inter.append((beg, beg + dels))
    if fa(funct, end) == 0:
        inter.append((end - dels, end))
    while x_0 < end:
        if isinstance(f(funct, x_0), complex) or isinstance(f(funct, x_1), complex):
            return 0
        if f(funct, x_0) is None or f(funct, x_1) is None:
            x_0 += dels
            x_1 += dels
            continue
        elif f(funct, x_0) * f(funct, x_1) <= 0:
            inter.append((x_0, x_1))
        x_0 += dels
        x_1 += dels
    return inter


# Метод Ньютона
def newton_method(funct: str, beg: float, end: float, eps: float, n_max: int, iter: float) -> tuple:
    x_0 = beg
    dif_func = str(dif_f(funct))
    section = "[{:<9.4}; {:>9.4}]".format(beg, end)
    error = (iter + 1, section, "Error", "Error", "Error", 1)
    for i in range(n_max):
        f_0 = f(funct, x_0)
        dif_f_0 = f(dif_func, x_0)
        if dif_f_0 == 0:
            error = (iter + 1, section, "Error", "Error", "Error", 3)
            return error
        x_1 = x_0 - f_0 / dif_f_0
        if not (beg <= x_1 <= end):
            error = (iter + 1, section, "Error", "Error", "Error", 2)
            return error
        if abs(x_1 - x_0) < eps:
            break
        x_0 = x_1
    else:
        return error

    return (iter + 1, section, format(x_1, "<9.4"), format(f(funct, x_1), "<.2g"), i + 1, 0)


# Нахождение строк таблицы
def tables_rows(funct: str, inters: list, eps: float, n_max: int) -> list[tuple]:
    rows = []
    for i in range(len(inters)):
        rows.append(newton_method(funct, inters[i][0], inters[i][1], eps, n_max, i))
    return rows