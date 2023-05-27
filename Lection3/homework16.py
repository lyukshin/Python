# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

def Task_1():
    list_cur = list()
    count = 0
    n = int(input('введите количество элементов в массиве N:\n '))

    for i in range(n):
        list_cur.append(random.randint(1, n))
    print(f"\t{list_cur}")

    x = int(input('введите число X:\n\t'))

    for i in range(n):
        if list_cur[i] == x:
            count += 1
    print(f"\t-> {count}")

Task_1()