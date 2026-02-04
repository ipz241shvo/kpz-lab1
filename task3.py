class Car:
    def __init__(self, brand, model, year, acceleration_step):
        ## Публічні дані
        # Марка автомобіля
        self.brand = brand
        # Модель автомобіля
        self.model = model
        # Рік випуску
        self.year = year

        ## Приватні поля стану
        # Поточна швидкість (початково 0)
        self.__speed = 0
        # Крок прискорення (індивідуальний)
        self.__acceleration_step = acceleration_step

    def accelerate(self):
        # Збільшує швидкість на індивідуальний крок
        self.__speed += self.__acceleration_step

    def brake(self):
        # Зменшує швидкість на індивідуальний крок
        self.__speed -= self.__acceleration_step
        # Не дозволяємо швидкості бути від'ємною
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        # Повертає поточну швидкість
        return self.__speed

# Приклад використання

cars = [
    Car("Toyota", "Corolla", 2020, 5),
    Car("BMW", "X5", 2019, 10)
]

for car in cars:
    print(f"\nАвтомобіль: {car.brand} {car.model} ({car.year})")

    print("Прискорення:")
    for i in range(5):
        car.accelerate()
        print(f"  Після прискорення {i + 1}: швидкість = {car.get_speed()}")

    print("Гальмування:")
    for i in range(5):
        car.brake()
        print(f"  Після гальмування {i + 1}: швидкість = {car.get_speed()}")
