class Bank:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
        self.__operations = []
        self.__operations.append(f"Створено рахунок з балансом {initial_balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__operations.append(f"Поповнення на {amount}")
        else:
            self.__operations.append(
                f"Невдала спроба поповнення на {amount}"
            )

    def withdraw(self, amount):
        if amount <= 0:
            self.__operations.append(
                f"Невдала спроба зняття на {amount}"
            )
        elif amount > self.__balance:
            self.__operations.append(
                f"Невдала спроба зняття {amount} (недостатньо коштів)"
            )
        else:
            self.__balance -= amount
            self.__operations.append(f"Зняття {amount}")

    def show_balance(self):
        return self.__balance

    def show_operations(self):
        return self.__operations

# Приклад використання
account = Bank(1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
account.withdraw(20000)
account.deposit(-50)

print("Баланс:", account.show_balance())
print("\nІсторія операцій:")
for op in account.show_operations():
    print(op)
