class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        """
        Initializes the bank account with the holder's name and an optional initial balance.
        """
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Current balance: ${self.balance:.2f}")


def main():
    """
    Entry point for the Bank Account Simulator program.
    """
    print("Welcome to the Bank Account Simulator!")
    account_holder = input("Enter the account holder's name: ").strip()
    account = BankAccount(account_holder)

    while True:
        print("\nChoose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == 3:
                account.check_balance()
            elif choice == 4:
                print(f"Goodbye, {account.account_holder}!")
                break
            else:
                print("Invalid choice. Please select an option between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
