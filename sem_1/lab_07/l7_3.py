#Нисуев Нису ИУ7-12Б
#Вар 4. Нахождение элемента с наибольшим кол-вом пробелов подряд

n = int(input('Введите размер массива: '))

while  n < 1:
	print('В списке должно быть больше 0 элементов')
	n = int(input('Введите размер массива: '))

lst = []
ind_space = 0  #Индекс элемента с максимальным кол-вом пробелов подряд
max_space = -1 #Макс кол-во пробелов подряд

for i in range(n):
	el = input(f'Введите {i + 1} элемент последовательности: ')
	lst.append(el)
	k = 1
	for j in range(len(el) - 1): #Поиск индекса элемента с максимальным кол-вом пробелов подряд
		if el[j] == el[j + 1] == ' ':
			k += 1
			if k > max_space:
				max_space = k
				ind_space = i
		else:
			k = 1
if max_space == -1:
        print('No')
else:
        print('Элемент с наибольшим кол-вом пробелов подряд: ', lst[ind_space]) 