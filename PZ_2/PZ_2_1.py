#Вариант №13
#Дано двузначное число. Вывести число, полученное при перестановки цифр исходного числа. % //

def reverse_number():
    while True:
        try:
            num = input('Введите двузначное число: ')

            if not num.isdigit():
                raise ValueError('Ошибка: Введены нечисловые данные!')

            if len(num) != 2:
                raise ValueError('Ошибка: Число должно быть двузначным!')

            num_int = int(num)

            reverse_num = num[1] + num[0]

            print(f'Исходное число {num}')
            print(f'Число после перестановки цифр: {reverse_num}')

            break

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            print("Пожалуйста, попробуйте еще раз.\n")

        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
            print("Пожалуйста, попробуйте еще раз.\n")

reverse_number()