#Нисуев Нису ИУ7-12Б
#Поворот матрицы на 90 градусов по и против часовой стрелки

#Блок ввода матрицы
n = int(input('Введите количество строк и столбцов квадратной матрицы матрицы: '))

while n <= 0:
	print('В матрице должно быть больше нуля столбцов и строк')
	n = int(input('Введите количество строк и столбцов квадратной матрицы матрицы: '))

lst = []
for i in range(n):
	print()
	lst.append([])
	for j in range(n):
		lst[i].append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: ')))

#Вывод матрицы
print('Исходная матрица:')		
for i in range(n):
	for j in range(n):
		print('{:5}'.format(lst[i][j]),end='')
	print()
print()

#Поворот матрицы на 90 градусов по часовый	
for i in range(n//2):
	for j in range(i, n-1-i):
		lst[i][j], lst[j][n-1-i], lst[n-1-i][n-1-j], lst[n-1-j][i] = lst[n-1-j][i], lst[i][j], lst[j][n-1-i], lst[n-1-i][n-1-j]

#Вывод повернутой матрицы
print('Матрица повернутая на 90 градусов по часовой:')		
for i in range(n):
	for j in range(n):
		print('{:5}'.format(lst[i][j]),end='')
	print()
print()

#Поворот матрицы на 90 градусов против часовый
for i in range(n//2):
	for j in range(i, n-1-i):
		lst[n-1-j][i], lst[i][j], lst[j][n-1-i], lst[n-1-i][n-1-j] = lst[i][j], lst[j][n-1-i], lst[n-1-i][n-1-j], lst[n-1-j][i]

#Вывод повернутой матрицы
print('Матрица повернутая на 90 градусов против часовой:')		
for i in range(n):
	for j in range(n):
		print('{:5}'.format(lst[i][j]),end='')
	print()
