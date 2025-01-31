import time

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, txn_type, amount, address=None, sender=None, receiver=None):
        """
        Add a transaction to the history.

        :param txn_type: Type of transaction ("Send" or "Receive").
        :param amount: Amount of BTC for the transaction.
        :param address: Wallet address (only for "Send" transactions).
        :param sender: Sender wallet address (for "Send" transactions).
        :param receiver: Receiver wallet address (for "Receive" transactions).
        """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        transaction = {
            "type": txn_type,
            "amount": amount,
            "timestamp": timestamp,
            "address": address if txn_type == "Send" else None,
            "sender": sender if txn_type == "Send" else None,
            "receiver": receiver if txn_type == "Receive" else None
        }
        self.transactions.append(transaction)

    def display_transactions(self):
        """
        Display all transactions in a formatted way.
        """
        if not self.transactions:
            print("No transactions found.")
            return

        print(f"{'Type':<10} {'Amount (BTC)':<15} {'Sender':<40} {'Receiver':<40} {'Timestamp':<20}")
        print("-" * 120)
        for txn in self.transactions:
            sender = txn['sender'] if txn['sender'] else "N/A"
            receiver = txn['receiver'] if txn['receiver'] else "N/A"
            print(f"{txn['type']:<10} {txn['amount']:<15.8f} {sender:<40} {receiver:<40} {txn['timestamp']:<20}")
