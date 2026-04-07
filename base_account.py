from abc import ABC, abstractmethod
import random

class AbstractAccount(ABC):
    def __init__(self, owner, balance=0.0, account_id=None):
        self.account_id = account_id or str(random.randint(1000, 9999))
        self.owner = owner
        self._balance = float(balance)
        self.status = "active"

    @abstractmethod
    def withdraw(self, amount): pass

    @abstractmethod
    def get_account_info(self): pass