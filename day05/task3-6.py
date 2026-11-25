class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies!")
        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies!")
        return self.amount > other.amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

m1 = Money(100, "INR")
m2 = Money(200, "INR")
m3 = Money(50, "USD")

print(m1 < m2) 
print(m1 > m2)  
