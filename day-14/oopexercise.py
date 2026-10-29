class Account:

    def __init__(self, username, acc_number, acc_balance, password):
        self.__username = username
        self.__acc_number = acc_number
        self.__acc_balance = acc_balance
        self.__password = password

    def login(self, username, password):
        if username == self.__username and password == self.__password:
            print("Login successful")
            return True
        else:
            print("Invalid username or password")
            return False

    def __show_details(self):
        print("Username:", self.__username)
        print("Account Number:", self.__acc_number)
        print("Account Balance:", self.__acc_balance)

    def show_details(self, username, password):
        if self.login(username, password):
            self.__show_details()


# Creating first object
account1 = Account("sardip", 101, 50000, "1234")

# Creating second object
account2 = Account("ram", 102, 30000, "5678")


# Login and show details
account1.show_details("sardip", "1234")

print()

account2.show_details("ram", "5678")