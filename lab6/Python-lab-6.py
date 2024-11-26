def factorial(n):
    if n < 0:
        return "Факториал не определен для отрицательных чисел"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Задание 1
n = int(input("Введите число n: "))
print(f"Факториал {n}! = {factorial(n)}")

import random
import math

# Задание 2
# Создаем массив A размерностью 10
A = [random.uniform(1, 10) for _ in range(10)]
print("Исходный массив A:", A)


# Вариант 12, данные из таблицы 1
# Определяем функции F1, F2 и F3
def F1(x):
    return 2 * x * math.e ** (-x)


def F2(x):
    return math.cos(2 * x)


def F3(x):
    return x ** 2 - math.cos(x)


# Вариант 2, данные из таблицы 1
# Определяем функции F1, F2 и F3
# def F1(x):
#     return 4 * x + 2
#
#
# def F2(x):
#     return 5 / (x + 0.4)
#
#
# def F3(x):
#     return 0.5 / (2 * math.sin(4 * x))


# Определяем функцию F(x)
def F(x):
    if x <= 3:
        return F1(x)
    elif 3 < x <= 6:
        return F2(x)
    elif 6 < x <= 10:
        return F3(x)


# Заполняем массив значениями функции F(i)
F_values = [F(x) for x in A]
print("Значения функции F(i):", F_values)

# Проверяем селективную обработку
result = []
for i in range(0, 10):
    result.append(F_values[i])

print("Результат расчета:", result)

# Вариант 12 из таблицы 2
# Находим минимальный и максимальный элементы
filtered_result = [x for x in result]
if filtered_result:
    min_value = min(filtered_result)
    max_value = max(filtered_result)
    division_result = min_value / max_value
    print(f"Найти частное от деления минимального элемента на максимальный элемент: {division_result}")
else:
    print("В массиве нет значений для вычисления.")

# Вариант 2, из таблицы 2
#
# # Фильтруем элементы, удовлетворяющие условию 5 <= A_i <= 15
# filtered_elements = [x for x in result if 5 <= x <= 15]
#
# # Проверяем, есть ли элементы, удовлетворяющие условию
# if filtered_elements:
#     # Вычисляем среднее арифметическое
#     average = sum(filtered_elements) / len(filtered_elements)
#     print(f"Среднее арифметическое элементов, удовлетворяющих условию 5 <= A_i <= 15: {average}")
# else:
#     print("Нет элементов, удовлетворяющих условию.")
