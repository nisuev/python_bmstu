def to_hex(num):
    num_parts = num.split('.')
    hex_num = ''
    sign = ''
    if num_parts[0][0] == '-':
        sign = '-'
        num_parts[0] = num_parts[0][1:]

    n = 2
    for i in range(n):
        if i % 2 == 0:
            int_part = int(num_parts[i], 8)
            hex_num += hex(int_part)[2:] + '.'
        if i % 2 != 0:
            bin_part = ''
            for j in range(len(num_parts[i])):
                bin_el = bin(int(num_parts[i][j]))[2:]
                if len(bin_el) != 3:
                    bin_el = '0' * (3 - (len(bin_el) % 3)) + bin_el
                bin_part += bin_el
            if len(bin_part) % 4 != 0:
                bin_part = bin_part + '0' * (4 - (len(bin_part) % 4))
            hex_del = ''
            for j in range(0, len(bin_part), 4):
                int_el = int(bin_part[j:j + 4], 2)
                hex_el = hex(int_el)[2:]
                hex_del += hex_el
            hex_num += hex_del

    hex_num = sign + hex_num
    return hex_num


file = 'in.txt'
file_new = 'out1.txt'
f = open(file, 'r', encoding='utf-8')
fn = open(file_new, 'w', encoding='utf-8')
n = 0
for i in f:
    hex_num = to_hex(i.rstrip())
    fn.write(hex_num)
    fn.write('\n')
    n += 1
f.close()
fn.close()

file = 'out1.txt'
file_new = 'out2.txt'
f = open(file, 'r', encoding='utf-8')
fn = open(file_new, 'w', encoding='utf-8')

ind_last = []
last_ln = -1
for i in range(n):
    min_len = float('+inf')
    min_num = ''
    ind = -1
    cnt = 0
    for j in f:
        num = j.strip()
        if len(num) < min_len:
            if cnt not in ind_last:
                min_num = num
                min_len = len(num)
                ind = cnt

        cnt += 1
    fn.write(min_num)
    fn.write('\n')
    if len(j) == last_ln:
        ind_last.append(ind)
        last_ln = len(j)
    else:
        ind_last = []
        ind_last.append(ind)
        last_ln = len(j)

    f.seek(0)

f.close()
fn.close()