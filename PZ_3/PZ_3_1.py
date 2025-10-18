#Вариант №13
#Даны три целых числа: A, B, C. Проверить истинность
#высказывания: «Хотя бы одно из чисел A, B, C положительное»

a, b, c = input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите первое число: ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели!')
        b = input('Введите второе число: ')

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Неправильно ввели!')
        c = input('Введите третье число: ')

if a > 0 or b > 0 or c > 0:
    print('Хотя бы одно число положительно')
else:
    print('Не одно число не является положительным')