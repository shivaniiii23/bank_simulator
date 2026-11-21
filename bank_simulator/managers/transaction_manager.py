
import random
from datetime import datetime


class TransactionManager:
    

    def __init__(self):
        self.transactions = []   
    @staticmethod
    def generate_transaction_id():
        return f"TXN{random.randint(1000, 9999)}"

    def log_transaction(self, account_no, txn_type, amount, balance_after):
       
        txn_id = self.generate_transaction_id()

        record = {                       
            "txn_id": txn_id,
            "account_no": account_no,
            "type": txn_type,
            "amount": amount,
            "balance_after": balance_after,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self.transactions.append(record)  
        
        return txn_id

    def get_statement(self, account_no, limit=10):
        
        account_txns = []
        for txn in self.transactions:
            if txn["account_no"] == account_no:
                account_txns.append(txn)

        return account_txns[-limit:][::-1]
