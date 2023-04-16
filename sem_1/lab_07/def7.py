#Защита 7 лабораторной
#дан список строк. В строке содержащей самое большое кол-во запятых, заменить запятые на соответсвующие колво пробелов

n = int(input('Введите длину списка: '))
lst = [0] * n
max_com = -1
ind_max = -1
for i in range(n):
    lst[i] = input(f'Введите {i + 1} элемент списка: ')
    k_com = 0
    for j in lst[i]:
        if j == ',':
            k_com += 1
    if k_com > max_com:
        max_com = k_com
        ind_max = i
print()

new_el = ''
for i in lst[ind_max]:
    if i == ',':
        new_el += ' '
    else:
        new_el += i

lst[ind_max] = new_el

print('Список с измененным элементом')
for i in range(n):
    print(f'{i + 1} элемент:', lst[i])
