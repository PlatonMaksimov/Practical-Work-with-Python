# Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
# память". Напишите метод, который выводит информацию о компьютере в формате
# "Марка: марка, Процессор: процессор, Оперативная память: память".

class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def display_info(self):
        print(f"Марка: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram}")


# Тестовые запуски
print("Компьютеры:")
pc1 = Computer("DEXP", "Intel Core i5-13400F", "16GB DDR4")
pc2 = Computer("MSI", "AMD Ryzen 7 5800X", "32GB DDR4")
pc3 = Computer("Apple", "M2 Pro", "16GB")

pc1.display_info()
pc2.display_info()
pc3.display_info()