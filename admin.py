class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can remove user"]

    def show_privileges(self):
        print("Admin :-\n" + str(self.privileges))


class User:
    def __init__(self, first_name, last_name, birth_date):
        self.fn = first_name
        self.ln = last_name
        self.bd = birth_date

    def name(self):
        print("FIRST NAME : " + self.fn.title() + "\nLAST NAME : " + self.ln.title())

    def dob(self):
        print("D.O.B. : " + str(self.bd))


class Admin(User):
    def __init__(self, first_name, last_name, birth_date):
        self.privileges = ["can add post", "can delete post", "can remove user"]
        super().__init__(first_name, last_name, birth_date)
        self.Privileges = Privileges()


call = Admin("Mohammad", "Asim", "11.01.2001")
call.Privileges.show_privileges()
