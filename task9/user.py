class User:
    def __init__(self, first_name, last_name, email, nickname, newsletter_agree=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.newsletter_agree = newsletter_agree
        self.login_attempts = 0

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        agree_text = "так" if self.newsletter_agree else "ні"
        print("=== Профіль користувача ===")
        print(f"Повне ім'я: {full_name}")
        print(f"Email: {self.email}")
        print(f"Нікнейм: {self.nickname}")
        print(f"Згода на розсилку: {agree_text}")

    def greeting_user(self):
        print(f"Вітаю, {self.first_name}! Раді бачити тебе на сайті 🙂")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
