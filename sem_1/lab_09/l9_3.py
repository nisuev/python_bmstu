#Нисуев Нису ИУ7-12Б
#Поиск кол-ва элементов строки матрицы, больших суммы соответствующей строки другой матрицы.
#Умножение матрицы на макс кол-во элементов

#Блок ввода матрицы D
nd = int(input('Введите количество строк матрицы D: '))
md = int(input('Введите количество столбцов матрицы D: '))

while md <= 0 or nd <= 0:
	print('В матрице должно быть больше нуля столбцов и строк')
	nd = int(input('Введите количество строк матрицы D: '))
	md = int(input('Введите количество столбцов матрицы D: '))
	
d = []
for i in range(nd):
	print()
	d.append([])
	for j in range(md):
		d[i].append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: ')))
print()

#Блок ввода матрицы Z
nz = int(input('Введите количество строк матрицы Z: '))
mz = int(input('Введите количество столбцов матрицы Z: '))

while mz <= 0 or nz <= 0:
	print('В матрице должно быть больше нуля столбцов и строк')
	nz = int(input('Введите количество строк матрицы Z: '))
	mz = int(input('Введите количество столбцов матрицы Z: '))
	
z = []
for i in range(nz):
	print()
	z.append([])
	for j in range(mz):
		z[i].append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: ')))
print()
		
#Вывод матрицы Z
print('Матрица Z:')		
for i in range(nz):
	for j in range(mz):
		print('{:5}'.format(z[i][j]),end='')
	print()
print()

g = [] #Список G
for i in range(nz):
	sum_z = 0
	k_d = 0
	if i >= nd:
		break
	else:
		for j in range(mz):
			sum_z += z[i][j] #Подсчет суммы элементов строки матрицы Z
		if i < nd: #Проверка на наличие такой строки в матрице D
			for j in range(md):
				if d[i][j] > sum_z: #Поиск кол-ва элементов строки матрицы D превышающих сумму элементов соответствующей строки матрицы Z
					k_d += 1
		g.append(k_d)
	
#Вывод матрицы D
print('Матрица D:')		
for i in range(nd):
	for j in range(md):
		print('{:5}'.format(d[i][j]),end='')
	print()
print()

#Поиск максимального элемента в массиве g
max_g = g[0]
for i in g:
	if i > max_g:
		max_g = i

#умножение элементов матрицы на число
for i in range(nd):
	for j in range(md):
		d[i][j] *= max_g
		
#Вывод матрицы D после умножения
print('Преобразованная матрица D:')		
for i in range(nd):
	for j in range(md):
		print('{:5}'.format(d[i][j]),end='')
	print()
print()

print('Массив кол-ва элементов строки D превышающих сумму элементов соответствующей строки Z: ', *g)
