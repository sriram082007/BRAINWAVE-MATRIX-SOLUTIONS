class ATM:
    def _init_(self, user_pin, balance=0):
        self.user_pin = user_pin
        self.balance = balance

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            pin = input("Enter your 4-digit PIN: ")
            if pin == self.user_pin:
                print("Authentication successful!\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. {attempts} attempts remaining.")
        print("Too many incorrect attempts. Card blocked.")
        return False

    def show_menu(self):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-4.")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: $"))
            if amount > 0:
                self.balance += amount
                print(f"${amount:.2f} deposited successfully.")
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount: $"))
            if amount > self.balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                self.balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")


if _name_ == "_main_":
    
    atm = ATM(user_pin="1234", balance=500.00)

    if atm.authenticate():
        atm.show_menu()
