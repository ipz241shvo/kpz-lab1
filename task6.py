class NameLengthError(ValueError):
    def __init__(self, name):
        # Повідомлення про помилку
        super().__init__(f"Довжина імені '{name}' менша за 10 символів")


def check_name(name):
    # Перевіряє довжину імені
    if len(name) < 10:
        raise NameLengthError(name)


# Приклад використання
if __name__ == "__main__":
    try:
        user_name = input("Введіть ім'я: ")
        check_name(user_name)
    except NameLengthError as e:
        print(e)
