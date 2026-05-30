
import sqlite3


#СОЗДАНИЕ БД И ТАБЛИЦЫ
def create_db():
    conn = sqlite3.connect('warehouse.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Товары (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Код_товара TEXT UNIQUE,
            Торговая_марка TEXT,
            Тип TEXT,
            Цена REAL,
            Количество_на_складе INTEGER,
            Минимальный_запас INTEGER
        )
    ''')
    conn.commit()
    conn.close()


#ВВОД 10 ЗАПИСЕЙ
def add_records():
    conn = sqlite3.connect('warehouse.db')
    cur = conn.cursor()

    # Если в таблице уже есть записи, спросим
    cur.execute("SELECT COUNT(*) FROM Товары")
    count = cur.fetchone()[0]
    if count >= 10:
        print("В таблице уже есть 10 или более записей. Добавление отменено.")
        conn.close()
        return

    print("\n--- Добавление 10 товаров ---")
    for i in range(10):
        print(f"\nТовар {i + 1}:")
        code = input("  Код товара: ")
        brand = input("  Торговая марка: ")
        ptype = input("  Тип: ")
        price = float(input("  Цена: "))
        quantity = int(input("  Количество на складе: "))
        min_stock = int(input("  Минимальный запас: "))

        try:
            cur.execute('''
                INSERT INTO Товары (Код_товара, Торговая_марка, Тип, Цена, Количество_на_складе, Минимальный_запас)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (code, brand, ptype, price, quantity, min_stock))
            conn.commit()
            print("  ✓ Добавлено")
        except sqlite3.IntegrityError:
            print("  Ошибка: товар с таким кодом уже существует!")

    conn.close()
    print("\nДобавление завершено.")


#ПОИСК (3 варианта)
def search():
    conn = sqlite3.connect('warehouse.db')
    cur = conn.cursor()

    print("\n--- ПОИСК ТОВАРОВ ---")
    print("1. Поиск по коду товара (точное совпадение)")
    print("2. Поиск по торговой марке (частичное совпадение)")
    print("3. Поиск товаров с количеством меньше минимального запаса")
    choice = input("Выберите вариант поиска (1-3): ")

    if choice == '1':
        code = input("Введите код товара: ")
        cur.execute("SELECT * FROM Товары WHERE Код_товара = ?", (code,))
        results = cur.fetchall()
        if results:
            print("\nРезультаты поиска:")
            for row in results:
                print(row)
        else:
            print("Товар не найден.")

    elif choice == '2':
        brand = input("Введите часть названия торговой марки: ")
        cur.execute("SELECT * FROM Товары WHERE Торговая_марка LIKE ?", (f'%{brand}%',))
        results = cur.fetchall()
        if results:
            print(f"\nНайдено {len(results)} товаров:")
            for row in results:
                print(row)
        else:
            print("Ничего не найдено.")

    elif choice == '3':
        cur.execute("SELECT * FROM Товары WHERE Количество_на_складе < Минимальный_запас")
        results = cur.fetchall()
        if results:
            print(f"\nТовары с дефицитом ({len(results)} шт.):")
            for row in results:
                print(row)
        else:
            print("Все товары в достаточном количестве.")

    else:
        print("Неверный выбор.")

    conn.close()


#УДАЛЕНИЕ (3 варианта)
def delete():
    conn = sqlite3.connect('warehouse.db')
    cur = conn.cursor()

    print("\n--- УДАЛЕНИЕ ТОВАРОВ ---")
    print("1. Удалить по коду товара")
    print("2. Удалить все товары заданной торговой марки")
    print("3. Удалить товары с нулевым количеством на складе")
    choice = input("Выберите вариант удаления (1-3): ")

    if choice == '1':
        code = input("Введите код товара для удаления: ")
        cur.execute("DELETE FROM Товары WHERE Код_товара = ?", (code,))
        conn.commit()
        print(f"Удалено записей: {cur.rowcount}")

    elif choice == '2':
        brand = input("Введите торговую марку для удаления: ")
        cur.execute("DELETE FROM Товары WHERE Торговая_марка = ?", (brand,))
        conn.commit()
        print(f"Удалено записей: {cur.rowcount}")

    elif choice == '3':
        cur.execute("DELETE FROM Товары WHERE Количество_на_складе = 0")
        conn.commit()
        print(f"Удалено записей: {cur.rowcount}")

    else:
        print("Неверный выбор.")

    conn.close()


#РЕДАКТИРОВАНИЕ (3 варианта)
def edit():
    conn = sqlite3.connect('warehouse.db')
    cur = conn.cursor()

    print("\n--- РЕДАКТИРОВАНИЕ ТОВАРОВ ---")
    print("1. Изменить цену товара по коду")
    print("2. Изменить количество на складе по торговой марке")
    print("3. Увеличить цену на 10% для товаров с остатком меньше минимального")
    choice = input("Выберите вариант редактирования (1-3): ")

    if choice == '1':
        code = input("Введите код товара: ")
        new_price = float(input("Новая цена: "))
        cur.execute("UPDATE Товары SET Цена = ? WHERE Код_товара = ?", (new_price, code))
        conn.commit()
        print(f"Обновлено записей: {cur.rowcount}")

    elif choice == '2':
        brand = input("Введите торговую марку: ")
        new_qty = int(input("Новое количество на складе: "))
        cur.execute("UPDATE Товары SET Количество_на_складе = ? WHERE Торговая_марка = ?", (new_qty, brand))
        conn.commit()
        print(f"Обновлено записей: {cur.rowcount}")

    elif choice == '3':
        cur.execute("UPDATE Товары SET Цена = Цена * 1.1 WHERE Количество_на_складе < Минимальный_запас")
        conn.commit()
        print(f"Обновлено записей: {cur.rowcount}")

    else:
        print("Неверный выбор.")

    conn.close()


#ПРОСМОТР ВСЕХ ЗАПИСЕЙ
def view_all():
    conn = sqlite3.connect('warehouse.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товары")
    rows = cur.fetchall()

    if rows:
        print("\n--- ВСЕ ТОВАРЫ ---")
        for row in rows:
            print(row)
    else:
        print("Таблица пуста.")
    conn.close()


#ГЛАВНОЕ МЕНЮ
def main():
    create_db()

    while True:
        print("\n" + "=" * 50)
        print("        ТОВАРНЫЙ ЗАПАС - Главное меню")
        print("=" * 50)
        print("1. Добавить 10 товаров")
        print("2. Поиск товаров (3 варианта)")
        print("3. Удаление товаров (3 варианта)")
        print("4. Редактирование товаров (3 варианта)")
        print("5. Показать все товары")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            add_records()
        elif choice == '2':
            search()
        elif choice == '3':
            delete()
        elif choice == '4':
            edit()
        elif choice == '5':
            view_all()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()