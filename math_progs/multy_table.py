n = int(input('Введите размер таблицы: '))
column_mult = [i for i in range(n+1)]
string_mult = [i for i in range(n+1)]
max_fact = len(str(max(column_mult)))
n += 1

mult_matrix = []
max_mult_digit = 0
for i in range(n):
    mult_matrix.append([])
    for j in range(n):
        mult = column_mult[i] * string_mult[j]
        mult_matrix[i].append(mult)
        max_mult_digit = max(max_mult_digit, len(str(mult)))

for i in range(n + 1):
    if i == 0:
        print(' ' * max_fact, '|', sep='', end='')
        continue
    print(f'{string_mult[i - 1]:>{max_mult_digit + 1}}', end='')
print()
print('-' * ((max_mult_digit + 1) * n + (max_fact + 1)))

for i in range(n):
    print(f'{column_mult[i]:>{max_fact}}|', end='')
    for j in range(n):
        print(f'{mult_matrix[i][j]:>{max_mult_digit + 1}}', end='')
    print()
