from base_account import AbstractAccount
from exceptions import InsufficientFundsError, InvalidOperationError

class SavingAccount(AbstractAccount):
    def __init__(self, owner, balance, interest_rate=0.05, min_balance=1000):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def calculate_monthly_profit(self):
        return self._balance * self.interest_rate

    def withdraw(self, amount):
        if self._balance - amount < self.min_balance:
            raise InsufficientFundsError(f"Нельзя снять ниже лимита в {self.min_balance}")
        self._balance -= amount

    def get_account_info(self):
        return f"Saving: {self.owner}, Баланс: {self._balance}"

class PremiumAccount(AbstractAccount):
    def __init__(self, owner, balance, overdraft_limit=5000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
        self.fee = 50

    def withdraw(self, amount):
        total_debit = amount + self.fee
        if self._balance - total_debit < -self.overdraft_limit:
            raise InsufficientFundsError("Превышен лимит овердрафта")
        self._balance -= total_debit

    def get_account_info(self):
        return f"Premium: {self.owner}, Баланс: {self._balance} (Лимит: {self.overdraft_limit})"

class InvestmentAccount(AbstractAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self.assets = {"stocks": 0.12, "bonds": 0.05, "etf": 0.08}

    def project_yearly_growth(self):
        avg_yield = sum(self.assets.values()) / len(self.assets)
        return self._balance * avg_yield

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError("На инвест-счете нельзя уходить в минус")
        self._balance -= amount

    def get_account_info(self):
        assets_list = ", ".join(self.assets.keys())
        return f"Investment: {self.owner}, Активы: {assets_list}"