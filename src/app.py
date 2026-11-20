import sys
from dbhelper import DBhelper

class Daraz:

    def __init__(self):

        # connect to the database
        self.db = DBhelper()
        self.menu()

    def menu(self):

        user_input = input("""
            1. Enter 1 to Register
            2. Enter 2 to Login
            3. Anything else to leave
        """)

        if user_input == "1":
            self.register()
        if user_input == "2":
            self.login()
        else:
            sys.exit(1000)

    def login_menu(self):
        input("""
            1. Enter 1 to See Profile
            2. Enter 2 to Edit Profile
            3. Enter 3 to Delete Profile
            4. Enter 4 to Logout
            
        """)

    def register(self):
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        password = input("Enter the password: ")

        response = self.db.register(name, email, password)

        if response:
            print("Registration Successful")
        else:
            print("Registration Failed")

        self.menu()

    def login(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        data = self.db.search(email, password)

        if len(data) == 0:
            print("Incorrect Email/Password")
            self.login()
        else:
            print("Hello", data[0][1])
            self.login_menu()

obj = Daraz()