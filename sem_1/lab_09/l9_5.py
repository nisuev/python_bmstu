#Нисуев Нису ИУ7-12Б
#Вар1 найти столбец с наибольшим кол-вом простых чисел

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
		lst[i].append(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: '))

#Вывод исходной матрицы
print('исходная матрица:')		
for i in range(n):
	for j in range(m):
		print('{:5}'.format(lst[i][j]),end='')
	print()
print()

str_let = 'aeyuio' #Список гласных английских букв
for i in range(n):
	for j in range(m):
		if lst[i][j].lower() in str_let: #Проверка элемента массива на гласность
			lst[i][j] = '.' #Замена гласных английских букв на точку
			
#Вывод измененной матрицы
print('Измененная матрица:')		
for i in range(n):
	for j in range(m):
		print('{:5}'.format(lst[i][j]),end='')
	print()
print()
