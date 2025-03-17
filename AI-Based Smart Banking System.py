class BankAccount:
    exchange_rates = {
        ("USD", "EUR"): 0.91,
        ("EUR", "USD"): 1.10,
        ("USD", "IDR"): 15000,
        ("IDR", "USD"): 0.000067,
        ("EUR", "IDR"): 16500,
        ("IDR", "EUR"): 0.000061
    }

    def __init__(self, account_holder, balance, currency):
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency

    def __str__(self):
        return f"{self.account_holder}'s Account: Balance = {self.currency} {self.balance:.2f}"

    def convert_currency(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        key = (from_currency, to_currency)
        if key in self.exchange_rates:
            return amount * self.exchange_rates[key]
        else:
            print("Exchange rate not available for this currency pair.")
            return 0

    def __add__(self, other):
        converted_amount = self.convert_currency(other.balance, other.currency, self.currency)
        self.balance += converted_amount
        print(f"{other.account_holder}'s funds converted to {self.currency} and added.")
        return self

    def __sub__(self, amount):
        converted_amount = self.convert_currency(amount, "USD", self.currency)
        if self.balance >= converted_amount:
            self.balance -= converted_amount
        else:
            print("Insufficient balance for withdrawal!")
        return self

    def apply_interest(self):
        interest_rate = 0.02 if self.balance > 5000 else 0.01
        self.balance += self.balance * interest_rate
        print("Applying interest...")

    def check_balance_warning(self):
        if self.balance < 100:
            print("Low Balance Warning!")


# Contoh penggunaan
john = BankAccount("John", 5000, "USD")
print(f"{john.account_holder}'s Account: Initial Balance = ${john.balance}")
john.apply_interest()
print(john)

emily = BankAccount("Emily", 1000, "EUR")
print(f"{emily.account_holder}'s Account: Initial Balance = €{emily.balance}")
usd_equivalent = emily.convert_currency(emily.balance, "EUR", "USD")
print(f"Converted to USD: ${usd_equivalent:.2f}")
emily -= 1200  # Emily mencoba menarik $1200 USD
print(emily)
