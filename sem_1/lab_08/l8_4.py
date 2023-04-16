#Нисуев Нису ИУ7-12Б
#замена столбцов с максимальной и минимальной суммой

#Блок ввода матрицы
n = int(input('Ввдите количество строк матрицы: '))
m = int(input('Ввдите количество столбцов матрицы: '))

while m <= 0 or n <= 0:
	print('В матрице должно быть больше нуля столбцов и строк')
	n = int(input('Ввдите количество строк матрицы: '))
	m = int(input('Ввдите количество столбцов матрицы: '))
	
lst = []
for i in range(n):
	print()
	lst.append([])
	for j in range(m):
		lst[i].append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: ')))

#Вывод изначальной матрицы
print('Исходная матрица:')		
for i in range(n):
	for j in range(m):
		print('{:5}'.format(lst[i][j]),end='')
	print()
print('',end='\n\n')

#Блок поиска
max_sum, min_sum = float('-inf'), float('inf')
ind_min, ind_max = 0, 0

for j in range(m):
	sum_el = 0
	for i in range(n):
		sum_el += lst[i][j] #Подсчет суммы элементов столбца
	if sum_el > max_sum: #Поиск индекса стобца с максимальной суммой
		max_sum = sum_el
		ind_max = j
	if sum_el < min_sum: #Поиск индекса стобца с минимальной суммой
		min_sum = sum_el
		ind_min = j

#Блок вывода
if max_sum == min_sum:
	print('В матрице у всех столбцов одинаковая сумма')

else:
	for i in range(n):
		lst[i][ind_max], lst[i][ind_min] = lst[i][ind_min], lst[i][ind_max]
	
	print('Измененная матрица:')
	for i in range(n):
		for j in range(m):
			print('{:5}'.format(lst[i][j]),end='')
		print()
