class Wallet:
    def __init__(self, balance=0):
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. Balance: {self.__balance}")
        else:
            print("Amount positive hona chahiye")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount positive hona chahiye")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. Balance: {self.__balance}")

    @property
    def balance(self):
        return self.__balance  

w = Wallet(1000)
w.deposit(500)
w.withdraw(200)
print("Current Balance:", w.balance)