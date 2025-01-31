from wallet.transactions import TransactionManager
import random
import re
import time

class Wallet:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        self.transaction_manager = TransactionManager()

    def display_balance(self):
        """
        Display the current wallet balance.
        """
        print(f"{self.name}'s Wallet Balance: {self.balance:.8f} BTC")

    def validate_address(self, address):
        """
        Validate a Bitcoin wallet address.

        :param address: The wallet address to validate.
        :return: True if valid, False otherwise.
        """
        if re.match(r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,39}$', address):
            return True
        print("Invalid wallet address!")
        return False

    def send_bitcoin(self, amount, receiver_wallet, address):
        """
        Simulate sending Bitcoin to a wallet address.

        :param amount: Amount of Bitcoin to send.
        :param address: Receiver wallet address.
        :param receiver_wallet: The receiver's wallet instance.
        """
        if not self.validate_address(address):
            return False

        if amount > self.balance:
            print("Insufficient balance to send the transaction!")
            return False
        if amount <= 0:
            print("Invalid amount! Must be greater than 0.")
            return False

        # Deduct the balance from the sender
        self.balance -= amount
        # Add the balance to the receiver
        receiver_wallet.balance += amount

        # Record the transaction for sender
        self.transaction_manager.add_transaction("Send", amount, address=address, sender=self.name)
        # Record the transaction for receiver
        receiver_wallet.transaction_manager.add_transaction("Receive", amount, receiver=self.name)

        print(f"Transaction successful! Sent {amount:.8f} BTC to {address}.")
        return True

    def receive_bitcoin(self):
        """
        Simulate receiving a random amount of Bitcoin.
        """
        amount = round(random.uniform(0.01, 0.1), 8)  # Random BTC between 0.01 and 0.1
        self.balance += amount
        self.transaction_manager.add_transaction("Receive", amount)
        print(f"Transaction successful! Received {amount:.8f} BTC.")

    def show_transaction_history(self):
        """
        Display the transaction history.
        """
        print("\nTransaction History:")
        self.transaction_manager.display_transactions()

class WalletSimulator:
    def __init__(self):
        self.sender_wallet = Wallet("Sender", balance=1.0)  # Starting balance for sender
        self.receiver_wallet = Wallet("Receiver", balance=0.0)  # Starting balance for receiver

    def run(self):
        """
        Main loop to simulate wallet operations.
        """
        print("Welcome to the Bitcoin Wallet Simulator!\n")
        while True:
            self.sender_wallet.display_balance()
            self.receiver_wallet.display_balance()

            print("Options:")
            print("1. Send Bitcoin")
            print("2. Receive Bitcoin (Sender's wallet)")
            print("3. View Transaction History")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                try:
                    address = input("Enter recipient wallet address: ")
                    amount = float(input("Enter amount to send (BTC): "))
                    self.sender_wallet.send_bitcoin(amount, self.receiver_wallet, address)
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            elif choice == "2":
                self.sender_wallet.receive_bitcoin()
            elif choice == "3":
                self.sender_wallet.show_transaction_history()
                self.receiver_wallet.show_transaction_history()
            elif choice == "4":
                print("Exiting the Bitcoin Wallet Simulator. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
