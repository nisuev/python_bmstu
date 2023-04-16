# 2cos2x - 2

import math as m

eps = 1e-20

start = float(input('start: '))
stop = float(input('stop: '))
step = float(input('step: '))

y_max, y_min = float('-inf'), float('inf')

i=0
while stop >= start + i * step:
    x = start + i * step
    y = 2 * m.cos(2 * x) - 2
    if y - y_max > eps:
        y_max = y
    if y - y_min < eps:
        y_min = y
    i += 1

if y_max == y_min:
    print('Для данного отрезка невозожно корректно вычислить значение функции')
    exit()

interval = (y_max - y_min) / 80

print(' '*10, f'{y_min:<{41}.{8}g}{y_max:>{40}.{8}g}')
i = 0
while stop >= start + i * step:
    x = start + i * step
    y = 2 * m.cos(2 * x) - 2
    print(f'{x:>{10}.{4}g}|',end='')
    i += 1
    for j in range(81):
        if y_min + interval * j - y <= eps < y_min + interval * (j + 1) - y:
            print('*', end='')
        elif y_min + interval * j <= eps < y_min + interval * (j + 1):
            print('|', end='')
        else:
            print(end=' ')
    print()
