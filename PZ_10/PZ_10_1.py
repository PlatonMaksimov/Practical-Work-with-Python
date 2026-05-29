# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Квадраты четных элементов:
# Сумма квадратов четных элементов:
# Среднее арифметическое суммы квадратов четных элементов:

import random

nums = [random.randint(-30, 50) for _ in range(12)]
with open('numbers.txt', 'w') as f:
    f.write(' '.join(map(str, nums)))

with open('numbers.txt', 'r') as f:
    data = list(map(int, f.read().split()))

min_elem = min(data)
even_squares = [x**2 for x in data if x % 2 == 0]
sum_squares = sum(even_squares)
avg_squares = sum_squares / len(even_squares) if even_squares else 0

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f"Исходные данные:\n{' '.join(map(str, data))}\n")
    f.write(f"Количество элементов: {len(data)}\n")
    f.write(f"Минимальный элемент: {min_elem}\n")
    f.write(f"Квадраты четных элементов: {' '.join(map(str, even_squares))}\n")
    f.write(f"Сумма квадратов четных элементов: {sum_squares}\n")
    f.write(f"Среднее арифметическое суммы квадратов четных элементов: {avg_squares}\n")

print("Готово! Файлы: numbers.txt, result.txt")