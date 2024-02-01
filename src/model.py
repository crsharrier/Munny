from datetime import date
from enum import Enum, auto
from typing import List

def validate_account_number():
    pass

def validate_sort_code():
    pass

class Frequency(Enum):
    DAILY = auto()
    WEEKLY = auto()
    MONTHLY = auto()
    ANNUALLY = auto()

class User:
    def __init__(self, name: str):
        self.id: int = None
        self.name = name        

class Payee:
    def __init__(self, 
                 name: str, 
                 description: str=None):
        self.id: int = None
        self.name = name
        self.description = description

class Employer:
    def __init__(self, 
                 name: str, 
                 description: str=None):
        self.id: int = None
        self.name = name
        self.description = description

class BankAccount:
    def __init__(self, 
                 owner: User, 
                 bank_name: str,
                 account_purpose: str):
        self.id: int = None
        self.owner = owner
        self.bank_name = bank_name
        self.account_purpose = account_purpose

class InPayment:
    def __init__(self,
                 destination: BankAccount,
                 source: Employer,
                 date: date,
                 net_amount: float):
        self.destination = destination
        self.source = source
        self.date = date
        self.net_amount = net_amount

class OutPayment:
    def __init__(self,
                 source_account: BankAccount,
                 payee: Payee,
                 date: date,
                 amount: float,
                 previous_payment=None):
        self.source_account = source_account
        self.payee = payee
        self.date = date
        self.amount = amount
        self.previous_payment: OutPayment = previous_payment
        self.next_payment: OutPayment = None
    
    def create_next_payment():
        pass


        
class Deduction:
    def __init__(self,
                 percentage: float,
                 allowance: float=None):
        self.percentage = percentage
        self.allowance = allowance

class Salary:
    def __init__(self,
                 net_amount: float,
                 deductions: List[Deduction]=None):
        self.net_amount = net_amount
        self.deductions = deductions

    def calculate_income_payments():
        pass