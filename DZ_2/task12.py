# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

S = int(input('Введите сумму задуманных чисел: '))
P = int(input('Введите произведение задуманных чисел: '))
while S < 0 or P < 0 or P > 10**6:
    print('Введите целые положительные числа не более 1000000.')
    S = int(input('Введите сумму задуманных чисел: '))
    P = int(input('Введите произведение задуманных чисел: '))
if P == 0:
    print(f'Задуманные числа: {S} и {P}')
elif P % 5 == 0:
    X = P // 5
    Y = P // X
else:
    X = (P + S) // S
    Y = P // X
print(f'Задуманные числа: {X} и {Y}')
