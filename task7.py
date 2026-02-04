# -------- Константи --------

MIN_ROMAN_VALUE = 1
MAX_ROMAN_VALUE = 3999

ROMAN_MAP = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

ROMAN_VALUES = {
    "I": 1, "V": 5, "X": 10,
    "L": 50, "C": 100,
    "D": 500, "M": 1000
}

VALID_ROMAN_CHARS = {"I", "V", "X", "L", "C", "D", "M"}

FORBIDDEN_REPEATS = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"]

FORBIDDEN_SUBTRACTIONS = ["IL", "IC", "ID", "IM", "XD", "XM", "VX", "LC", "DM"]


# -------- Логіка конвертації --------

class DecimalToRoman:
    def __init__(self, number):
        if not isinstance(number, int) or not (MIN_ROMAN_VALUE <= number <= MAX_ROMAN_VALUE):
            raise ValueError(
                f"Число має бути цілим у діапазоні {MIN_ROMAN_VALUE}–{MAX_ROMAN_VALUE}"
            )
        self.number = number

    def convert(self):
        result = ""
        num = self.number

        for value, symbol in ROMAN_MAP:
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
        if any(ch not in VALID_ROMAN_CHARS for ch in self.roman):
            raise ValueError("Римське число містить недопустимі символи")

        for seq in FORBIDDEN_REPEATS:
            if seq in self.roman:
                raise ValueError("Некоректні повторення у римському числі")

        for seq in FORBIDDEN_SUBTRACTIONS:
            if seq in self.roman:
                raise ValueError("Некоректне правило віднімання у римському числі")

    def convert(self):
        total = 0
        prev = 0

        for ch in reversed(self.roman):
            value = ROMAN_VALUES[ch]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total


# -------- Ввід користувача --------

def get_decimal_input():
    while True:
        value = input(
            f"Введіть десяткове число ({MIN_ROMAN_VALUE}–{MAX_ROMAN_VALUE}): "
        ).strip()

        if not value.isdigit():
            print("Помилка: потрібно ввести додатне ціле число.")
            continue

        number = int(value)
        if MIN_ROMAN_VALUE <= number <= MAX_ROMAN_VALUE:
            return number

        print(
            f"Помилка: число має бути в діапазоні {MIN_ROMAN_VALUE}–{MAX_ROMAN_VALUE}."
        )


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
