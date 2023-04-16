#Нисуев Нису ИУ7-12Б
#Вар 3. Замена всех заглавных согласных английских букв на строчные

Cps_let = 'BCDFGHJKLMNPQRSTVWXZ' #заглавные согласные буквы
'''str_let = 'bcdfghjklmnpqrstvwxz' #строчные согласные буквы'''ds

n = int(input('Введите размер массива: '))

while  n < 1:
	print('В списке должно быть больше 0 элементов')
	n = int(input('Введите размер массива: '))

lst = []

for i in range(n):
	el = input(f'Введите {i + 1} элемент последовательности: ')
	new_el = '' #Создание нового элемента
	for j in range(len(el)):
		if el[j] in Cps_let: #Проверка на принадлежность к заглавным согласным буквам
			'''ind = Cps_let.index(el[j]) #Нахождение буквы
			new_el += str_let[ind] #Замена ее на строчную'''
			new_el += el[j].lower()
		else:
			new_el += el[j]
	lst.append(new_el)
	
print('Замененный список:')
for i in range(n):
	print(f'{i + 1} элемент: {lst[i]}')
