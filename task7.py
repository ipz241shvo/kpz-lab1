class DecimalToRoman:
    def __init__(self, number):
        if not isinstance(number, int) or not (1 <= number <= 3999):
            raise ValueError("Число має бути цілим у діапазоні 1–3999")
        self.number = number

    def convert(self):
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = ""
        num = self.number

        for value, symbol in roman_map:
            while num >= value:
                result += symbol
                num -= value

        return result


class RomanToDecimal:
    def __init__(self, roman):
        if not isinstance(roman, str) or not roman.strip():
            raise ValueError("Римське число не може бути порожнім")

        self.roman = roman.upper()
        self._validate_roman()

    def _validate_roman(self):
        valid_chars = {"I", "V", "X", "L", "C", "D", "M"}
        if any(ch not in valid_chars for ch in self.roman):
            raise ValueError("Римське число містить недопустимі символи")

        forbidden_repeats = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"]
        for seq in forbidden_repeats:
            if seq in self.roman:
                raise ValueError("Некоректні повторення у римському числі")

        forbidden_subtractions = ["IL", "IC", "ID", "IM", "XD", "XM", "VX", "LC", "DM"]
        for seq in forbidden_subtractions:
            if seq in self.roman:
                raise ValueError("Некоректне правило віднімання у римському числі")

    def convert(self):
        roman_values = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100,
            "D": 500, "M": 1000
        }

        total = 0
        prev = 0

        for ch in reversed(self.roman):
            value = roman_values[ch]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total


# -------- Ввід користувача --------

def get_decimal_input():
    while True:
        value = input("Введіть десяткове число (1–3999): ").strip()
        if not value.isdigit():
            print("Помилка: потрібно ввести додатне ціле число.")
            continue

        number = int(value)
        if 1 <= number <= 3999:
            return number

        print("Помилка: число має бути в діапазоні 1–3999.")


def get_roman_input():
    while True:
        value = input("Введіть римське число: ").strip()
        try:
            RomanToDecimal(value)
            return value
        except ValueError as e:
            print("Помилка:", e)


# -------- Керування програмою --------

def main():
    while True:
        print("\nОберіть режим:")
        print("1 — Десяткове → Римське")
        print("2 — Римське → Десяткове")
        print("0 — Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            number = get_decimal_input()
            print("Римське число:", DecimalToRoman(number).convert())

        elif choice == "2":
            roman = get_roman_input()
            print("Десяткове число:", RomanToDecimal(roman).convert())

        elif choice == "0":
            print("Завершення програми.")
            break

        else:
            print("Помилка: введіть 1, 2 або 0.")


if __name__ == "__main__":
    main()
