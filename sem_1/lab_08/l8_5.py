#Нисуев Нису ИУ7-12Б
#Макс значение над главной диагональю и мин под побочной

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
print('Матрица:')		
for i in range(n):
	for j in range(n):
		print('{:5}'.format(lst[i][j]),end='')
	print()

max_el = float('-inf')
ind_el = ()
#Нахождение наибольшего элемента над главной диагональю
for i in range(n):
	for j in range(i + 1, n):
		if lst[i][j] > max_el:
			max_el = lst[i][j]
			ind_el = (i, j)
			
print('Максимальный элемент над главной диагональю: ', lst[ind_el[0]][ind_el[1]])


min_el = float('inf')
ind_el = ()
#Нахождение наименьшего элемента под побочной диагональю
for i in range(n):
	for j in range(n - i, n):
		if lst[i][j] < min_el:
			min_el = lst[i][j]
			ind_el = (i, j)
			
print('Минимальный элемент под побочной диагональю: ', lst[ind_el[0]][ind_el[1]])
