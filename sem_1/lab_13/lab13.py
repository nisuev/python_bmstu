# Нисуев Нису Иу7-12Б
# Работа с файлами и базой данных
# База данных - антропометрия человека
import os
		
#Функция для выбора файла
def file_choice(file):
	file_list = os.listdir()
	if file == 'lab13.py':
		print('Нельзя открывать файл программы')
		return
	if file in file_list:
		print(f'Программа работает с файлом {file}')
		return file
	else:
		try:
			f = open(file,'w')
			os.remove(file)
			print('Такого файла не существует')
		except:
			print('Имя файла введено неверно')

#Функция для ввода файла
def file_input(file):
	file = None
	while file == None:
		file = input('Введите название файла, в которую хотите инициализировать базу данных: ')
		if file == 'lab13.py':
			print('Нельзя инициализировать базу данных в файл программы')
			file == None
		else:
			try:
				f = open(file, 'w', encoding = 'utf-8')
				f.close()
				return  file
			except:
				print('Имя файла введено неверно')

# Функция инициализации базы данных
def data_initial(file, data_head):
	ver = None
	if file == 'l13.py':
		print('Нельзя инициализировать базу данных в файл программы')
		return
	
	if file == None:
		return
	
	print('Как вы хотите инициализировать базу данных?')
	print('1. Ручным вводом')
	print('2. Заданным шаблоном')
	print()
	ver = input_act(ver, 2, 1)
	with open(file, 'w', encoding = 'utf-8') as f:
		
		if ver == 1: #Ввод вручную
			num_str = None #Кол-во записываемых строк
			while True:
				var = input('Введите кол-во строк базы данных: ')
				try:
					num_str = int(var)
					break
				except:
					print('Введите целое число строк')
					
			for i in range(num_str):
				str_data = '' #Строка базы данных
				for j in range(4):
					
					if j == 0: #Ввод имени
						name = input(f'Введите {data_head[j]} {i + 1}-го человека: ')
						while not name.isalpha():
							print(f'{name} не является именем')
							name = input(f'Введите {data_head[j]} {i + 1}-го человека: ')
						name = name[0].upper() + name[1:].lower()
						str_data += name
						str_data += '|'
					
					if j == 1: #Ввод пола
						male = (input(f'Введите {data_head[j]} {i + 1}-го человека: ')).lower()
						while male != 'м' and male != 'ж':
							print('Введите [м/ж] в зависимости от пола')
							male = (input(f'Введите {data_head[j]} {i + 1}-го человека: ')).lower()
						str_data += male
						str_data += '|'
					
					if j == 2: #Ввод роста
						height = None
						while True:
							var = input(f'Введите {data_head[j]} {i + 1}-го человека в сантиметрах: ')
							try:
								height = float(var)
								if height <= 0:
									print('Рост не может быть отрицательным или равен нулю')
									continue
								break
							except:
								print('Введите числовое значение роста')
						height = f'{height:.5g}см'
						str_data += height
						str_data += '|'
					
					if j == 3: #Ввод веса
						weight = None
						while True:
							var = input(f'Введите {data_head[j]} {i + 1}-го человека в кг: ')
							try:
								weight = float(var)
								if weight <= 0:
									print('Вес не может быть отрицательным или равен нулю')
									continue
								break
							except:
								print('Введите числовое значение роста')
						weight = f'{weight:.5g}кг'
						str_data += weight
				f.write(str_data) #Запись строки
				f.write('\n') #Перевод на новую
		
		if ver == 2: #Ввод по шаблону
			f.write('Иван|м|183м|77кг\n')
			f.write('Карина|ж|168м|55кг\n')
			f.write('Мага|м|210м|90кг\n')
			f.write('Марья|ж|150м|45кг\n')

# Функция вывода базы данных
def file_out(file, data_head):
	os.chmod(file, 0o777) #Выдача полных прав на файл пользователю
	max_len = [3, 3, 4, 3] #Список максимальных длин строк по столбцам
	
	f = open(file, 'r', encoding='utf-8')
	
	#Нахождение максимальных длин строк по столбцам
	for i in f:
		string_data = i.strip()
		if string_data == '':
			print('База данных пуста')
			return
		data_str = string_data.split('|')
		for j in range(4):
			if len(data_str[j]) > max_len[j]:
				max_len[j] = len(data_str[j]) + 2
	
	f.close()
	#Блок вывода
	print('-'*(sum(max_len) + 5))
	
	for i in range(4):
		print(f'|{data_head[i]:^{max_len[i]}}',end='')
	print('|')
	print('-'*(sum(max_len) + 5))
	
	f = open(file, 'r', encoding='utf-8')
	for i in f:
		string_data = i.strip()
		data_str = string_data.split('|')
		for j in range(4):
				print(f'|{data_str[j]:^{max_len[j]}}',end='')
		print('|')
	print('-'*(sum(max_len) + 5))
	f.close()

