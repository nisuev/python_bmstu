#Нисуев Нису ИУ7-12Б
#Формирование матрицы С путем перемножения элементов матриц А и В
#Поиск суммы элементов всех столбцов

#Блок ввода матриц
n = int(input('Введите количество строк матриц A и B: '))
m = int(input('Введите количество столбцов матриц А и В: '))

while m <= 0 or n <= 0:
	print('В матрицах должно быть больше нуля столбцов и строк')
	n = int(input('Введите количество строк матриц А и В: '))
	m = int(input('Введите количество столбцов матриц А и В: '))

#Ввод матрицы А
a = []
for i in range(n):
	print()
	a.append([])
	for j in range(m):
		a[i].append(float(input(f'Введите {j + 1}-й элемент {i + 1}-й строки матрицы А: ')))

#Вывод матрицы A
print('Mатрица A:')		
for i in range(n):
	for j in range(m):
		print('{:10.5g}'.format(a[i][j]),end='')
	print()
print()

#Ввод матрицы В
b = []
for i in range(n):
	print()
	b.append([])
	for j in range(m):
		b[i].append(float(input(f'Введите {j + 1}-й элемент {i + 1}-й строки матрицы B: ')))

#Вывод матрицы B
print('Mатрица B:')		
for i in range(n):
	for j in range(m):
		print('{:10.5g}'.format(b[i][j]),end='')
	print()
print()
	
c = [[0] * m for i in range(n)] #Ввод матрицы С

#Создание матрицы С по правилу
for i in range(n):
	for j in range(m):
		c[i][j] = a[i][j] * b[i][j] #Перемножение соответствующих элементов матриц А и В
		
		
#Вывод матрицы C
print('Mатрица C:')		
for i in range(n):
	for j in range(m):
		print('{:10.5g}'.format(c[i][j]),end='')
	print()
print()

#Подсчет суммы столбцов
v = [0] * m #Создание списка сумм
for j in range(m):
	sum_el = 0
	for i in range(n):
		sum_el += c[i][j] #Поиск суммы элементов столбца
	v[j] = sum_el

for i in range(m):
	print(f'Сумма элементов {i + 1} столбца матрицы С: ', v[i])

