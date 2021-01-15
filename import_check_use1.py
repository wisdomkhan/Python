from user_class import User


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can remove user"]

    def show_privileges(self):
        print("Admin :-\n" + str(self.privileges))


class Admin(User):
    def __init__(self, first_name, last_name, birth_date):
        self.privileges = ["can add post", "can delete post", "can remove user"]
        super().__init__(first_name, last_name, birth_date)
        self.Privileges = Privileges()
