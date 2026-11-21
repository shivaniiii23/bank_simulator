
class InsufficientBalanceError(Exception):
    

    def __init__(self, message="Insufficient balance for this transaction"):
        self.message = message
        super().__init__(self.message)


class InvalidPinError(Exception):
    

    def __init__(self, message="Incorrect PIN entered"):
        self.message = message
        super().__init__(self.message)


class AccountNotFoundError(Exception):
    

    def __init__(self, message="No account found with this account number"):
        self.message = message
        super().__init__(self.message)


class InvalidAmountError(Exception):
    
    def __init__(self, message="Amount must be a positive number"):
        self.message = message
        super().__init__(self.message)