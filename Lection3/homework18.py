# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

def Task_2():
    list_cur = list()
    n = int(input('введите количество элементов в массиве N:\n '))

    for i in range(n):
        list_cur.append(random.randint(1, n))
    print(f"\t{list_cur}")

    x = int(input('введите число X:\n\t'))

    min = 100
    for i in range(n):
        min_cur = abs(x - list_cur[i])
        max_cur = abs(list_cur[i] - x)

        if max_cur <= min:
            min = max_cur
            count = list_cur[i]
        elif min_cur <= min:
            min = min_cur
            count = list_cur[i]

    print(f"\t-> {count}")

Task_2()