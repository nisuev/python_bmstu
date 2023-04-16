# Нисуев Нису ИУ7-12Б лаб№3
# нахождение сторон треугольника, высоты этого треугольника к большей стороне
# проверка остроугольности
# расположение введенной точки по отношению к этому треугольнику
# расстояние от этой точки до треугольника если она находится в нем
# Введем координаты  точек треугольника АВС
xA = int(input('Введите кординату Х первой точки: '))
yA = int(input('Введите кординату Y первой точки: '))
xB = int(input('Введите кординату Х второй точки: '))
yB = int(input('Введите кординату Y второй точки: '))
xC = int(input('Введите кординату Х третьей точки: '))
yC = int(input('Введите кординату Y третьей точки: '))
eps = 0.00000000001

# формируем треугольник АВС
AB = ((xA-xB) ** 2 + (yA-yB) ** 2) ** 0.5
BC = ((xB-xC) ** 2 + (yB-yC) ** 2) ** 0.5
AC = ((xA-xC) ** 2 + (yA-yC) ** 2) ** 0.5

# Проверка на существование треугольника по теореме о сумме двух сторон больше третьей
if not((AB + BC) - AC > eps and (BC + AC) - AB > eps and (AC + AB) - BC > eps):
    print('Треугольника не существует')

else:
    # распределение сторон по возрастанию длин
    maxside, srside, minside = AB, BC, AC
    if maxside < srside:
        maxside, srside = srside, maxside
    if srside < minside:
        srside, minside = minside, srside
    if maxside < srside:
        maxside, srside = srside, maxside

    print('Стороны треугольника: {:.5g}, {:.5g}, {:.5g}'.format(maxside, srside, minside))
    p_ABC = (AB + BC + AC) / 2 # полупериметр ABC
    S_ABC = (p_ABC * (p_ABC - AB) * (p_ABC - BC) * (p_ABC - AC)) ** 0.5 # площадь ABC
    h = (2 * S_ABC) / maxside

    print('Высота проведенная из наибольшего угла = {:.5g}'.format(h))

    # проверка на остроугольность
    if maxside ** 2 < srside ** 2 + minside ** 2:
        print('Треугольник остроугольный')
    else:
        print('Треугольник не является остроугольным')

    # Введем координаты точки О
    xO = int(input('Введите координату Х: '))
    yO = int(input('Введите координату Y: '))

    # формируем треугольники ABO,ACO,BOC
    BO = ((xB-xO) ** 2 + (yB-yO) ** 2) ** 0.5
    CO = ((xC-xO) ** 2 + (yC-yO) ** 2) ** 0.5
    AO = ((xA-xO) ** 2 + (yA-yO) ** 2) ** 0.5

    # ищем полупериметры ABO,ACO,BOC
    p_ABO = (AB + BO + AO) / 2
    p_ACO = (AC + CO + AO) / 2
    p_BOC = (CO + BO + BC) / 2

    # ищем площади ABO,ACO,BOC
    S_ABO = (p_ABO * (p_ABO - AB) * (p_ABO - BO) * (p_ABO - AO)) ** 0.5
    S_ACO = (p_ACO * (p_ACO - AC) * (p_ACO - CO) * (p_ACO - AO)) ** 0.5
    S_BOC = (p_BOC * (p_BOC - CO) * (p_BOC - BO) * (p_BOC - BC)) ** 0.5

    # Доказываем нахождение точки O относительно треугольника ABC
    if (S_ABO + S_ACO + S_BOC) - S_ABC < eps:
        print('Точка принадлежит треугольнику')
        # ищем минимальное расстояние от точки до сторон треугольника АВС
        h_ABO = (2 * S_ABO) / AB
        h_ACO = (2 * S_ACO) / AC
        h_BOC = (2 * S_BOC) / BC
        if (h_BOC - 0) < eps or (h_ABO - 0) < eps or (h_ACO - 0) < eps:
            print('Точка лежит на стороне треугольника')
        else:
            r = min(h_BOC, h_ACO, h_ABO) # минимальное расстояние от О до сторон АВС
            print('Минимальное расстояние от точки до сторон треугольника = {:.5g}'.format(r))
    else:
        print('Точка не принадлежит треугольнику')
