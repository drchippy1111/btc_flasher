import random
import time
from rich.console import Console
from rich.table import Table

console = Console()

# Simulated wallet balance
wallet_balance = 1.0  # 1 BTC

def display_balance():
    console.print(f"[green]Wallet Balance:[/] {wallet_balance:.8f} BTC\n")

def send_bitcoin(amount):
    global wallet_balance
    if amount > wallet_balance:
        console.print("[red]Insufficient balance to send the transaction![/]")
        return False
    wallet_balance -= amount
    console.print(f"[blue]Transaction sent:[/] {amount:.8f} BTC")
    return True

def receive_bitcoin(amount):
    global wallet_balance
    wallet_balance += amount
    console.print(f"[green]Transaction received:[/] {amount:.8f} BTC")

def transaction_history(transactions):
    table = Table(title="Transaction History")
    table.add_column("Type", style="cyan", justify="center")
    table.add_column("Amount (BTC)", style="magenta", justify="center")
    table.add_column("Timestamp", style="yellow", justify="center")

    for txn in transactions:
        table.add_row(txn["type"], f"{txn['amount']:.8f}", txn["timestamp"])
    console.print(table)

def main():
    transactions = []
    console.print("[bold green]Bitcoin Wallet Simulator[/bold green]\n")

    while True:
        display_balance()
        console.print("1. Send Bitcoin")
        console.print("2. Receive Bitcoin")
        console.print("3. View Transaction History")
        console.print("4. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            amount = float(input("Enter amount to send (BTC): "))
            if send_bitcoin(amount):
                transactions.append({
                    "type": "Send",
                    "amount": amount,
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                })
        elif choice == "2":
            amount = round(random.uniform(0.01, 0.1), 8)
            receive_bitcoin(amount)
            transactions.append({
                "type": "Receive",
                "amount": amount,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            })
        elif choice == "3":
            transaction_history(transactions)
        elif choice == "4":
            console.print("[bold red]Exiting...[/bold red]")
            break
        else:
            console.print("[red]Invalid choice![/]")

if __name__ == "__main__":
    main()
