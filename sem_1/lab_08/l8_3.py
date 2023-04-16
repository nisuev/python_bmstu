#Нисуев Нису ИУ7-12Б
#Вар1 найти столбец с наибольшим кол-вом простых чисел

#Блок ввода матрицы
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))

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

#Вывод матрицы
print('Матрица:')		
for i in range(n):
	for j in range(m):
		print('{:5}'.format(lst[i][j]),end='')
	print()
print()

#Блок поиска
max_clm = -1
ind_clm = 0
 		
for j in range(m):
	k_pr = 0
	for i in range(n):
		#Проверка числа на простоту
		if lst[i][j] <= 1: #Отсеивание отрицательных чисел, 1 и 0
			pr = False
		else: #Проверка на простоту
			pr = True
			for dl in range(2,int(lst[i][j] ** 0.5) + 1): #Перебор возможных делителей до корня элемента
				if lst[i][j] % dl == 0: #Проверка на делимость
					pr = False
					break
			print(lst[i][j],pr)
		if pr is True:
			k_pr += 1 #Подсчет кол-ва простых чисел
	if k_pr > max_clm: #Поиск индекса столбца с макс кол-вом простых чисел
		max_clm = k_pr
		ind_clm = j

#Блок вывода
print(f'Столбец {ind_clm + 1} с наибольшим кол-вом простых чисел: ', end='')
for i in range(n):
	print(lst[i][ind_clm], end=' ')
