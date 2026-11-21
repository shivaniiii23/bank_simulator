
from models.account import Account


class CurrentAccount(Account):
    
    OVERDRAFT_LIMIT = 5000.0

    def __init__(self, account_no, holder_name, balance, pin):
        super().__init__(account_no, holder_name, balance, pin, account_type="Current")

    def withdraw(self, amount):
        
        if amount <= 0:
            return False, "Amount must be greater than zero", None

        if self._balance - amount < -self.OVERDRAFT_LIMIT:
            return (
                False,
                f"Withdrawal denied. Overdraft limit of Rs. {self.OVERDRAFT_LIMIT:.2f} exceeded.",
                None,
            )

        self._balance -= amount
        return True, "Withdrawal successful", self._balance

    @classmethod
    def from_dict(cls, data):
        
        obj = cls(data["account_no"], data["holder_name"], data["balance"], "0000")
        obj._pin_hash = data["pin_hash"]
        return obj
