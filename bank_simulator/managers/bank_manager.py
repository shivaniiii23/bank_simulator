
import random

from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount


class BankManager:
    
    def __init__(self):
        self.accounts = []   # LIST of Account objects (in-memory only)

    def _generate_account_number(self):
        
        existing_numbers = [acc.account_no for acc in self.accounts]

        account_no = random.randint(1000, 9999)
        while account_no in existing_numbers:
            account_no = random.randint(1000, 9999)

        return account_no

    def create_account(self, holder_name, initial_deposit, pin, account_type):
        
        account_no = self._generate_account_number()

        if account_type.lower() == "savings":
            account = SavingsAccount(account_no, holder_name, initial_deposit, pin)
        else:
            account = CurrentAccount(account_no, holder_name, initial_deposit, pin)

        self.accounts.append(account)   # LIST mein add ho raha hai
        return account

    def find_account(self, account_no):
        
        account_no_str = str(account_no).strip()

        if not account_no_str.isdigit():
            return None

        account_no_int = int(account_no_str)

        for account in self.accounts:
            if account.account_no == account_no_int:
                return account

        return None

    def list_all_accounts(self):
        
        if not self.accounts:
            print("No accounts found in the system.")
            return

        print(f"{'Acc No':<8}{'Name':<20}{'Type':<12}{'Balance':>12}")
        print("-" * 52)
        for account in self.accounts:
            print(
                f"{account.account_no:<8}{account.holder_name:<20}"
                f"{account.account_type:<12}{account.balance:>12.2f}"
            )
