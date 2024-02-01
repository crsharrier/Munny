from repository.abstract_repository import AbstractRepository
import sqlite3
import model
import pandas as pd

from services import PATH_TO_DB

class SQLRepository(AbstractRepository):
    def __init__(self):
        self.conn: sqlite3.Connection = sqlite3.connect(PATH_TO_DB)
        self.cursor: sqlite3.Cursor = self.conn.cursor()
        print(f'Connected to database @ {PATH_TO_DB}!')
        self.run_script('create_tables')

    def run_script(self, script_name: str):
        script_path = f'./src/repository/SQL/{script_name}.sql'
        try:
            with open(script_path, 'r') as script_file:
                sql_script = script_file.read()

            self.conn.executescript(sql_script)
            self.conn.commit()

            print(f"{script_name} executed successfully.")
        except Exception as e:
            print(f"Error executing {script_name}:", str(e))
    
    @property
    def users(self):
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in self.cursor.description]) 
        return df
    
    @property
    def payees(self):
        self.cursor.execute("SELECT * FROM payee")
        result = self.cursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in self.cursor.description]) 
        return df
    
    @property
    def employers(self):
        self.cursor.execute("SELECT * FROM employer")
        result = self.cursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in self.cursor.description]) 
        return df
    
    @property
    def bank_accounts(self):
        self.cursor.execute("SELECT * FROM bank_account")
        result = self.cursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in self.cursor.description]) 
        return df

    @property
    def in_payments(self):
        self.cursor.execute("SELECT * FROM in_payment")
        result = self.cursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in self.cursor.description]) 
        return df

    @property
    def out_payments(self):
        self.cursor.execute("SELECT * FROM out_payment")
        result = self.cursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in self.cursor.description]) 
        return df
    


    # ========================================================
    # add() methods
    # ========================================================
    def add_user(self, user: model.User):
        result = self.cursor.execute(
            '''
            INSERT INTO user (name)
            VALUES (?)
            ''', (user.name,)
        )
        user.id = self.cursor.lastrowid

    def add_payee(self, payee: model.Payee):
        if payee.description is not None:
            self.cursor.execute(
            '''
            INSERT INTO payee (name, description)
            VALUES (?, ?)
            ''', (payee.name, payee.description)
            )   
        else:
            self.cursor.execute(
                '''
                INSERT INTO payee (name)
                VALUES (?)
                ''', (payee.name,)
            )
        payee.id = self.cursor.lastrowid

    def add_employer(self, employer: model.Employer):
        if employer.description is not None:
            self.cursor.execute(
            '''
            INSERT INTO employer (name, description)
            VALUES (?, ?)
            ''', (employer.name, employer.description)
            )   
        else:
            self.cursor.execute(
                '''
                INSERT INTO employer (name)
                VALUES (?)
                ''', (employer.name,)
            )
        employer.id = self.cursor.lastrowid

    def add_bank_account(self, account: model.BankAccount):
        self.cursor.execute(
            '''
            INSERT INTO bank_account (user_id, bank_name)
            VALUES (?, ?)
            ''', (account.owner.id, account.bank_name)
        )
        account.id = self.cursor.lastrowid

    def add_in_payment(self, payment: model.InPayment):
        self.cursor.execute(
            '''
            INSERT INTO in_payment (account_id, employer_id, date, net_amount)
            VALUES (?, ?, ?, ?)
            ''', (payment.destination.id, payment.source.id, payment.date, payment.net_amount)
        )

    def add_out_payment(self, payment: model.OutPayment):
        self.cursor.execute(
            '''
            INSERT INTO out_payment (source_account_id, payee_id, date, amount)
            VALUES (?, ?, ?, ?)
            ''', (payment.source_account.id, payment.payee.id, payment.date, payment.amount)
        )

