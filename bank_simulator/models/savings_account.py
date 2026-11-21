

from models.account import Account


class SavingsAccount(Account):
   

    MIN_BALANCE = 1000.0
    INTEREST_RATE = 4.0  

    def __init__(self, account_no, holder_name, balance, pin):
        super().__init__(account_no, holder_name, balance, pin, account_type="Savings")

    def withdraw(self, amount):
        
        if amount <= 0:
            return False, "Amount must be greater than zero", None

        if self._balance - amount < self.MIN_BALANCE:
            return (
                False,
                f"Withdrawal denied. Minimum balance of Rs. {self.MIN_BALANCE:.2f} "
                f"must be maintained in a Savings Account.",
                None,
            )

        self._balance -= amount
        return True, "Withdrawal successful", self._balance

    def calculate_interest(self):
        
        return (self._balance * self.INTEREST_RATE) / 100

    @classmethod
    def from_dict(cls, data):
       
        obj = cls(data["account_no"], data["holder_name"], data["balance"], "0000")
        obj._pin_hash = data["pin_hash"]
        return obj

