# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('Введите разность(шаг) арифметической прогрессии: '))
n = int(input('Введите количество элементов арифметической прогрессии: '))

arithmeticProgress = [num for num in range(a, (a+(n-1)*d)+a, d)]
print(arithmeticProgress)