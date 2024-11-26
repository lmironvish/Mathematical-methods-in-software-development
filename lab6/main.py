import first
import second
import third
import fourth

print('Задание 1')
n = int(input("Введите число n: "))
print(f"Факториал {n}! = {first.factorial(n)}")

print('Задание 2')
print("Исходный массив A:", second.A)
# Заполняем массив значениями функции F(i)
print("Значения функции F(i):", second.F_values)
print("Результат расчета:", second.result)

# Вариант 12 из таблицы 2
# Находим минимальный и максимальный элементы
division_result = second.division_result()

# Вывод в файл
with open("output.txt", "w") as file:
    file.write("Исходный массив A: " + str(second.A) + "\n")
    file.write(f"частное от деления минимального элемента на максимальный элемент: {division_result}\n")


print('Задание 3')
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
print('Задание 4')
m = int(input("Введите наименьшее целое число m: "))
M = int(input("Введите наибольшее целое число M: "))
print(f"Массив A: {fourth.a}")
print(f"Целые числа из интервала ({m}, {M}), которые не входят в последовательность a1, ..., a30: {fourth.missing_numbers(m, M)}")
