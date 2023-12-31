# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input("Введите количество монеток, лежащих на столе: "))
x = n + 1
r = random.randint(0, x)
g = n - r
if r > g:
    min = g
else:
    min = r
print(f"Минимальное количество монет, которые необходимо перевернуть: {min}")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random
x = random.randint(1, 1001)
y = random.randint(1, 1001)
print(f"Сумма этих чисел: {x + y}")
print(f"Произведение этих чисел: {x * y}")
S = x + y
P = x * y
D = S**2 - 4 * P
if D > 0:
    a1 = (-(-S) + D**(1 / 2)) / (2 * 1)
    a2 = (-(-S) - D**(1 / 2)) / (2 * 1)
    if a1 > 0:
        b1 = S - a1
        print(f"Петя загадал эти числа: {a1}, {b1}")
    elif a2 > 0:
        b2 = S - a2
        print(f"Петя загадал эти числа: {a2}, {b2}")
elif D == 0:
    a = -(-S) / (2 * 1)
    if a > 0:
        b = S - a
        print(f"Петя загадал эти числа: {a}, {b}")
else:
    print("Не удаётся отгадать числа(")


#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

N = int(input("Введите число N: "))
a = 1
print(a)
while a < N:
    a = a * 2
    print(a)