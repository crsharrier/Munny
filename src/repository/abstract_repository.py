from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    # ========================================================
    # add() methods
    # ========================================================
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def add_payee(self, payee):
        pass

    @abstractmethod
    def add_employer(self, employer):
        pass

    @abstractmethod
    def add_bank_account(self, BankAccount):
        pass

    @abstractmethod
    def add_in_payment(self, payment):
        pass

    @abstractmethod
    def add_out_payment(self, payment):
        pass

    # ========================================================
    # @property methods
    # ========================================================
    @property
    @abstractmethod
    def users():
        pass

    @property
    @abstractmethod
    def payees():
        pass

    @property
    @abstractmethod
    def employers():
        pass

    @property
    @abstractmethod
    def bank_accounts():
        pass

    @property
    @abstractmethod
    def in_payments():
        pass

    @property
    @abstractmethod
    def out_payments():
        pass
    