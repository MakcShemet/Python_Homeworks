# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint

N = int(input('Введите натуральное число (размер массива): '))
my_list = [randint(1, 9) for i in range(N)]
print(*my_list)
X = int(input('Введите искомое число: '))
print(f'Количество раз, которое искомое вами число встречается в массиве равно: {my_list.count(X)}')