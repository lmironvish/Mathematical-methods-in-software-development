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