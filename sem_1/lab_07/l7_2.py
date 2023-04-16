#Нисуев Нису ИУ7-12Б
#Вар 1. Добавление удвоенных значений элементов кратных трем после них

#Блок ввода
n = int(input('Введите размер массива: '))

while  n < 1:
	print('В списке должно быть больше 0 элементов')
	n = int(input('Введите размер массива: '))

lst = []

for i in range(n):
	el = int(input(f'Введите {i + 1} элемент последовательности: '))
	lst.append(el)


shift = 0  # количество элементов кратных трем(сдвиг элементов вправо)
for i in range(n):
	if lst[i] % 3 == 0:
		shift += 1
		lst.append(None) # расширение списка

i = len(lst)-1

while i >= 0:
	if lst[i-shift] % 3 == 0:
		lst[i] = lst[i-shift] * 2  # Запись удвоенного эемента
		lst[i-1], lst[i-shift] = lst[i-shift], lst[i-1]  # Запись эемента на пред. место
		shift -= 1  # Уменьшение сдвига
		i -= 1  # Для перехода к следующему
	else:
		lst[i], lst[i-shift] = lst[i-shift], lst[i]
	i -= 1

print('Список с удвоенными значениями чисел кратных трем:')
for i in range(len(lst)):
	print(f'{i + 1} элемент: {lst[i]}')



'''yt fkujhbnv код
for i in range(n):
	el = int(input(f'Введите {i + 1} элемент последовательности: '))
	lst.append(el)
	if el % 3 == 0:
		lst.append('new_el') #Добавление элемента после числа кратного трем
		
k_0 = lst.count('new_el') #Кол-во элементов кратных трем

if k_0 == 0:
	print('Всписке нет элементов кратных трем')

else:
	for i in range(k_0):
		ind = lst.index('new_el')
		lst[ind] = lst[ind - 1] * 2 #Добавление удвоенного значения элементов кратных трем
	print('Список с удвоенными значениями чисел кратных трем: ', *lst)'''
