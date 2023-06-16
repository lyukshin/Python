

# Задача No1. Решение в группах
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2

import math


n = int(input("Машина проезжает за день "))
m = int(input("Длинна маршрута "))

days1 = m / n
days2 = math.ceil(days1)
print(days2)


# days = m // n + 1
days = (m + n - 1) // n
print(days)

# Решение 1
n = int(input("Введите сколько км в день: "))
m = int(input("Введите сколько км в день: "))
days = m // n + (m%n > 0)
print(days)


# Решение 2
n = int(input())
m = int(input())
s = (m + n - 1) // n
print(s)