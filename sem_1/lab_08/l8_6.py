#Нисуев Нису ИУ7-12Б
#Транспонирование матрицы

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

#вывод иначальной матрицы
print('Изначальная матрица:')		
for i in range(n):
	for j in range(n):
		print('{:5}'.format(lst[i][j]),end='')
	print()

#Траспонирование матрицы
for i in range(n):
	for j in range(i):
		lst[i][j], lst[j][i] = lst[j][i], lst[i][j] #Перестановка элементов по правилу транспонирования

#Вывод траспонированной матрицы
print('Транспонированная матрица:')
for i in range(n):
	for j in range(n):
		print('{:5}'.format(lst[i][j]),end='')
	print()

