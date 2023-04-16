#Нисуев Нису ИУ7-12Б
#Вар1 найти строку с наибольшим средним арифметическим

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

#Вывод матрицы
print('Матрица:')		
for i in range(n):
	for j in range(m):
		print('{:5}'.format(lst[i][j]),end='')
	print()

#Блок поиска
max_str = float('-inf')
ind_str = 0

#Поиск строки с наибольшим средним арифметическим
for i in range(n):
	sum_el = 0 
	for j in range(m):
		sum_el += lst[i][j]
	sr_str = sum_el / m #Подсчет среднего арифметического
	if sr_str > max_str: #Поиск индекса строки с наибольшим средним арифметическим
		max_str = sr_str
		ind_str = i

print(f'Строка {ind_str + 1} с наибольшим средним арифметическим: ',*lst[ind_str])
