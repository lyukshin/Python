# Задача 2: Найдите сумму цифр трехзначного числа.

# Результаты:
# 123 -> 6 (1 + 2 + 3) 
# 100 -> 1 (1 + 0 + 0)



def sum_of_digits(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum

# Чтение вводного числа
number = int(input("Введите трехзначное число: "))

digit_sum = sum_of_digits(number)
print(f"Сумма цифр числа {number} равна {digit_sum}.")