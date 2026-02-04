from user import User

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "Allowed to add message",
                "Allowed to delete users",
                "Allowed to ban users",
                "Allowed to view logs",
            ]
        self.privileges = privileges

    def show_privileges(self):
        print("=== Привілеї адміністратора ===")
        if not self.privileges:
            print("Немає привілеїв.")
            return
        for p in self.privileges:
            print(f"- {p}")


class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, newsletter_agree=False):
        super().__init__(first_name, last_name, email, nickname, newsletter_agree)
        self.priv = Privileges()
