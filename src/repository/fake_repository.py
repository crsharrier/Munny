from .abstract_repository import AbstractRepository
from typing import Set
from .. import model

'''
Fake implementation of AbstractRepository for testing purposes
'''
class FakeRepository(AbstractRepository):
    def __init__(self):
        self.users: Set[model.User] = set()
        self.bank_accounts: Set[model.BankAccount] = set()
        self.payees: Set[model.Payee] = set()
        self.payments: Set[model.Payment] = set()
        self.regular_payments: Set[model.RegularPayment] = set()

    def add_user(self, user: model.User):
        self.users.add(user)
    
    def add_bank_account(self, account: model.BankAccount):
        self.bank_accounts.add(account)

    def add_payee(self, payee: model.Payee):
        self.payees.add(payee)
    
    def add_payment(self, payment: model.Payment):
        self.payments.add(payment)
    
    def add_regular_payment(self, regular_payment: model.RegularPayment):
        self.regular_payments.add(regular_payment)
    
    def get_user(self, id: int):
        for user in self.users:
            if user.id == id:
                return user
        return None
    
    def get_bank_account(self, id: int):
        for account in self.bank_accounts:
            if account.id == id:
                return account
        return None
    
    def get_payee(self, id: int):
        for payee in self.payees:
            if payee.id == id:
                return payee
        return None
    
    def get_payment(self, id: int):
        for payment in self.payments:
            if payment.id == id:
                return payment
        return None

    def get_regular_payment(self, id: int):
        for regular_payment in self.regular_payments:
            if regular_payment.id == id:
                return regular_payment
        return None