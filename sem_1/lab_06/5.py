#Нисуев Нису ИУ7-12Б
#№5 смена мест минимального нечтного и максимального четного в массиве
n = int(input('Введите размер массива: '))

while  n < 1:
	print('В списке должно быть больше 0 элементов')
	n = int(input('Введите размер массива: '))

list=[0] * n

max_el, min_el = float('-inf'), float('inf')

for i in range(n):
	list[i] = int(input(f'Введите {i + 1} элемент: '))
	if list[i] % 2 == 0 and list[i] > max_el: #поиск макс чет
		max_el = list[i]
	if list[i] % 2 != 0 and list[i] < min_el: #поиск мин нечет
		min_el = list[i]

if max_el ==  float('-inf'):
	print('В списке нет четных чисел')
	exit()

if max_el ==  float('inf'):
	print('В списке нет нечетных чисел')
	exit()
	
list[list.index(max_el)], list[list.index(min_el)] = list[list.index(min_el)], list[list.index(max_el)] #смена макс чет и мин нечет
for i in range(n):
		print(f'{i + 1} элемент: {list[i]}')
