# Нисуев Нису ИУ7-12Б
# построение таблицы суммы бесконечного ряда
# s = x + x ** 3 / 3! + ... + x ** (2n + 1) / (2n + 1)!

import math as m

x = float(input('Введите значение аргумента: '))
eps = float(input('Введите точность: '))
step = int(input('Введите целочисленный шаг: '))
num = int(input('Введите количество итераций: '))
s = 0

# проверка вводимых данных
while step <= 0:
    print('шаг должен быть положительный и больше нуля')
    step = int(input('Введите целочисленный шаг: '))
while x == 0:
    print('аргумент не должен быть равен 0')
    x = float(input('Введите целочисленный шаг: '))
while eps <= 0:
    print('точность должна быть положительный и больше нуля')
    eps = float(input('Введите точность: '))
while num <= 0:
    print('количество итераций должно быть положительный и больше нуля')
    num = int(input('Введите количество итераций: '))
while step > num:
    print('количество итераций должно быть больше шага')
    step = int(input('Введите целочисленный шаг: '))
    num = int(input('Введите количество итераций: '))

# шапка таблицы
print('-' * 43)
print('|{:^13s}|{:^13s}|{:^13s}|'.format('№итерации', 't', 's'))
print('|', '-' * 41, '|', sep='')
sqX = x ** 2  #квадрат аргумента

# начало таблицы
for i in range(num):
    if i == 0:  # вывод первого элемента
        t = x  # значение первого элемента последовательности
        s += x
        print('|', '{:11.5g}'.format(1), '|', '{:11.5g}'.format(t), '|', '{:11.5g}'.format(s), '|')  # вывод первой строки таблицы
    else:
        n = i + 1  # номер шага
        t = (t * sqX) / ((2 * i) * (2 * i + 1)) # подсчет n-ого элемента последовательности
        if t == m.inf:
            print('-' * 43, end='\n\n')
            print('За указанное число итераций не удалось достичь необходимой точности')
        if t < eps:  # проверка на точность
            print('-' * 43, end='\n\n')
            print('Сумма бесконечного ряда - {:.5g}, вычислена за {} итераций'.format(s, i))
            break
        s += t  # подсчет суммы
        if n == num:  # проверка на окончание итераций
            if t < eps:
                print('|', '{:11.5g}'.format(n), '|', '{:11.5g}'.format(t), '|', '{:11.5g}'.format(s), '|')  # вывод поледней строки таблицы
                print('-' * 43, end='\n\n') # закрытие таблицы
                print('Сумма бесконечного ряда - {:.5g}, вычислена за {} итераций'.format(s, n))  # вывод результата подсчетов
                break
            else:
                print('|', '{:11.5g}'.format(n), '|', '{:11.5g}'.format(t), '|', '{:11.5g}'.format(s), '|')
                print('-' * 43, end='\n\n')
                print('За указанное число итераций не удалось достичь необходимой точности')
                break
        if (n-1) % step == 0:  # вывод по шагу
            print('|', '{:11.5g}'.format(n), '|', '{:11.5g}'.format(t), '|', '{:11.5g}'.format(s), '|')  # вывод n-ой строки таблицы