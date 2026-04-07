from abc import ABC, abstractmethod
import random
from enum import Enum

class BankError(Exception):
    """Базовый класс для ошибок банка"""
    pass

class AccountFrozenError(BankError):
    """Ошибка: счет заморожен"""
    pass


class AccountClosedError(BankError):
    """Ошибка: счет закрыт"""
    pass

class InvalidOperationError(BankError):
    """Ошибка: некорректная операция (например, отрицательная сумма)"""
    pass

class InsufficientFundsError(BankError):
    """Ошибка: недостаточно средств"""
    pass

class Status(Enum):
    ACTIVE = "активный"
    FROZEN = "замороженный"
    CLOSED = "закрытый"


class Currency(Enum):
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"
    KZT = "KZT"
    CNY = "CNY"

class AbstractAccount(ABC):
    def __init__(self, owner, balance=0.0, account_id=None):
        self.account_id = account_id
        self.owner = owner
        self._balance = float(balance)  # Защищенный баланс
        self.status = Status.ACTIVE  # По умолчанию активен

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_account_info(self):
        pass

class BankAccount(AbstractAccount):
    def __init__(self, owner, balance=0.0, account_id=None, currency=Currency.RUB):
        # Автоматическая генерация короткого айди, если он не задан
        if account_id is None:
            account_id = str(random.randint(10000000, 99999999))

        super().__init__(owner, balance, account_id)
        self.currency = currency  # Валюта

    def _check_transaction(self, amount):
        if self.status == Status.FROZEN:
            raise AccountFrozenError("Операция невозможна: счет заморожен.")
        if self.status == Status.CLOSED:
            raise AccountClosedError("Операция невозможна: счет закрыт.")
        if amount <= 0:
            raise InvalidOperationError("Сумма должна быть положительной.")

    def deposit(self, amount):
        self._check_transaction(amount)
        self._balance += amount
        print(f"Пополнение: +{amount} {self.currency.value}")

    def withdraw(self, amount):
        self._check_transaction(amount)
        if amount > self._balance:
            raise InsufficientFundsError("Недостаточно средств на балансе.")
        self._balance -= amount
        print(f"Снятие: -{amount} {self.currency.value}")

    def get_account_info(self):
        return f"Счет {self.account_id} ({self.owner}): {self._balance} {self.currency.value}"

    def __str__(self):
        last_4 = self.account_id[-4:]  # Последние 4 цифры
        return (f"--- Информация о счете ---\n"
                f"Тип: BankAccount\n"
                f"Клиент: {self.owner}\n"
                f"Номер: ****{last_4}\n"
                f"Статус: {self.status.value}\n"
                f"Баланс: {self._balance} {self.currency.value}\n")


if __name__ == "__main__":
    try:
        acc1 = BankAccount("Иван Иванов", 1000, currency=Currency.USD)
        acc2 = BankAccount("Петр Петров", 500)
        acc2.status = Status.FROZEN

        print(acc1)
        print(acc2)

        acc1.deposit(500)
        acc1.withdraw(200)
        print(f"Новый баланс Ивана: {acc1.get_account_info()}")

        print("\nПопытка снять деньги с замороженного счета...")
        acc2.withdraw(100)

    except BankError as e:
        print(f"Ошибка Банка: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
