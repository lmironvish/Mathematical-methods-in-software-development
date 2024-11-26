import first
import second
import third
import fourth
import random
import math

# Задание 1
n = int(input("Введите число n: "))
print(f"Факториал {n}! = {first.factorial(n)}")


# Задание 2

print("Исходный массив A:", second.A)
# Заполняем массив значениями функции F(i)
print("Значения функции F(i):", second.F_values)
print("Результат расчета:", second.result)

# Вариант 12 из таблицы 2
# Находим минимальный и максимальный элементы
filtered_result = [x for x in second.result]
if filtered_result:
    min_value = min(filtered_result)
    max_value = max(filtered_result)
    division_result = min_value / max_value
    print(f"Найти частное от деления минимального элемента на максимальный элемент: {division_result}")
else:
    print("В массиве нет значений для вычисления.")


# Вывод в файл

with open("output.txt", "w") as file:
    file.write("Исходный массив A: " + str(second.A) + "\n")
    file.write(f"частное от деления минимального элемента на максимальный элемент: {division_result}\n")

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


# Задание 3


# Размерность матрицы
n = int(input("Введите число n: "))

# Создаем матрицу и заполняем её случайными значениями
matrix = third.create_matrix(n)

# Выводим матрицу
print("Созданная матрица:")
for row in matrix:
    print(row)

# Находим сумму элементов в заштрихованной части матрицы
shaded_sum = third.sum_shaded_elements(matrix)
print(f"Сумма элементов в заштрихованной части матрицы: {shaded_sum}")


# Задание 4
print(f"Массив A: {fourth.a}")
print(f"Целые числа из интервала ({fourth.m}, {fourth.M}), которые не входят в последовательность a1, ..., a30: {fourth.missing_numbers}")
