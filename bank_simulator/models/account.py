
import hashlib


class Account:
   
    def __init__(self, account_no, holder_name, balance, pin, account_type="Account"):
        self.account_no = account_no
        self.holder_name = holder_name
        self._balance = float(balance)
        self._pin_hash = self._hash_pin(pin)
        self.account_type = account_type

    @staticmethod
    def _hash_pin(pin):
       
        return hashlib.sha256(str(pin).encode()).hexdigest()

    def verify_pin(self, pin):
       
        return self._hash_pin(pin) == self._pin_hash

    @property
    def balance(self):
        
        return self._balance

    def deposit(self, amount):
        
        if amount <= 0:
            return False, "Amount must be greater than zero", None

        self._balance += amount
        return True, "Deposit successful", self._balance

    def withdraw(self, amount):
        
        if amount <= 0:
            return False, "Amount must be greater than zero", None

        if amount > self._balance:
            return False, "Insufficient balance for this transaction", None

        self._balance -= amount
        return True, "Withdrawal successful", self._balance

    def display_statement(self):
        
        print(f"Account No   : {self.account_no}")
        print(f"Holder Name  : {self.holder_name}")
        print(f"Account Type : {self.account_type}")
        print(f"Balance      : Rs. {self._balance:.2f}")

    def to_dict(self):
        
        return {
            "account_no": self.account_no,
            "holder_name": self.holder_name,
            "balance": self._balance,
            "pin_hash": self._pin_hash,
            "account_type": self.account_type,
        }
