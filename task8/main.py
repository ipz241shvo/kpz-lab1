from shop import Shop, Discount


def part_a():
    # a) Екземпляр store, вивід атрибутів, виклик методів
    store = Shop("Rozetka", "інтернет-магазин техніки")

    print("a) Атрибути окремо:")
    print("shop_name:", store.shop_name)
    print("store_type:", store.store_type)

    print("\nВиклик describe_shop():")
    store.describe_shop()

    print("\nВиклик open_shop():")
    store.open_shop()


def part_b():
    # b) Три різні екземпляри, describe_shop() для кожного
    store1 = Shop("EVA", "косметика")
    store2 = Shop("ATB", "продукти")
    store3 = Shop("Kasta", "одяг")

    print("\nb) Три магазини:")
    store1.describe_shop()
    print()
    store2.describe_shop()
    print()
    store3.describe_shop()


def part_c():
    # c) number_of_units (0), потім змінити і вивести знову
    store = Shop("Epicentr", "будматеріали")

    print("\nc) number_of_units спочатку:", store.number_of_units)
    store.number_of_units = 12
    print("number_of_units після зміни:", store.number_of_units)


def part_d():
    # d) set_number_of_units() та increment_number_of_units()
    store = Shop("Foxtrot", "електроніка")

    print("\nd) set_number_of_units та increment_number_of_units:")
    print("Початково number_of_units:", store.number_of_units)

    store.set_number_of_units(20)
    print("Після set_number_of_units(20):", store.number_of_units)

    store.increment_number_of_units(5)
    print("Після increment_number_of_units(5):", store.number_of_units)


def part_e():
    # e) Discount(Shop) + discount_products + get_discounts_products()
    store_discount = Discount(
        "Comfy",
        "побутова техніка",
        discount_products=["Навушники", "Мишка", "Клавіатура"]
    )

    print("\ne) Товари зі знижкою:")
    store_discount.get_discounts_products()


def part_f():
    # f) Перевірка імпорту Shop() (клас імпортовано з shop.py)
    all_store = Shop("AllStore", "універсальний магазин")

    print("\nf) Перевірка імпорту:")
    all_store.open_shop()


def main():
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_f()


if __name__ == "__main__":
    main()
