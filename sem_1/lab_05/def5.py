#Нисуев Нису ИУ7-12Б
#(x/2)**n/(n-1)!
x = float(input('аргумент: '))
eps = float(input('точность: '))

x_n = x / 2
sum_x = 0
halfX = x / 2
num_itr = 0

fact = 1
while True:
    print(x_n)
    num_itr += 1
    sum_x += x_n
    x_n = x_n * halfX / fact
    fact += 1
    if abs(x_n) < eps:
        break

print(f'Сумма бесконечного ряда - {sum_x:.7g}, вычисленна за {num_itr} итераций')
