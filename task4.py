class Dog:
    # Атрибути класу
    mammal = True        # собака є ссавцем
    nature = "unknown"   # характер (визначається у підкласах)
    breed = "unknown"    # порода (визначається у підкласах)

    def __init__(self, name, age):
        # Атрибути екземпляра
        self.name = name  # кличка собаки
        self.age = age    # вік собаки

    def show_info(self):
        # Виводить інформацію про конкретну собаку
        print(f"Ім'я: {self.name}, Вік: {self.age} років")

    def bark(self):
        # Загальна поведінка собаки
        print(f"{self.name} гавкає!")

# Порода Лабрадор
class Labrador(Dog):
    nature = "добрий"
    breed = "Лабрадор"

    def swim(self):
        print(f"{self.name} любить плавати!")

# Порода Вівчарка
class Shepherd(Dog):
    nature = "охоронний"
    breed = "Вівчарка"

    def guard(self):
        print(f"{self.name} охороняє дім!")

# Порода Бульдог
class Bulldog(Dog):
    nature = "спокійний"
    breed = "Бульдог"

    def rest(self):
        print(f"{self.name} любить відпочивати.")

class Pets:
    def __init__(self):
        # Список домашніх тварин
        self.pets = []

    def add_pet(self, pet):
        # Додає улюбленця до списку
        self.pets.append(pet)

    def show_all_pets(self):
        # Виводить інформацію про всіх домашніх улюбленців
        print("Мої домашні улюбленці:")
        for pet in self.pets:
            print(
                f"- {pet.breed}: {pet.name}, {pet.age} років, характер: {pet.nature}"
            )

# Створюємо собак різного віку
dog1 = Labrador("Рекс", 3)
dog2 = Shepherd("Барон", 5)
dog3 = Bulldog("Макс", 2)
dog4 = Bulldog("Арс", 10)
dog5 = Shepherd("Бар", 4)

# Створюємо об'єкт Pets
my_pets = Pets()

# Додаємо собак до списку улюбленців
my_pets.add_pet(dog1)
my_pets.add_pet(dog2)
my_pets.add_pet(dog3)
my_pets.add_pet(dog5)

# Виводимо інформацію про домашніх тварин
my_pets.show_all_pets()

print("\nПоведінка собак:")
dog1.swim()
dog2.guard()
dog3.rest()
dog4.rest()
