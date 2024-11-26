import random

# Функция для создания и заполнения квадратной матрицы случайными значениями
def create_matrix(n):
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]


# Функция для нахождения суммы элементов в заштрихованной части матрицы
def sum_shaded_elements(matrix):
    n = len(matrix)
    total_sum = 0

    for i in range(n):
        for j in range(n):
            if i != j and abs(i - j) == 1:  # Элементы на диагоналях, параллельных главной, но не на главной
                total_sum += matrix[i][j]

    return total_sum

