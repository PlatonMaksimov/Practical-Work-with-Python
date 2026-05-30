# Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол". От этого
# класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
# связанные с социальным положением (например, "семейное положение",
# "количество детей" и т.д.).

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")


class Man(Person):
    def __init__(self, name, age, marital_status, has_children=False, children_count=0):
        super().__init__(name, age, "Мужской")
        self.marital_status = marital_status  # "женат", "холост", "разведён"
        self.has_children = has_children
        self.children_count = children_count

    def display_info(self):
        super().display_info()
        print(f"  Семейное положение: {self.marital_status}")
        if self.has_children:
            print(f"  Детей: {self.children_count}")
        else:
            print("  Детей: нет")


class Woman(Person):
    def __init__(self, name, age, marital_status, has_children=False, children_count=0, maiden_name=None):
        super().__init__(name, age, "Женский")
        self.marital_status = marital_status  # "замужем", "не замужем", "разведена"
        self.has_children = has_children
        self.children_count = children_count
        self.maiden_name = maiden_name  # девичья фамилия (доп. свойство)

    def display_info(self):
        super().display_info()
        print(f"  Семейное положение: {self.marital_status}")
        if self.has_children:
            print(f"  Детей: {self.children_count}")
        else:
            print("  Детей: нет")
        if self.maiden_name:
            print(f"  Девичья фамилия: {self.maiden_name}")


# Тестовые запуски
print("\n=== Задача 2: Человек, Мужчина, Женщина ===")

person = Person("Алексей", 30, "Мужской")
person.display_info()

print()
man = Man("Дмитрий", 35, "женат", has_children=True, children_count=2)
man.display_info()

print()
woman = Woman("Елена", 28, "замужем", has_children=True, children_count=1, maiden_name="Иванова")
woman.display_info()

print()
woman2 = Woman("Мария", 22, "не замужем")
woman2.display_info()