# Дозапись строк в базу данных
def file_add(file, data_head):
	os.chmod(file, 0o777) #Выдача полных прав на файл пользователю

	with open(file, 'a', encoding = 'utf-8') as f:
		num_str = None #Кол-во дозаписываемых строк 
		while True:
			var = input('Введите кол-во строк, которое хотите дозаписать: ')
			try:
				num_str = int(var)
				break
			except:
				print('Введите целое число строк')
					
		for i in range(num_str):
			str_data = '' #Дозаписываемая строка
			for j in range(4):
				
				if j == 0: #Ввод имени
					name = input(f'Введите {data_head[j]} {i + 1}-го человека: ')
					while not name.isalpha():
						print(f'{name} не является именем')
						name = input(f'Введите {data_head[j]} {i + 1}-го человека: ')
					name = name[0].upper() + name[1:].lower()
					str_data += name
					str_data += '|'
					
				if j == 1: #Ввод пола
					male = (input(f'Введите {data_head[j]} {i + 1}-го человека: ')).lower()
					while male != 'м' and male != 'ж':
						print('Введите [м/ж] в зависимости от пола')
						male = (input(f'Введите {data_head[j]} {i + 1}-го человека: ')).lower()
					str_data += male
					str_data += '|'
					
				if j == 2: #Ввод роста
					height = None
					while True:
						var = input(f'Введите {data_head[j]} {i + 1}-го человека в сантиметрах: ')
						try:
							height = float(var)
							if height <= 0:
								print('Рост не может быть отрицательным или равен нулю')
								continue
							break
						except:
							print('Введите числовое значение роста')
					height = f'{height:.5g}см'
					str_data += height
					str_data += '|'
					
				if j == 3: #Ввод веса
					weight = None
					while True:
						var = input(f'Введите {data_head[j]} {i + 1}-го человека в кг: ')
						try:
							weight = float(var)
							if weight <= 0:
									print('Вес не может быть отрицательным или равен нулю')
									continue
							break
						except:
							print('Введите числовое значение роста')
					weight = f'{weight:.5g}кг'
					str_data += weight
			f.write(str_data) #Дозапись строки
			f.write('\n') #Перевод на новую

# Функция для поиска по одному критериям
def str_find_1(file, data_head):
	os.chmod(file, 0o777) #Выдача полных прав на файл пользователю
	
	crit = None
	print('Введите критерий по которому хотите найти информацию')
	data_list()
	crit_num = input_crit_num(crit) - 1
	print()
	crit = input_crit(crit_num)
	print()
	crit_data = [] #Список строк подходящих по критерию
	f = open(file, 'r', encoding='utf-8')
	#Нахождение строк подходящих по критерию
	for i in f:
		string_data = i.strip()
		data_str = string_data.split('|')
		if data_str[crit_num] == crit:
			crit_data.append(data_str)
	
	if len(crit_data) == 0:
		print('Совпадений нет')
	else:
		max_len = [3, 3, 4, 3] #Список максимальных длин строк по столбцам
		for i in range(len(crit_data)):
			for j in range(4):
				if max_len[j] < len(crit_data[i][j]):
					max_len[j] = len(crit_data[i][j]) + 2
		#Блок вывода
		print('-'*(sum(max_len) + 5))
		
		for i in range(4):
			print(f'|{data_head[i]:^{max_len[i]}}',end='')
		print('|')
		print('-'*(sum(max_len) + 5))
	
		f.seek(0) #Переход к началу файла
		for i in range(len(crit_data)):
			for j in range(4):
				print(f'|{crit_data[i][j]:^{max_len[j]}}',end='')
			print('|')
		print('-'*(sum(max_len) + 5))

# Функция для поиска по двум критериям
def str_find_2(file, data_head):
	os.chmod(file, 0o777) #Выдача полных прав на файл пользователю
	
	crit_1 = None
	print('Введите 1-ый критерий по которому хотите найти информацию')
	data_list()
	crit_num_1 = input_crit_num(crit_1) - 1 #Номер первого критерия
	print()
	crit_1 = input_crit(crit_num_1) #Первый критерий
	print()
	
	crit_2 = None
	print('Введите 2-ой критерий по которому хотите найти информацию')
	data_list()
	crit_num_2 = input_crit_num(crit_2) - 1 #Номер второго критерия
	print()
	while crit_num_1 == crit_num_2:
		print('Второй критерий должен отличаться от первого')
		crit_num_2 = input_crit_num(crit_2) - 1
	crit_2 = input_crit(crit_num_2) #Второй критерий
	print()
	crit_data = [] #Список строк подходящих по критерию
	f = open(file, 'r', encoding='utf-8')
	#Нахождение строк подходящих по критерию
	for i in f:
		string_data = i.strip()
		data_str = string_data.split('|')
		if data_str[crit_num_1] == crit_1 and data_str[crit_num_2] == crit_2:
			crit_data.append(data_str)
	
	if len(crit_data) == 0:
		print('Совпадений нет')
	else:
		max_len = [3, 3, 4, 3] #Список максимальных длин строк по столбцам
		for i in range(len(crit_data)):
			for j in range(4):
				if max_len[j] < len(crit_data[i][j]):
					max_len[j] = len(crit_data[i][j]) + 2
		#Блок вывода
		print('-'*(sum(max_len) + 5))
		
		for i in range(4):
			print(f'|{data_head[i]:^{max_len[i]}}',end='')
		print('|')
		print('-'*(sum(max_len) + 5))
	
		f.seek(0) #Переход к началу файла
		for i in range(len(crit_data)):
			for j in range(4):
				print(f'|{crit_data[i][j]:^{max_len[j]}}',end='')
			print('|')
		print('-'*(sum(max_len) + 5))

