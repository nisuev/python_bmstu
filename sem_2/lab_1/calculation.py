# Логическая часть калькулятора троичной с/с
# Троично симметричное число вида (i01)

# Функция выравнивая чисел по разрядам
def num_align(n1, n2):
    if '.' in n2 or '.' in n1:
        if '.' in n1 and '.' in n2:
            n1, n2 = alig_float(n1, n2)
        elif '.' in n1:
            n2.append('.')
            n1, n2 = alig_float(n1, n2)
        else:
            n1.append('.')
            n1, n2 = alig_float(n1, n2)
    else:
        n1, n2 = alig_int(n1, n2)

    return n1, n2


# Выравнивание чисел с плавающей точкой
def alig_float(n1: list[str], n2: list[str]) -> list[str]:
    # Выравнивание целой части
    if n1.index('.') > n2.index('.'):
        n2 = ['0'] * (n1.index('.') - n2.index('.')) + n2
    else:
        n1 = ['0'] * (n2.index('.') - n1.index('.')) + n1

    # Выравнивание дробной части
    if len(n1[n1.index('.'):]) > len(n2[n2.index('.'):]):
        n2 = n2 + ['0'] * (len(n1[n1.index('.'):]) - len(n2[n2.index('.'):]))
    else:
        n1 = n1 + ['0'] * (len(n2[n2.index('.'):]) - len(n1[n1.index('.'):]))

    return n1, n2


# Выравнивание чисел с целой частью
def alig_int(n1: list[str], n2: list[str]) -> list[str]:
    if len(n1) < len(n2):
        n1 = ['0'] * (len(n2) - len(n1)) + n1
    else:
        n2 = ['0'] * (len(n1) - len(n2)) + n2

    return n1, n2


# Функция сложения
def trial_sum(num_1: str, num_2: str) -> str:
    num_1 = list(num_1)
    num_2 = list(num_2)
    # Выравнивание чисел
    num_1, num_2 = num_align(num_1, num_2)

    # Создание массива остатков и массива ответа
    num_ost = ['0'] * (len(num_1) + 1)
    if num_1.count('.'):
        num_ost[num_1.index('.') + 1] = '.'
    num_ans = num_ost

    # Словари сопастовления
    trial_to_dec = {'0': 0, '1': 1, 'i': -1, '1i': 2, 'i1': -2}
    dec_to_trial = {0: '0', 1: '1', -1: 'i', 2: '1i', -2: 'i1', 3: '10', -3: 'i0'}

    # Алгоритм сложения
    for i in range(-1, -(len(num_1) + 1), -1):
        if num_ans[i] == '.':
            continue
        # Сумма значений i разряда
        dig = dec_to_trial[trial_to_dec[num_1[i]] + trial_to_dec[num_2[i]] + trial_to_dec[num_ans[i]]]
        # Поиск остатка
        if len(dig) == 2:
            if num_ost[i - 1] != '.': num_ost[i - 1] = dig[0]
            else: num_ost[i - 2] = dig[0]
            dig = dig[1]
        num_ans[i] = dig  # Присваивание значения разряда
    if num_ost[0] != '0': num_ans[0] = num_ost[0]  # Присваивание последнего остатка
    else: num_ans = num_ans[1::]

    # Возвращение полученного значения
    if num_ans.count('i') == 0 and num_ans.count('1') == 0:
        return '0'

    # Алгоритм сокращения ненужных нулей
    ans = ''.join(num_ans)
    shift = 0
    for i in range(len(ans)):
        if ans[i] != '0' or (ans[i] == '0' and ans[i + 1] == '.'):
            break
        else:
            shift += 1
    ans = ans[shift:]
    ans_parts = ans.split('.')
    if ans_parts[-1].count('1') == ans_parts[-1].count('i') == 0:
        ans = ans_parts[0]
    else:
        if len(ans_parts) == 2:
            while ans_parts[-1][-1] == '0':
                ans_parts[-1] = ans_parts[-1][:-1]
            ans = '.'.join(ans_parts)
    return ans


# Функция вычитания
def trial_sub(num_1: str, num_2: str) -> str:
    num_2 = num_2.replace('1', 'l').replace('i', '1').replace('l', 'i')  # Реверс второго оператора выражения
    return trial_sum(num_1, num_2)
