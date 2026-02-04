import random

class Coin:
    def __init__(self):
        self.__sideup = "орел"

    def toss(self):
        self.__sideup = random.choice(["орел", "решка"])

    def get_sideup(self):
        return self.__sideup


# Перевірка введення
while True:
    user_input = input("Введіть кількість підкидань (додатне число): ")

    if user_input.isdigit() and int(user_input) > 0:
        n = int(user_input)
        break
    else:
        print("Помилка! Введіть додатне ціле число.")

# Приклад використання
coin = Coin()

for i in range(n):
    coin.toss()
    print(f"Підкидання {i + 1}: {coin.get_sideup()}")