# Функция для ввода номера критерия
def input_crit_num(crit):
	while True:
		var = input('Введите номер действия: ')
		try:
			crit = int(var)
			if crit < 1 or crit > 4:
				print('Введите номер из перечисленных критериев')
				continue
			return crit
		except:
			print('Введите целое число из перчисленных')

# Ввод критерия по номеру
def input_crit(crit):
	if crit == 0: #Ввод имени
		name = input(f'Введите искомое  {data_head[crit]}: ')
		while not name.isalpha():
			print(f'{name} не является именем')
			name = input(f'Введите искомое  {data_head[crit]}: ')
		name = name[0].upper() + name[1:].lower()
		return name
					
	if crit == 1: #Ввод пола
		male = (input(f'Введите искомый {data_head[crit]}: ')).lower()
		while male != 'м' and male != 'ж':
			print('Введите [м/ж] в зависимости от пола')
			male = (input(f'Введите искомый {data_head[crit]}: ')).lower()
		return male
					
	if crit == 2: #Ввод роста
		height = None
		while True:
			var = input(f'Введите искомый {data_head[crit]} в сантиметрах: ')
			try:
				height = float(var)
				if height <= 0:
					print('Рост не может быть отрицательным или равен нулю')
					continue
				break
			except:
				print('Введите числовое значение роста')
		height = f'{height:.5g}см'
		return height
					
	if crit == 3: #Ввод веса
		weight = None
		while True:
			var = input(f'Введите искомый {data_head[crit]} в кг: ')
			try:
				weight = float(var)
				if weight <= 0:
					print('Вес не может быть отрицательным или равен нулю')
					continue
				break
			except:
				print('Введите числовое значение роста')
		weight = f'{weight:.5g}кг'
		return weight

# Функция для вызова меню
def menu(): 
	print('-'*15,'Меню','-'*15,sep='')
	print('[0] - Выход из программы')
	print('[1] - Выбор файла для работы')
	print('[2] - Инициализация базы данных')
	print('[3] - Вывод содержимого базы данных')
	print('[4] - Добавление записи в конец базы данных')
	print('[5] - Поиск по одному полю')
	print('[6] - Поиск по двум полям')
	print()
	return ''
	
# Функция для ввода номера действия
def input_act(act, num_end, num_begin):
	while True: 
		var = input('Введите номер действия: ')
		try:
			act = int(var)
			if act < num_begin or act > num_end:
				print('Введите номер из перечисленных действий')
				continue
			return act
		except:
					print('Введите целое число из перчисленных в меню')

act = None # Действие
work_file = None  # Файл для работы
data_head = ['Имя', 'Пол', 'Рост', 'Вес']  # Шапка базы данных

# Функция для вызова критериев базы данных
def data_list():
	print('1. Имя')
	print('2. Пол')
	print('3. Рост(в см)')
	print('4. Вес(в кг)')
	print()
	return ''

# Работа программы по номеру действия
while act != 0:
	menu()
	act = input_act(act, 6, 0) #Ввод номера действия
	print()
	
	if act == 0: 
		print('Выход из программы')
	
	if act == 1:
		file = None
		file = input('Введите файл для работы: ')
		work_file = file_choice(file)
	
	if act == 2:
		file = None
		file = file_input(file)
		data_initial(file, data_head)
	
	if act == 3:
		if work_file == None:
			print('Не выбран файл для работы')
		else:
			file_out(work_file, data_head)
			
	if act == 4:
		if work_file == None:
			print('Не выбран файл для работы')
		else:
			file_add(work_file, data_head)
	
	if act == 5:
		if work_file == None:
			print('Не выбран файл для работы')
		else:
			str_find_1(work_file, data_head)
	
	if act == 6:
		if work_file == None:
			print('Не выбран файл для работы')
		else:
			str_find_2(work_file, data_head)	
	
	print()	
