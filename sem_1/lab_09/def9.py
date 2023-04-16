#в матрице найти строку с наибольшим кол-вом 0 и поменять со столбцом с наибольшей суммой элементов

n = int(input('Введите кол-во строк матрицы: '))
m = int(input('Введите кол-во столбцов матрицы: '))



matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(float(input(f'Введите {j + 1} элемент {i + 1} строки: ')))
    print()

print('Введенная матрица')   
for i in range(n):
    for j in range(m):
        print('{:10.5g}'.format(matrix[i][j]),end='')
    print()


if n != m:
    print('В матрице невозможно поменять строку и столбец, т.к. матрица не квадратная')

else:
    max_nul = -1
    ind_nul = -1
    for i in range(n):
        k_nul = 0
        for j in range(m):
            if matrix[i][j] == 0:
                k_nul += 1
        if k_nul > max_nul:
            max_nul = k_nul
            ind_nul = i

    if ind_nul == -1:
        print('В матрице нет строк содержащих нули')

    else:
        ind_max = -1
        max_sum = -1
        for j in range(m):
            sum_el = 0
            for i in range(n):
                sum_el += matrix[i][j]
            if sum_el > max_sum:
                max_sum = sum_el
                ind_max = j

        if m >= n:
            for i in range(n):
                for j in range(m):
                    matrix[ind_nul][m - j - 1], matrix[i][ind_max] = matrix[i][ind_max], matrix[ind_nul][m - j - 1]

        print('Заменненая матрица')   
        for i in range(n):
            for j in range(m):
                print('{:10.5g}'.format(matrix[i][j]),end='')
            print()
