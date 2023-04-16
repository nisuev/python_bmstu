#Нисуев Нису ИУ7-12Б
#Вар 1. удаление Нулевых элементов из списка

#Блок ввода
n = int(input('Введите размер массива: '))

while  n < 1:
	print('В списке должно быть больше 0 элементов')
	n = int(input('Введите размер массива: '))

lst = [0] * n

for i in range(n):
	lst[i] = int(input(f'Введите {i + 1} элемент последовательности: '))

print(lst)
if lst.count(0) == 0:
        print('В списке нет нулевых значений')
        exit()

i = 0
shift = 0  # Количество элементов для удаления (Сдвиг элементов влево)
while i < n:
    if lst[i] == 0:
        shift += 1  # Увеличение сдвига, т.к. удален еще 1 элемент
    else:
        lst[i-shift], lst[i] = lst[i], lst[i-shift]  # Сдвиг элементов
    i += 1
lst = lst[0:n-shift]  # Сокращение длины списка

print('Список без нулевых значений: ')
for i in range(len(lst)):
	print(f'{i + 1} элемент: {lst[i]}')



'''Не алгоритм решение
k_0 = lst.count(0) #Кол-во нулевых значений

#Удаление нулевых значений
if k_0 == 0:
	print('В списке нет нулевых значений')
	
else:
	for i in range(k_0):
		lst.remove(0)
	print('Список без нулевых значений: ', *lst)'''
