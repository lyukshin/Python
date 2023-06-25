# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# Результаты:
# 6 -> 1 4 1
# 24 -> 4 16 4 
# 60 -> 10 40 10


def count_cranes(total_cranes):
    katya = total_cranes // 4
    petya_sereja = katya // 3
    return petya_sereja, katya, petya_sereja

# Чтение вводных данных
total_cranes = int(input("Введите общее количество журавликов: "))

petya_count, katya_count, sereja_count = count_cranes(total_cranes)
print(f"Петя: {petya_count}, Катя: {katya_count}, Сережа: {sereja_count}.")
