import model as model
import pandas as pd
from datetime import date
from repository.csv_repository import CSVRepository
from repository.sql_repository import SQLRepository

from ui.app import *

#repo = CSVRepository()
repo = SQLRepository()

user_christian = model.User('Christian')
user_renata = model.User('Renata')

payee_gina = model.Payee('Gina Leong')

employer_kubrick = model.Employer('Kubrick')

savings = model.BankAccount(user_renata, 'Natwest Savings', 'savings')
food_household = model.BankAccount(user_christian, 'Santander Current', 'Food, Household')
monzo_chris = model.BankAccount(user_christian, 'Christian\'s Monzo', 'Travel, Spending Money')
monzo_ren = model.BankAccount(user_renata, 'Renata\'s Monzo', 'Travel, Spending Money')

in_payment1 = model.InPayment(monzo_chris, employer_kubrick, date.today(), 100)

out_payment1 = model.OutPayment(monzo_chris, payee_gina, date.today(), 50)

repo.add_user(user_christian)
repo.add_user(user_renata)

repo.add_payee(payee_gina)
repo.add_employer(employer_kubrick)

repo.add_bank_account(savings)
repo.add_bank_account(food_household)
repo.add_bank_account(monzo_chris)
repo.add_bank_account(monzo_ren)

repo.add_in_payment(in_payment1)
repo.add_out_payment(out_payment1)

print(repo.users)
print(repo.in_payments)
print(repo.out_payments)

