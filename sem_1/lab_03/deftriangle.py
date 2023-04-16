# найти медиану из наибольшего угла
xa = int(input('Введите координату Х первой точки '))
ya = int(input('Введите координату Y первой точки '))
xb = int(input('Введите координату Х второй точки '))
yb = int(input('Введите координату Х второй точки '))
xc = int(input('Введите координату Х третьей точки '))
yc = int(input('Введите координату Х третьей точки '))


AB = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
BC = ((xc - xb) ** 2 + (yc - yb) ** 2) ** 0.5
AC = ((xc - xa) ** 2 + (yc - ya) ** 2) ** 0.5


maxside, srside, minside = AB, BC, AC
if maxside < srside:
    maxside, srside = srside, maxside
if srside < minside:
    srside, minside = minside, srside
if maxside < srside:
    maxside, srside = srside, maxside


m_ABC = ((2 * minside ** 2 + 2 * srside ** 2 - maxside ** 2) ** 0.5) / 2
print('Медиана проведенная из наибольшего угла = {:.5g}'.format(m_ABC))
