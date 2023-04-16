#Нисуев Нису ИУ7-12Б
#№1a удаление элемента из списка
n = int(input('Введите размер массива: '))

while  n < 1:
	print('В списке должно быть больше 0 элементов')
	n = int(input('Введите размер массива: '))
	
list=[0] * n

for i in range(n):
	list[i] = int(input(f'Введите {i + 1} элемент: '))
	
del_n = int(input('Введите индекс удаляемого элемента: '))

if 0 >= del_n or del_n > n:
	print('Индекс за границами массива')
	exit()


list.pop(del_n - 1)
for i in range(n - 1):
	print(f'{i + 1} элемент: {list[i]}')
