#дана целочисленная матрица. Найти минимум и максимум, и посчитать сумму всех элементов подматрицы образованную этим минимумом и максимумом
n = int(input('введите кол-во строк: '))
m = int(input('Введите кол-во столбцов: '))
print()

mtx =[]
min_el,max_el = float('inf'), float('-inf')
ind_max  = ind_min = (-1, -1)
for i in range(n):
    mtx.append([])
    for j in range(m):
        mtx[i].append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: ')))
        if mtx[i][j] < min_el:
            min_el = mtx[i][j]
            ind_min = (i , j)
        if mtx[i][j] > max_el:
            max_el = mtx[i][j]
            ind_max = (i , j)
    print()

print('Матрица')
for i in range(n):
    for j in range(m):
        print('{:5}'.format(mtx[i][j]),end='')
    print()

if ind_min[0] > ind_max[0]:
    ind_min, ind_max = (ind_max[0], ind_min[1]), (ind_min[0], ind_max[1])

if ind_min[1] > ind_max[1]:
    ind_min, ind_max = (ind_min[0], ind_max[1]), (ind_max[0], ind_min[1])

sum_el = 0            
for i in range(ind_min[0],ind_max[0] + 1):
    for j in range(ind_min[1],ind_max[1] + 1):
        sum_el += mtx[i][j]
        
print('Сумма элементов подматрицы образованная минимумом и максимумом: ', sum_el)
