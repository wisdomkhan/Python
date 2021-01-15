class User:
    def __init__(self, first_name, last_name, birth_date):
        self.fn = first_name
        self.ln = last_name
        self.bd = birth_date

    def name(self):
        print("FIRST NAME : " + self.fn.title() + "\nLAST NAME : " + self.ln.title())

    def dob(self):
        print("D.O.B. : " + str(self.bd))


regi = {}
p = True

while p:
    user = User(input('Enter first name\t'), input('Enter last name\t'), input("Enter date of birth(DD.MM.YY)\t"))
    print("USER REGISTERED")
    regi[user.fn] = user.ln, user.bd
    c = input('Any new sign-ups left?\t')
    if c.lower() != 'yes':
        p = False
print(regi)
