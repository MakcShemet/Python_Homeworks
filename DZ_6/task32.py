# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

myList = [num for num in range(1, 20)]
print(myList)

minimum = int(input('Введите начальное значение диапазона: '))
maximum = int(input('Введите конечное значение диапазона: '))

for i in myList:
    if i >= minimum and i <= maximum:
        print(myList.index(i), end=' ')