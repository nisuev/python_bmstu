#Нисуев Нису ИУ7-12Б "Квадратные уравнения"
a = float(input('Введите коэфицент a: '))
b = float(input('Введите коэфицент b: '))
c = float(input('Введите коэфицент с: '))
if a == 0:
    if b == 0:
        if c == 0:
            print('решением могут являться все действительные числа')
        else:
            print('действительных корней не существует')
    else:
        x = -c / b #Вычисление корня уравнения
        print('x = {:.5g}'.format(x))

else:
    d = b ** 2 - 4 * a * c #Вычисление дискриминанта
    if d < 0:
        print('действительных корней не существует')
    elif d == 0:
        x = -b / (2 * a) #Вычисление корня уравнения
        print('x = {:.5g}'.format(x))
    else:
        x1 = (-b + d ** 0.5) / (2 * a) #Вычисление корня уравнения
        x2 = (-b - d ** 0.5) / (2 * a) #Вычисление корня уравнения
        print('x1 = {:.5g}'.format(x1), 'x2 = {:.5g}'.format(x2))
