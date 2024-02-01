import src.model as model
from src.repository.fake_repository import FakeRepository
from src.repository.abstract_repository import AbstractRepository

# ========================================================
# Insert repository here:
# ========================================================
repository: AbstractRepository = FakeRepository()

test_user = model.User('Christian')
test_account = model.BankAccount('Santander')
test_payee = model.Payee('Gina', 12345678, 123456, 'landlord')
test_payment = model.Payment(1, 1, 2000.00)
test_regular_payment = model.RegularPayment(1, 1, 300.00)

# ========================================================
# Test creation of entities using repository.add*() and repository.get*()
# ========================================================
def test_create_user():
    user_id = test_user.id
    repository.add_user(test_user)

    retrieved_user = repository.get_user(user_id)
    assert retrieved_user.name == 'Christian'

def test_create_account():
    account_id = test_account.id
    repository.add_bank_account(test_account)

    retrieved_account = repository.get_bank_account(account_id)
    assert retrieved_account.bank_name == 'Santander'

def test_create_payee():
    payee_id = test_payee.id
    repository.add_payee(test_payee)

    retrieved_payee = repository.get_payee(payee_id)
    assert retrieved_payee.name == 'Gina'

def test_create_payment():
    payment_id = test_payment.id
    repository.add_payment(test_payment)

    retrieved_payment = repository.get_payment(payment_id)
    assert retrieved_payment.amount == 2000.00

'''
def test_create_regular_payment():
    regular_payment_id = test_regular_payment.id
    repository.add_regular_payment(test_regular_payment)

    retrieved_regular_payment = repository.get_regular_payment(regular_payment_id)
    assert retrieved_regular_payment.amount == 300.00
'''
