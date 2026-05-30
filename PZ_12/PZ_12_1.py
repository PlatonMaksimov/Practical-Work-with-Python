# 1. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.

import random

#Ввод размеров
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

#Генерация матрицы
matrix = [[random.randint(-20, 50) for _ in range(cols)] for _ in range(rows)]

#Вывод исходной матрицы
print("\nИсходная матрица:")
for row in matrix:
    print(row)

#Обработка строки с нечетным номером
print("\nСреднее арифметическое для строк с нечетным номером (1, 3, 5...):")
for i in range(rows):
    if i % 2 == 0:
        avg = sum(matrix[i]) / cols
        print(f"Строка {i+1}: {avg:.2f}")