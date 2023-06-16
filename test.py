def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Пример использования функции
n = int(input("Введите число: "))

factorial_value = factorial(n)
print(f"Факториал числа {n} равен {factorial_value}.")