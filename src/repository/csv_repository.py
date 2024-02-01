from repository.abstract_repository import AbstractRepository
import pandas as pd
import model

class CSVRepository(AbstractRepository):
    def __init__(self):
        self.users = pd.DataFrame(columns=['user_id', 'name'])
        self.bank_accounts = pd.DataFrame(columns=['account_id', 'name', 'account_purpose', 'payments', 'regular_payments'])
        self.payees = pd.DataFrame(columns=['payee_id', 'name', 'account_number', 'sort_code', 'description', 'payments', 'regular_payments'])
        self.payments = pd.DataFrame(columns=['source_account_id', 'payee_id', 'amount', 'date'])
        #self.regular_payments: self.dataframes.append(pd.DataFrame(columns=['user_id', 'name', 'bank_accounts']))

    # ========================================================
    # add() methods
    # ========================================================
    
    def add_user(self, user: model.User):
        new_row = {'user_id': user.id, 
                   'name': user.name
                   }
        self.users = self.users.append(new_row, ignore_index=True)

    def add_payee(self, payee: model.Payee):
        new_row = {'payee_id': payee.id, 
                   'name': payee.name, 
                   'account_number': payee.account_number, 
                   'sort_code': payee.sort_code, 
                   'description': payee.description, 
                   'payments': payee.payments, 
                   'regular_payments': payee.regular_payments}
        self.payees = self.payees.append(new_row, ignore_index=True)

    def add_bank_account():
        pass
    
    def add_bank_account(self, account: model.BankAccount):
        new_row = {
            'account_id': account.id, 
            'name': account.bank_name, 
            'account_purpose': account.account_purpose, 
            'payments': account.payments, 
            'regular_payments': account.regular_payments}
        self.bank_accounts = self.bank_accounts.append(new_row, ignore_index=True)
    
    def add_payee(self, payee: model.Payee):
        new_row = {'payee_id': payee.id, 
                   'name': payee.name, 
                   'account_number': payee.account_number, 
                   'sort_code': payee.sort_code, 
                   'description': payee.description, 
                   'payments': payee.payments, 
                   'regular_payments': payee.regular_payments}
        self.payees = self.payees.append(new_row, ignore_index=True)
    
    def add_in_payment(self, payment: model.InPayment):
        new_row = {'source_account_id': payment.source_account_id, 
                   'payee_id': payment.payee_id, 
                   'amount': payment.amount, 
                   'date': payment.date}
        self.payments = self.payments.append(new_row, ignore_index=True)

    def add_out_payment():
        pass
    

    # ========================================================
    # @property methods
    # ========================================================
    
    @property
    def users():
        pass
    
    @property
    def payees():
        pass

    @property
    def employers():
        pass

    @property
    def bank_accounts():
        pass
    
    
    @property
    def in_payments():
        pass

    @property
    def out_payments():
        pass