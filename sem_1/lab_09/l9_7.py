#Нисуев Нису ИУ7-12Б
#Ввод трехмерного массива и вывод его среза по второму индексу

#Блок ввода трехмерной матрицы
x = int(input('Введите количество строк матрицы: '))
y = int(input('Введите количество столбцов матрицы: '))
z = int(input('Введите кол-во матриц: '))

while x < 1 or y < 1 or z < 1:
	if x < 1:
		x = int(input('Введите количество строк матрицы: '))
	elif y < 1:
		y = int(input('Введите количество столбцов матрицы: '))
	else:
		z = int(input('Введите кол-во матриц: '))
		
print()
martrix = []
for i in range(z):
	martrix.append([])
	for j in range(y):
		martrix[i].append([])
		for k in range(x):
			martrix[i][j].append(input(f'Введите {k+1}-й элемент {j+1}-й строки {i+1}-й матрицы: '))
		print()
	print()

#спрашиваем индекс среза
cut = int(input(f'Введите срез трехмерной матрицы по второму индексу (1-{y}): ')) - 1

while cut >= y or cut < 0:
	cut = int(input(f'Введите срез трехмерной матрицы по второму индексу (1-{y}): ')) - 1

for i in range(x):
	for j in range(z):
		print(f'{martrix[i][cut][j]:5}',end='')
	print()
