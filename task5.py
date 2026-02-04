class Buffer:
    def __init__(self):
        # Внутрішній список для накопичення елементів послідовності
        self.data = []

    def add(self, *a):
        # Додає наступну частину послідовності
        for number in a:
            self.data.append(number)

            # Обробляємо п'ятірки поки в буфері є щонайменше 5 елементів
            while len(self.data) >= 5:
                five = self.data[:5]              # перші 5 елементів
                print("Сума п’ятірки:", sum(five)) # вивід суми
                self.data = self.data[5:]          # видаляємо використані 5 елементів

    def get_current_part(self):
        # Повертає елементи, які залишилися в буфері
        return self.data


# Приклад використання
if __name__ == "__main__":
    buf = Buffer()

    buf.add(1, 2, 3)
    print("Поточний буфер:", buf.get_current_part())

    buf.add(4, 5, 6, 7, 8, 9)
    print("Поточний буфер:", buf.get_current_part())

    buf.add(10, 11)
    print("Поточний буфер:", buf.get_current_part())
