class BankError(Exception): pass
class AccountFrozenError(BankError): pass
class InsufficientFundsError(BankError): pass
class InvalidOperationError(BankError): pass