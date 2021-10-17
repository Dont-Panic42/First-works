def binsearch(lst, key):
    l = -1
    r = len(lst)
    while l < r - 1:
        m = (l + r) // 2
        if lst[m] < key:
            l = m
        else:
            r = m
    return r

def mysort(l):
    fl = True
    while fl:
        fl = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                fl = True
                (l[i], l[i + 1]) = (l[i + 1], l[i])


s = input('Введите последовательность чисел через пробел: ')
num = int(input('Введите число: '))
lst = list(map(float, s.split()))

mysort(lst)
print(lst)
pos = binsearch(lst, num)
print("Позиция =", pos)
