# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120


def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Чтение вводных данных
n = int(input("Введите число n: "))

factorial_value = factorial(n)
print(f"Факториал числа {n} равен {factorial_value}.")
