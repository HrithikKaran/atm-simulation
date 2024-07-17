import time

class BankAccount:
    def __init__(self, pin):
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return False
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: {amount}")
            return True

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: {amount}")

    def change_pin(self, new_pin):
        self.pin = new_pin

    def view_transactions(self):
        for transaction in self.transaction_history:
            print(transaction)

def login(account):
    attempts = 3
    while attempts > 0:
        pin = int(input("Enter your PIN: "))
        if pin == account.pin:
            print("Access granted.")
            return True
        else:
            attempts -= 1
            print("Wrong PIN. Attempts remaining:", attempts)
            if attempts == 0:
                print("Access denied. Exiting...")
                exit()
    return False

def execute_task(account):
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            print(f"Balance: Rs.{account.check_balance()}")
            time.sleep(5)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if account.withdraw(amount):
                print(f"Withdrew Rs.{amount}")
                print(f"New balance: Rs.{account.check_balance()}")
                time.sleep(5)
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print(f"Deposited Rs.{amount}.")
            print(f"New balance: Rs.{account.check_balance()}")
            time.sleep(5)
        elif choice == "4":
            new_pin = int(input("Enter new PIN: "))
            account.change_pin(new_pin)
            print("PIN changed successfully.")
            time.sleep(5)
        elif choice == "5":
            account.view_transactions()
            time.sleep(5)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    account = BankAccount(1234)  # Default PIN 1234
    if login(account):
        execute_task(account)
