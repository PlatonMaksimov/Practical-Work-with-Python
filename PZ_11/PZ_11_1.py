# 1.Проверить есть ли в последовательности целых N чисел число K.

numbers = [3, 7, 12, -5, 8, 10, 21, -2, 9, 4]
K = 10

contains = any(lambda x: x == K, numbers)

print(f"Последовательность: {numbers}")
print(f"Число {K} {'присутствует' if contains else 'отсутствует'}")