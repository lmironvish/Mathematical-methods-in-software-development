import random

a = list(int(random.uniform(1, 31)) for _ in range(100))  # Пример последовательности от 1 до 30

def missing_numbers(start, end):
    # Определяем последовательность a1, ..., a30
    missing_numbers_array = [x for x in range(start + 1, end + 1) if x not in a]

    return missing_numbers_array
