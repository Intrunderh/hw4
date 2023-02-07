n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))

print()

pervoe = []
for i in range(n):
    chisla = int(input('Введите числа первого множества: '))
    pervoe.append(chisla)

print()

vtoroe = []
for i in range(m):
    chisla = int(input('Введите числа второго множества: '))
    vtoroe.append(chisla)
    
print()

print(f'Введенные числа первого множества: {pervoe}')
print(f'Введенные числа второго множества: {vtoroe}')

print()

chislas = list(set(pervoe) & set(vtoroe))
chislas.sort()
print(f'Числа, встречающиеся в обоих наборах: {chisla}')






'''
n = int(input('Введите количество элементов первого множества: '))
temp_1 = []
for i in range(n):
    chisla = int(input('Введите числа: '))
    temp_1.append(chisla)
print(f'Введенные числа первого множества: {temp_1}')

m = int(input('Введите количество элементов второго множества: '))
temp_2 = []
for i in range(m):
    chisla = int(input('Введите числа: '))
    temp_2.append(chisla)
print(f'Введенные числа второго множества: {temp_2}')

seen = set( for x in a)
print(*seen)

# a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
# seen = set(x for x in a)
# print(*seen)

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
pervoe = []
for i in range(n):
    chisla = int(input('Введите числа первого множества: '))
    pervoe.append(chisla)
vtoroe = []
for i in range(m):
    chisla = int(input('Введите числа второго множества: '))
    vtoroe.append(chisla)

seen_1 = set(x for x in pervoe)
seen_2 = set(x for x in vtoroe)

print(*seen_1)
print(*seen_2)


def merge_lists(lst1, lst2):
    for i in lst2:
        if i not in lst1:
            lst1.append(i)
    return lst1
'''