def mat_in():
    n = int(input('Введите количество строк матрицы: '))
    m = int(input('Введите количество столбцов матрицы: '))

    while m <= 0 or n <= 0:
        print('В матрице должно быть больше нуля столбцов и строк')
        n = int(input('Ввдите количество строк матрицы: '))
        m = int(input('Ввдите количество столбцов матрицы: '))

    matrix = []
    for i in range(n):
        print()
        matrix.append([])
        for j in range(m):
            matrix[i].append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: ')))
    print()

    return matrix


def mat_out(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(f'{matrix[i][j]:8.4g}', end='')
        print()
    print()


def mat_multy(mat1, mat2):  # mat1 * mat2
    # Размерность матрицы №1
    n1 = len(mat1)
    m1 = len(mat1[0])

    # Размерность матрицы №2
    n2 = len(mat2)
    m2 = len(mat2[0])

    if m1 != n2:
        print('Матрицы нельзя перемножить')
        return None

    mat_mult = []
    for n in range(n1):
        mat_mult.append([])
        for i in range(m2):
            sum_el = 0
            for j in range(m1):
                sum_el += mat1[n][j] * mat2[j][i]
            mat_mult[n].append(sum_el)
    return mat_mult


def yes_not(before):
    acts = ['n', 'y']
    act = input(f'{before} [y/n]: ').lower()
    print()

    while act not in acts:
        print('Введите [y/n]')
        act = input(f'{before} [y/n]: ').lower()
        print()

    return acts.index(act)


print('Матрица-множимое')
matrix_1 = mat_in()
temp = yes_not('Вывести матрицу-множимое')
if temp == 1:
    mat_out(matrix_1)

print('Матрица-множитель')
matrix_2 = mat_in()
temp = yes_not('Вывести матрицу-множитель')
if temp == 1:
    mat_out(matrix_2)

mult_matrix = mat_multy(matrix_1, matrix_2)
if mult_matrix is not None:
    print('Матрица-произведение')
    mat_out(mult_matrix)