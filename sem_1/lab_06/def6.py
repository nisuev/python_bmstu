#список целых
#заменить первый нулевой на среднее арифметическое положительных

n = int(input('Введите размер массива: '))

lst = [0] * n
ind_nul = -1

for i in range(n):
    lst[i] = int(input(f'Введите {i + 1} элемент последовательности: '))
    if lst[i] == 0 and ind_nul == -1:
        ind_nul = i         

if lst.count(0) == 0:
    print('В списке нет нулевых значений')

else:
    k_p = 0
    sum_p = 0

    for i in range(n):
        if lst[i] > 0:
            k_p += 1
            sum_p += lst[i]

    if k_p == 0 and sum_p == 0:
        print('В списке нет положительных элементов')

    else:
        sr_ar = sum_p / k_p
        lst[ind_nul] = sr_ar
        print('Измененный список: ')
        for i in range(n):
            print(f'{i + 1} элемент последовательности: {lst[i]}')
