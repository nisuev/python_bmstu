#Нисуев Нису ИУ7-12Б
#Лабораторная работа №12
#Работа с текстом по заданному меню
#Умножение и деление
#Поиск предложения с макс кол-вом слов с черед буквами

def left_txt(txt): #Функция для выравнивания по левому краю
	for i in range(len(txt)):
		txt[i] = txt[i].strip() #Удаление крайних пробелов
		while "  " in txt[i]:
			txt[i] = txt[i].replace("  ", " ") #Удаление смноженных пробелов

def right_txt(txt): #Функция для выравнивания по правому краю
	left_txt(txt) #выравнивание по левому краю

	global max_ln
	for i in range(len(txt)):
		txt[i] = (' ' * (max_ln - len(txt[i]))) + txt[i]

def width_txt(txt): #Функция для выравнивания по ширине
	left_txt(txt) #выравнивание по левому краю
	
	global max_ln
	for i in range(len(txt)):
		ln_string = len(txt[i])
		if txt[i].count(" ") == 0:
			continue
		else:
			n_gap, max_rep = divmod(max_ln - ln_string + txt[i].count(" "), txt[i].count(" "))
			txt[i] = txt[i].replace(" ", " " * n_gap).replace(" " * n_gap, " " * (n_gap + 1), max_rep)

def delword(txt, word): #Функция для удаления слова
	punct_1 = '.,?!:; ' #Одиночные знаки препинания
	punct_2 = ['""','()','[]','{}'] #Сдвоенные знаки препинания
	for i in range(len(txt)):
		if word in txt[i]:
			txt[i] = txt[i].replace(word, '') #Удаление слова
			for s in punct_2:
				txt[i] = txt[i].replace(s, '')  #Удаление сдвоенных знаков
			for s in punct_1:
				s_gap = ' ' + s
				txt[i] = txt[i].replace(s_gap, s) #Удаление одиночных знаков
			
def replace_word(txt, old_word, new_word): #Функция для замены слова на новое
	for i in range(len(txt)):
		txt[i] = txt[i].replace(old_word, new_word)
		
# Нахождение значений выражений в тексте
def arifmetic_calc(txt):
	count = 0  # Счётчик вычисленных выражений
	exp = []  # Список содержащий текущее выражение
	dig = ""  # Текущее число
	for i in range(len(txt)):
		string = txt[i]  # Текущая строка
		for j in range(len(txt[i])):
			if string[j].isdigit(): #Если цифра
				if not dig and not exp:
					start = j  # Начало отсчёта выражения
				dig += string[j]  # Добавление текущего символа к числу
			elif string[j].isalpha() or string[j] in '.,":-;!?': #Если символ или знак
				if dig:
					if exp:
						if exp[-1] in "*/":
							exp.append(dig)  # Добавление числа в список
							dig = ""
				if len(exp) > 2 and len(exp) % 2 != 0: #Проверка на возможность счета
					end = j if string[j - 1] == " " else j + 1 #Конец выражения
					result = int(exp[0])  # Результат выражения
					k = 1
					while k < len(exp):
						if exp[k] == "*":
							result *= int(exp[k + 1])  # Умножение
							zero = False
						elif exp[k] == "/":
							try:
								result /= int(exp[k + 1])  # Деление
							except ZeroDivisionError:
								zero = True  # Произошло деление на 0
								break
							else:
								zero = False
						k += 2
					if not zero:
						txt[i] = txt[i].replace(string[start: end - 1], str(f"{result:.1g}"), 1) # Изменение строки с добавлением результата
						count += 1
					zero = False
				exp = []
			elif string[j] == " ": #Если пробел
				if dig:
					if exp:
						if exp[-1].isdigit():
							exp.pop(-1)  # Удаление числа из списка
					exp.append(dig)  # Добавление числа в список
					dig = ""
			elif string[j] in "*/": #Если знак умножения или деления
				if dig:
					if exp:
						if exp[-1].isdigit():
							exp.pop(-1)  # Удаление числа из списка
					exp.append(dig)  # Добавление числа в список
					dig = ""
				if exp:
					if exp[-1].isdigit():
						exp.append(string[j])  # Добавление знака в список
					else:
						exp.pop(-1)
		exp = []
	return count

def del_sentence(txt): #Функция для удаления предложения с максимальным кол-вом слов, в которых чередуются гласные и согласные
	txt_2 = txt.copy() 
	for i in range(len(txt_2)):
		txt_2[i] = txt_2[i] + '##'
	txt_2 = ' '.join(txt_2)
	txt_2 = " ".join(txt_2.split())
	txt_2 = txt_2.split('. ') #Создание списка предложений с определенным разделителем на строки
	for i in range(len(txt_2) - 1):
		txt_2[i] += '.'
	l = [0] * len(txt) #Список длин строк
	for i in range(len(txt)):
		l[i] = len(txt[i]) #Кол-во символов в строке
	txt = ' '.join(txt)
	txt = " ".join(txt.split())
	txt = txt.split('. ') #Создание списка предложений
	for i in range(len(txt) - 1):
		txt[i] += '.' #Возврат точки
	word_count = [0] * len(txt) #Список счетчика слов с критерием по предложениям
	for i in range(len(txt)):
		words = txt[i].split() #Список слов строки
		for j in range(len(words)):
			if isCriteria(words[j]): #Проверка слов на критерий
				word_count[i] += 1 #Счет кол-ва подходящих слов
	print(f'{index_max(word_count) + 1} предложение:') #Вывод номера предложения
	print(txt[index_max(word_count)]) #Вывод предложения
	print('\n\n')
	txt_2.pop(index_max(word_count)) #Удаление предложения
	#Возврат к строчному виду текста
	txt_2 = ' '.join(txt_2)
	txt_2 = txt_2.split('##')
	
	#Присваивание текстовуму файлу нового вида
	global text
	text = txt_2
	left_txt(text)

