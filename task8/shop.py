class Shop:
    def __init__(self, shop_name, store_type):
        # Назва магазину
        self.shop_name = shop_name
        # Тип магазину
        self.store_type = store_type
        # Кількість видів товару (за замовчуванням 0)
        self.number_of_units = 0

    def describe_shop(self):
        # Виводить інформацію про магазин
        print(f"Магазин: {self.shop_name}")
        print(f"Тип магазину: {self.store_type}")

    def open_shop(self):
        # Повідомляє, що магазин відкритий
        print("Онлайн-магазин відкритий!")

    def set_number_of_units(self, value):
        # Задає кількість видів товару
        if not isinstance(value, int):
            raise ValueError("Кількість видів товару має бути цілим числом.")
        if value < 0:
            raise ValueError("Кількість видів товару не може бути від’ємною.")
        self.number_of_units = value

    def increment_number_of_units(self, step):
        # Збільшує кількість видів товару на задану величину
        if not isinstance(step, int):
            raise ValueError("Збільшення має бути цілим числом.")
        if step < 0:
            raise ValueError("Збільшення не може бути від’ємним.")
        self.number_of_units += step


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products=None):
        # Викликаємо конструктор батьківського класу
        super().__init__(shop_name, store_type)
        # Список товарів зі знижкою
        self.discount_products = discount_products if discount_products is not None else []

    def get_discounts_products(self):
        # Виводить список товарів зі знижкою
        if not self.discount_products:
            print("Наразі немає товарів зі знижкою.")
        else:
            print("Товари зі знижкою:")
            for item in self.discount_products:
                print(f"- {item}")
