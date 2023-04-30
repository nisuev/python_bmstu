def mat_in() -> list[list[int]]:
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


def mat_out(matrix: list[list[int]]) -> None:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        print('|', end='')
        for j in range(m):
            print(f'{matrix[i][j]:^5}', end='')
        print(''
              '|')
    print()


# Транспонирование матрицы
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])

    transp_matrix = []
    for j in range(m):
        transp_matrix.append([])
        for i in range(n):
            transp_matrix[j].append(matrix[i][j])

    return transp_matrix


# Поворот матрицы на 90 по и против часовой
def rotate(matrix, direct):

    n = len(matrix)
    m = len(matrix[0])

    if direct == '90->':
        r_matrix = []
        for j in range(m):
            r_matrix.append([])
            for i in range(n):
                r_matrix[j].insert(0, matrix[i][j])

    if direct == '<-90':
        r_matrix = []
        for j in range(m):
            r_matrix.insert(0, [])
            for i in range(n):
                r_matrix[0].append(matrix[i][j])

    return r_matrix


mat = mat_in()
print('Матрица')
mat_out(mat)

tranp_mat = transpose(mat)
print('Транспонированная матрица')
mat_out(tranp_mat)