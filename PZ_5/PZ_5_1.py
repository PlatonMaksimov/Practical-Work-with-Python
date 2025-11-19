# Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные.

def calc_sum():
    """Вычисляет сумму чисел ряда от 1 до 60."""
    total = 0
    number = 1
    end_number = 60

    while number <= end_number:
        total += number
        number += 1

    return total


def main():
    try:
        result = calc_sum()
        print(f"Сумма чисел от 1 до 60: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

main()