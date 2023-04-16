
#метод серединных прямоугольников
# x ** 2 - 1 на отрезке от а до b с числом разбиения n

def f(x):
    #return 4
    return x ** 2 - 1

def mid_rect(begin, end, n):
    step = (end - begin) / n
    s = 0
    x = begin
    while x < end:
        s += f((x + (x + step)) / 2) * step
        x += step
    return s

x_begin = float(input('Введите начало отрезка интегрирования: '))
x_end = float(input('Введите конец отрезка интегрирования: '))
n = int(input('Введите кол-во разбиений: '))
print(f'Интеграл, посчитанный методом серединных прямоугольников, на заданном отрезке = {mid_rect(x_begin, x_end, n):.5g}')