def isCriteria(wrd): #Проверка на чередующиеся буквы в слове
	gl = 'aeyuioAEYUIOыуаеиоюэёяЯЫУАЕИОЮЭЁ'
	sogl = 'qzwsxdcrfvtgbhnjmklpQZWSXDCRFVTGBHNJMKLPйфцчвскмпнртгшлбщдзжхЙФЦЧВСКМПНРТГШЛБЩДЗЖХ'

	if wrd[0] in gl:
		letter = gl
	else:
		letter = sogl   
	for i in wrd:
		if i in letter:
			if letter == gl:
				letter = sogl
			else:
				letter = gl
		else:
			return False
		return True

def index_max(m): #нахождение индекса предложения со словами, в котором чеедуются гласные и согласные
	mx = m[0]
	mx_ind = 0
	for i in range(1, len(m)):
		if mx < m[i]:
			mx = m[i]
			mx_ind = i
	return mx_ind
	

def txtout(txt): #Функция для вывода текста
	for i in txt:
		print(i)
	print('\n\n')

def menu(): #Функция для вызова меню
	print('Меню')
	print('[0] - Выход из программы')
	print('[1] - Выравнивание текста по левому краю')
	print('[2] - Выравнивание текста по правому краю')
	print('[3] - Выравнивание текста по ширине')
	print('[4] - Удаление всех вхождений заданного слова')
	print('[5] - Замена одного слова другим')
	print('[6] - Вычисление умножений и вычитаний внутри текста')
	print('[7] - Удаление предложения с максимальным кол-вом слов, в котором гласные чередуются с согласными')
	print('[8] - Вывод текста')
	return ''
	
def input_act(act): #Функция для ввода номера действия
	while True: 
		var = input('Введите номер действия: ')
		try:
			act = int(var)
			if act < 0 or act > 8:
				print('Введите номер из перечисленных действий')
				continue
			return act
		except:
					print('Введите целое число из перчисленных в меню')


allign = 1 #хранение выравнивания

def save_allign(txt): #Функция для сохранения выравнивания
	global allign
	if allign == 1:
		left_txt(txt)
		
	if allign == 2:
		right_txt(txt)
		
	if allign == 3:
		width_txt(txt)
	
print(menu()) #Вывод меню

act = None #Номер действия
text = ['И точно, она была хороша: высокая, тоненькая, глаза черные, как у горной серны, так и заглядывали',
'к вам в душу. Печорин в задумчивости не сводил с нее глаз, и Она частенько исподлобья на него',
'посматривала. Только не один (Печорин) - 8 / 3 любовался хорошенькой княжной: из угла комнаты на нее смотрели',
'другие два глаза, неподвижные, огненные. Я стал вглядываться и узнал моего старого',
'знакомца Казбича. Он, 1 * 2 знаете, был не то, чтоб мирной, не то, чтоб немирной. Подозрений',
'на него было много, хоть он ни в какой шалости не был замечен. Бывало, он',
'приводил к нам в крепость баранов и продавал дешево, только никогда не торговался: что',
'запросит, давай, хоть зарежь, не 11 * 26 уступит -1 * 2 * 3.'] #Текст


max_ln = 0 #Длина максимальной строки
for i in text:
	max_ln = max(max_ln,len(i))


#Исполнение действий
while act != 0:
	act = input_act(act) #Ввод номера действия
	
	if act == 0: 
		print('Выход из программы')
	
	if act == 1:
		left_txt(text)
		allign = 1
	
	if act == 2:
		right_txt(text)
		allign = 2
	
	if act == 3:
		width_txt(text)
		allign = 3
	
	print('\n\n')
	if act == 4:
		while True:
			word = input("Введите слово которое хотите удалить: ")
			if word.isalpha():
				break
			else:
				print("Вы ввели не слово")
		
		delword(text, word)
		save_allign(text)
	
	if act == 5:
		while True:
			old_word = input("Введите слово которое хотите заменить: ")
			if old_word.isalpha():
				break
			else:
				print("Вы ввели не слово")
		while True:
			new_word = input("Введите слово которым хотите заменить: ")
			if new_word.isalpha():
				break
			else:
				print("Вы ввели не слово")
	
		replace_word(text, old_word, new_word)
		save_allign(text)

	if act == 6:
		arifmetic_calc(text)
		save_allign(text)
		
	if act == 7:
		del_sentence(text)
		save_allign(text)
	
	if act == 8:
		txtout(text)
