#Нисуев Нису ИУ7-12Б
#сортировка метододом пирамиды(Кучи)

#Импорт библиотек
import random as r
import time as t 

# Функция для перемешения максимального элемента в корневой узел поддерева
def heapify(lst, n, i):
	largest = i # Индекс корневого узла
	left = 2 * i + 1   # левый дочерний элемент корневого узла
	right = 2 * i + 2   # правый дочерний элемент корневого узла
	# Проверяем существует ли левый дочерний элемент больший, чем корень
	if left < n and lst[i] < lst[left]:
		largest = left
	# Проверяем существует ли правый дочерний элемент больший, чем корень
	if right < n and lst[largest] < lst[right]:
		largest = right
	# Замена кореня, если нашелся больший
	if largest != i:
		global k #Счет перестановок
		k += 1
		lst[i], lst[largest] = lst[largest], lst[i] # перестановка
		# Применяем heapify к корневому узлу
		heapify(lst, n, largest)

# Основная функция для сортировки пирамидой
def heapSort(lst):
	n = len(lst)
	# Построение убывающей пирамиды
	for i in range(n//2 , -1, -1):
		heapify(lst, n, i)
	# Извлечение элемента
	for i in range(n-1, 0, -1):
		global k #Счет перестановок
		k += 1
		lst[i], lst[0] = lst[0], lst[i] # перестановка
		heapify(lst, i, 0)



#Первая часть

#Блок ввода списка
n = None  #Длина списка
while True:
	var = input('Введите длину списка: ')
	try:
		n = int(var)
		if n <= 0:
			print('Длина должна быть больше 0')
			continue
		break
	except:
		print('Введите целое число больше 0')
print()

k = 0 #Fake_k
lst = [0] * n #Список

#Ввод элементов списка
for i in range(n):
	while True:
		var = input(f'Введите {i + 1}-й элемент массива: ')
		try:
			lst[i] = float(var) # i элемент списка
			break
		except:
			print('Введите вещественное число')
		print()
print()

heapSort(lst)
print('Отсортированный список: ')
for i in range(n):
	print(f'{i + 1} элемент спска: {lst[i]:.5g}')
print()



#Вторая часть

#Функция создания рандомного списка
def Rand_list(n):
	lst = []
	for i in range(n):
		lst.append(r.randint(-100,100))
	return lst 

#Функция создания отсортированного списка
def Sort_list(n):
	lst = [i for i in range(1,n+1)]
	return lst
	
#Функция создания обратно отсортированного списка 
def Rev_sort_list(n):
	lst = [i for i in range(n,0,-1)]
	return lst

#Справка по трёхмерной матрице

#                                
#              reversesorted list->/         /|
#                  random list->  /         / |
#               sorted list->    /         /  |
#              N1       ->      | t1   k1 |  /
#              N2       ->      | t2   k2 | /
#              N3       ->      | t3   k3 |/
#
# № матрицы - вид списка
# строка  - длина списка
# столбец: [0] - время сортировки, [1] - число перестановок элементов

#Блок ввода длин списков
N = [0] * 3

for i in range(3):
	while True:
		var = input(f'Введите N{i + 1}: ')
		try:
			N[i] = int(var)
			if N[i] <= 0:
				print('Длина должна быть больше 0')
				continue
			break
		except:
			print('Введите целое число больше 0')
print()

list_types = ['Упорядоченный список', 'Случайный список', 'Упорядоченный в обратном порядке'] #Виды списков

data_v = [[[0]*2 for i in range(3)] for j in range(3)] #Трехмерная матрица данных, описанная выше

#Блок подсчета времени и кол-ва перстановок
for i in range(3):
	types = [Sort_list(N[i]), Rand_list(N[i]), Rev_sort_list(N[i])] #Создание списков по видим с заданной длиной N[i]
	for j in range(3):
		lst = types[j]
		k = 0 #Кол-во перестановок(поменяется после выполнения ф-ции)
		time_start = t.time()
		heapSort(lst)
		time_end = t.time()
		delt_time = time_end - time_start #Поиск времени выполнения
		data_v[j][i][0], data_v[j][i][1] = delt_time, k

#Блок вывода
print('{:^123s}'.format('Таблица'))
#Шапка таблицы
print('-'*123)
print('|{:^34s}'.format(''), end='|')
for i in range(3):
	print('{:^28.5g}'.format(N[i]), end='|')
print()
print('|',' '*34, '|', '-'*28, '|', '-'*28, '|', '-'*28, '|', sep='')
print('|{:^34s}'.format(''), end='|')
for i in range(3):
	print('{:^11s}|{:^16s}'.format('Время','Перестановки'), end='|')
print()
print('|','-'*121, '|', sep='')

#Основная часть таблицы
for i in range(3):
	print('|{:^34s}'.format(list_types[i]), end='|')
	for j in range(3):
		print('{:^11.2g}|{:^16.5g}'.format(data_v[i][j][0],data_v[i][j][1]), end='|')
	print()
print('-'*123)
