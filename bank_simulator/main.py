
from managers.bank_manager import BankManager
from managers.transaction_manager import TransactionManager
from utils.validators import validate_pin, validate_name, is_valid_number


def print_header(title):
    print("\n" + "=" * 45)
    print(title.center(45))
    print("=" * 45)


def create_account_flow(bank_manager):
    print_header("Create New Account")

    acc_type = input("Account Type (savings/current): ").strip().lower()
    while acc_type not in ("savings", "current"):
        print("Invalid type. Please enter 'savings' or 'current'.")
        acc_type = input("Account Type (savings/current): ").strip().lower()

    name = input("Customer Name: ").strip()
    while not validate_name(name):
        print("Invalid name. Use letters and spaces only.")
        name = input("Customer Name: ").strip()

    deposit_input = input("Initial Deposit Amount: Rs. ").strip()

    if is_valid_number(deposit_input) and float(deposit_input) > 0:
        deposit = float(deposit_input)

        pin = input("Set a 4-digit PIN: ").strip()
        while not validate_pin(pin):
            print("PIN must be exactly 4 digits.")
            pin = input("Set a 4-digit PIN: ").strip()

        account = bank_manager.create_account(name, deposit, pin, acc_type)
        print(f"\nAccount created successfully!")
        print(f"Your Account Number is: {account.account_no}")
        print("Please save this number - you will need it to log in.")
       
    else:
        print("Invalid amount. Account creation cancelled.")


def account_session(account, bank_manager, txn_manager):
    while True:
        print_header(f"Welcome, {account.holder_name}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Mini Statement")
        print("5. Transfer Money")
        print("6. Logout")

        choice = input("Enter choice: ").strip()

        match choice:
            case "1":
                amount_input = input("Enter deposit amount: Rs. ").strip()

                if is_valid_number(amount_input):
                    amount = float(amount_input)
                    success, message, new_balance = account.deposit(amount)

                    if success:
                        txn_manager.log_transaction(account.account_no, "Deposit", amount, new_balance)
                        print(f"Deposit successful. New Balance: Rs. {new_balance:.2f}")
                    else:
                        print(f"Error: {message}")
                else:
                    print("Error: Amount must be a valid number")

            case "2":
                amount_input = input("Enter withdrawal amount: Rs. ").strip()

                if is_valid_number(amount_input):
                    amount = float(amount_input)
                    success, message, new_balance = account.withdraw(amount)

                    if success:
                        txn_manager.log_transaction(account.account_no, "Withdraw", amount, new_balance)
                        print(f"Withdrawal successful. New Balance: Rs. {new_balance:.2f}")
                    else:
                        print(f"Error: {message}")
                else:
                    print("Error: Amount must be a valid number")

            case "3":
                account.display_statement()

            case "4":
                records = txn_manager.get_statement(account.account_no)

                if not records:
                    print("No transactions found yet.")
                else:
                    print_header("Mini Statement")
                    for r in records:
                        print(
                            f"[{r['timestamp']}] {r['type']:<12} "
                            f"Rs. {r['amount']:.2f}  (Balance: Rs. {r['balance_after']:.2f})  "
                            f"TxnID: {r['txn_id']}"
                        )

            case "5":
                receiver_no = input("Enter receiver's Account Number: ").strip()
                receiver = bank_manager.find_account(receiver_no)

                if receiver is None:
                    print("Error: No account found with this account number")
                else:
                    amount_input = input("Enter amount to transfer: Rs. ").strip()

                    if is_valid_number(amount_input):
                        amount = float(amount_input)
                        success, message, sender_balance = account.withdraw(amount)

                        if success:
                            _, _, receiver_balance = receiver.deposit(amount)

                            txn_id = txn_manager.log_transaction(
                                account.account_no, "Transfer-Out", amount, sender_balance
                            )
                            txn_manager.log_transaction(
                                receiver.account_no, "Transfer-In", amount, receiver_balance
                            )

                            print(f"Transfer successful! Transaction ID: {txn_id}")
                            print(f"Your new balance: Rs. {sender_balance:.2f}")
                        else:
                            print(f"Error: {message}")
                    else:
                        print("Error: Amount must be a valid number")

            case "6":
                print("Logged out successfully.")
                break

            case _:
                print("Invalid choice. Please try again.")


def login_flow(bank_manager, txn_manager):
    print_header("Login")

    account_no = input("Enter Account Number: ").strip()
    account = bank_manager.find_account(account_no)

    if account is None:
        print("Error: No account found with this account number")
    else:
        pin = input("Enter PIN: ").strip()

        if account.verify_pin(pin):
            account_session(account, bank_manager, txn_manager)
        else:
            print("Error: Incorrect PIN entered")


def main():
    bank_manager = BankManager()
    txn_manager = TransactionManager()

    while True:
        print_header("Bank Simulator")
        print("1. Create New Account")
        print("2. Login to Existing Account")
        print("3. Admin: View All Accounts")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        match choice:
            case "1":
                create_account_flow(bank_manager)
            case "2":
                login_flow(bank_manager, txn_manager)
            case "3":
                print_header("All Accounts")
                bank_manager.list_all_accounts()
            case "4":
                print("\nThank you for using ABC Bank Simulator. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")



main()
