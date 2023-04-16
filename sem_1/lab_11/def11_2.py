#вставки с бинарным поиском
def insertbin(lst,n):
    for i in range(1,n):
        var = lst[i]
        low = 0
        high = i

        while low < high:
            mid = (low + high) // 2
            if var < lst[mid]:
                high = mid
            else:
                low = mid + 1
        j = i
        while j > low and j > 0:
            lst[i] = lst[j - 1]
            j = j - 1
        lst[low] = var
    return lst
            

n = int(input('Введите длину массива: '))
lst = [0] * n
for i in range(n):
    lst[i] = float(input(f'Введите {i + 1} элемент массива: '))

print()
insertbin(lst, n)
print('отсортированный список: ')
for i in range(n):
    print(f'{i + 1} элемент: {lst[i]:.5g}')
