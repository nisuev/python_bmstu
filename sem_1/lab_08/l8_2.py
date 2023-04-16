#Нисуев Нису ИУ7-12Б
#Перестановка строк с наибольшим и наименьшим кол-вом отрицательных элементов

#Блок ввода матрицы
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))

while m <= 0 or n <= 0:
	print('В матрице должно быть больше нуля столбцов и строк')
	n = int(input('Введите количество строк матрицы: '))
	m = int(input('Введите количество столбцов матрицы: '))

lst = []
for i in range(n):
	print()
	lst.append([])
	for j in range(m):
		lst[i].append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: ')))

#Вывод изначальной матрицы
print('изначальная матрица:')		
for i in range(n):
	for j in range(m):
		print('{:5}'.format(lst[i][j]),end='')
	print()

#Блок поиска
max_str, min_str = -1, m + 1
ind_mx, ind_mn = 0, 0

for i in range(n):
	k = 0
	for j in range(m):
		if lst[i][j] < 0: #Счет отрицательных чисел
			k += 1
	if k > max_str: #Поиск индекса строки с наибольшим кол-вом отрицательных элементов
		max_str = k
		ind_mx = i
	if k < min_str:  #Поиск индекса строки с наименьшим кол-вом отрицательных элементов
		min_str = k
		ind_mn = i

#Блок вывода
if min_str == max_str:
	print('В матрице все строчки имеют одинаковое кол-во отрицательных элементов')
	
else:
	lst[ind_mn], lst[ind_mx] = lst[ind_mx], lst[ind_mn] #Замена строк
	print('Измененная матрица:')
	for i in range(n):
		for j in range(m):
			print('{:5}'.format(lst[i][j]),end='')
		print()
	
		
		
