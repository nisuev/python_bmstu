# Треугольник Паскаля
def PascalTriangle(n: int) -> None:
    list_triangle = []
    triangle_top = [1]
    for i in range(n):
        list_triangle.append(triangle_top)
        triangle_top = [sum(x) for x in zip([0] + triangle_top, triangle_top + [0])]

    for i in range(n):
        top = ''
        for j in range(len(list_triangle[i])):
            if j != len(list_triangle[i]) - 1:
                top += str(list_triangle[i][j])
                top += '   '
            else:
                top += str(list_triangle[i][j])
        list_triangle[i] = top

    max_ln = len(list_triangle[-1])
    for i in list_triangle:
        print(f'{i:^{max_ln}}')


num = int(input('Введите кол-во строк: '))
PascalTriangle(num)
