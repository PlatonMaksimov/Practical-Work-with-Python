# 2. В матрице найти максимальный положительный элемент, кратный 4.

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

#Поиск максимального положительного элемента, кратного 4
max_elem = None
for row in matrix:
    for x in row:
        if x > 0 and x % 4 == 0:
            if max_elem is None or x > max_elem:
                max_elem = x

print("\nРезультат:")
if max_elem is not None:
    print(f"Максимальный положительный элемент, кратный 4: {max_elem}")
else:
    print("Таких элементов нет.")