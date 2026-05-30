# 1. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.

matrix = [
    [3, 8, 1],
    [5, -2, 7],
    [0, 4, 6],
    [9, -1, 2],
    [7, 3, -4]
]

print("Исходная матрица:")
list(map(print, matrix))

#Cтроки с нечётным номером
odd_rows = matrix[::2]  # срез

#Среднее арифметическое через map + lambda
averages = list(map(lambda row: sum(row) / len(row), odd_rows))

print("\nСреднее арифметическое для строк с нечетным номером (1,3,5...):")
list(map(lambda avg, i: print(f"Строка {i*2+1}: {avg:.2f}"), averages, range(len(averages))))