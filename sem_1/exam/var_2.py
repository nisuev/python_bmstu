def to_roman(num):
    one = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    ten = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundred = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thouthand = ['', 'M', 'MM', 'MMM']

    one_num = one[num % 10]
    ten_num = ten[num // 10 % 10]
    hundred_num = hundred[num // 100 % 10]
    thouthands_num = thouthand[num // 1000]

    roman_num = thouthands_num + hundred_num + ten_num + one_num
    return roman_num

file = 'in1.txt'
file_new = 'out1.txt'
f = open(file, encoding='utf-8')
max_len = -1
for i in f:
    len_roman = len(to_roman(int(i)))
    if len_roman > max_len:
        max_len = len_roman

f.seek(0)
fn = open(file_new, 'w',  encoding='utf-8')
for i in f:
    fn.write(f'{to_roman(int(i)):^{max_len}}')
    fn.write('\n')

f.close()
fn.close()

file = 'out1.txt'
file_num = 'in2.txt'
file_new = 'out2.txt'

f = open(file, encoding='utf-8')
f_num = open(file_num, encoding='utf-8')
f_new = open(file_new, 'w',  encoding='utf-8')

for num in f_num:
    num_str = 0
    while int(num.strip()) != num_str:
        roman_num = f.readline().rstrip()
        num_str += 1
    f.seek(0)
    f_new.write(roman_num)
    f_new.write('\n')

f.close()
f_num.close()
f_new.close()