class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid Balance")


account = BankAccount(10000)

print(account.balance)

account.balance = 15000

print(account.balance)

account.balance = -5000

