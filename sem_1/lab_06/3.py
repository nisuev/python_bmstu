#Нисуев Нису ИУ7-12Б
#№3 поиск К-го экстремума
n = int(input('Введите размер массива: '))
list=[0] * n

while n <= 0:
	print('длина списка не может быть меньше или равна 0')
	n = int(input('Введите размер массива: '))

for i in range(n):
	list[i] = int(input(f'Введите {i + 1} элемент: '))

k = int(input('Введите номер искомого экстремума: '))

num_ext = 1

for i in range(1, n - 1):
	if list[i - 1] < list[i] > list[i + 1] or list[i - 1] > list[i] < list[i + 1]:
		if num_ext == k:
			print(f'{k} экстремум в списке = {list[i]}')
			break
		else:
			num_ext += 1

else:
	if num_ext == 1:
		print('Всписке нет экстремумов')
	else:
		print(f'в списке экстремумов меньше чем {k} ')
 
