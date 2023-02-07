n = int(input( 'Введите количество кустов: ' ))
lis = [int(x) for x in input('Введите числа через пробел: ').split()]
n = len(lis)
lis = lis + lis[:2]
ma = 0
for i in range(n):
    ma = max(ma, lis[i] + lis[i+1] + lis[i+2])
print(f'Максимальное число ягод, которое может собрать за один заход собирающий модуль = {ma}')