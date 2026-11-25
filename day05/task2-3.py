class Account:
    def get_interest_rate(self):
        return 4

class SavingsAccount(Account):
    def get_interest_rate(self):
        return 6.5

class FixedDeposit(Account):
    def get_interest_rate(self):
        return 8.0

accounts = [Account(), SavingsAccount(), FixedDeposit()]

for acc in accounts:
    print(acc.get_interest_rate())