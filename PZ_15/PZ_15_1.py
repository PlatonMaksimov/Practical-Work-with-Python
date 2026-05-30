
import sqlite3
from data_products import products_data


class WarehouseDB:
    def __init__(self, db_name='warehouse.db'):
        self.db_name = db_name
        self.create_table()
        self.load_data()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.get_connection() as conn:
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

    def load_data(self):
        """Загружает готовые данные из файла, если таблица пуста"""
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM Товары")
            if cur.fetchone()[0] == 0:
                cur.executemany('''
                    INSERT INTO Товары (Код_товара, Торговая_марка, Тип, Цена, Количество_на_складе, Минимальный_запас)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', products_data)
                print(f"Загружено {len(products_data)} записей из data_products.py")

    #ПОИСК (3 варианта)
    def search_by_code(self, code):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Товары WHERE Код_товара = ?", (code,))
            return cur.fetchall()

    def search_by_brand(self, brand_part):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Товары WHERE Торговая_марка LIKE ?", (f'%{brand_part}%',))
            return cur.fetchall()

    def search_out_of_stock(self):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Товары WHERE Количество_на_складе < Минимальный_запас")
            return cur.fetchall()

    #УДАЛЕНИЕ (3 варианта)
    def delete_by_code(self, code):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM Товары WHERE Код_товара = ?", (code,))
            return cur.rowcount

    def delete_by_brand(self, brand):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM Товары WHERE Торговая_марка = ?", (brand,))
            return cur.rowcount

    def delete_zero_quantity(self):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM Товары WHERE Количество_на_складе = 0")
            return cur.rowcount

    #РЕДАКТИРОВАНИЕ (3 варианта)
    def update_price(self, code, new_price):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("UPDATE Товары SET Цена = ? WHERE Код_товара = ?", (new_price, code))
            return cur.rowcount

    def update_quantity_by_brand(self, brand, new_qty):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("UPDATE Товары SET Количество_на_складе = ? WHERE Торговая_марка = ?", (new_qty, brand))
            return cur.rowcount

    def increase_price_for_deficit(self, percent=10):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                f"UPDATE Товары SET Цена = Цена * {1 + percent / 100} WHERE Количество_на_складе < Минимальный_запас")
            return cur.rowcount

    #ВСЕ ЗАПИСИ
    def get_all(self):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Товары")
            return cur.fetchall()


#МЕНЮ (консольный интерфейс)
def main():
    db = WarehouseDB()

    while True:
        print("\n" + "=" * 50)
        print("        ТОВАРНЫЙ ЗАПАС - Главное меню")
        print("=" * 50)
        print("1. Показать все товары")
        print("2. Поиск товаров")
        print("3. Удаление товаров")
        print("4. Редактирование товаров")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            rows = db.get_all()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("Таблица пуста.")

        elif choice == '2':
            print("\n--- ПОИСК ---")
            print("1. По коду товара")
            print("2. По части торговой марки")
            print("3. Товары с дефицитом")
            opt = input("Выберите вариант (1-3): ")

            if opt == '1':
                code = input("Код товара: ")
                res = db.search_by_code(code)
            elif opt == '2':
                brand = input("Часть названия марки: ")
                res = db.search_by_brand(brand)
            elif opt == '3':
                res = db.search_out_of_stock()
            else:
                print("Неверный выбор")
                continue

            if res:
                for r in res:
                    print(r)
            else:
                print("Ничего не найдено.")

        elif choice == '3':
            print("\n--- УДАЛЕНИЕ ---")
            print("1. По коду товара")
            print("2. По торговой марке (все)")
            print("3. Удалить товары с нулевым остатком")
            opt = input("Выберите вариант (1-3): ")

            if opt == '1':
                code = input("Код товара: ")
                cnt = db.delete_by_code(code)
            elif opt == '2':
                brand = input("Торговая марка: ")
                cnt = db.delete_by_brand(brand)
            elif opt == '3':
                cnt = db.delete_zero_quantity()
            else:
                print("Неверный выбор")
                continue

            print(f"Удалено записей: {cnt}")

        elif choice == '4':
            print("\n--- РЕДАКТИРОВАНИЕ ---")
            print("1. Изменить цену по коду товара")
            print("2. Изменить количество на складе по торговой марке")
            print("3. Поднять цены на дефицитные товары на 10%")
            opt = input("Выберите вариант (1-3): ")

            if opt == '1':
                code = input("Код товара: ")
                new_price = float(input("Новая цена: "))
                cnt = db.update_price(code, new_price)
            elif opt == '2':
                brand = input("Торговая марка: ")
                new_qty = int(input("Новое количество: "))
                cnt = db.update_quantity_by_brand(brand, new_qty)
            elif opt == '3':
                cnt = db.increase_price_for_deficit(10)
            else:
                print("Неверный выбор")
                continue

            print(f"Обновлено записей: {cnt}")

        elif choice == '5':
            print("До свидания!")
            break

        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()