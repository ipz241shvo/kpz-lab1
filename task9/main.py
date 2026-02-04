from user import User
from admin import Admin

def demo_users():
    users = [
        User("Володимир", "Шваб", "vova@example.com", "vshvab", True),
        User("Анна", "Коваль", "anna@example.com", "ann_k", False),
        User("Максим", "Іванов", "max@example.com", "maximchik", True),
    ]

    for u in users:
        u.describe_user()
        u.greeting_user()
        print()

def demo_login_attempts():
    u = User("Тест", "Користувач", "test@example.com", "tester")
    u.increment_login_attempts()
    u.increment_login_attempts()
    u.increment_login_attempts()
    print(f"login_attempts після збільшень: {u.login_attempts}")

    u.reset_login_attempts()
    print(f"login_attempts після reset: {u.login_attempts}")
    print()

def demo_admin_privileges():
    admin = Admin("Адмін", "Сайту", "admin@example.com", "root", True)
    admin.priv.show_privileges()
    print()

if __name__ == "__main__":
    demo_users()            # a
    demo_login_attempts()   # b
    demo_admin_privileges() # c + d + e
