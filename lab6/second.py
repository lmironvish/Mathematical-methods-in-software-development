import random
import math

# Создаем массив A размерностью 10
A = [random.uniform(1, 10) for _ in range(10)]


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

# Проверяем селективную обработку
result = []
for i in range(0, 10):
    result.append(F_values[i])


# вариант 12

def division_result():
    filtered_result = [x for x in result]
    if filtered_result:
        min_value = min(filtered_result)
        max_value = max(filtered_result)
        division_result = min_value / max_value
        print(f"Найти частное от деления минимального элемента на максимальный элемент: {division_result}")
        return division_result
    else:
        print("В массиве нет значений для вычисления.")


# вариант 2
def average_of_5_and_15():
    # Фильтруем элементы, удовлетворяющие условию 5 <= A_i <= 15
    filtered_elements = [x for x in result if 5 <= x <= 15]
    # Проверяем, есть ли элементы, удовлетворяющие условию
    if filtered_elements:
        # Вычисляем среднее арифметическое
        average = sum(filtered_elements) / len(filtered_elements)
        print(f"Среднее арифметическое элементов, удовлетворяющих условию 5 <= A_i <= 15: {average}")
        return average
    else:
        print("Нет элементов, удовлетворяющих условию.")
