class User:
    def __init__(self, first_name, last_name, birth_date):
        self.fn = first_name
        self.ln = last_name
        self.bd = birth_date

    def name(self):
        print("FIRST NAME : " + self.fn.title() + "\nLAST NAME : " + self.ln.title())

    def dob(self):
        print("D.O.B. : " + str(self.bd))
