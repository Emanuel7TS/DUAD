class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def add_money(self):
        amount = float(input("Type how much money you want to add: "))
        self.balance += amount
        print(f"You've added {amount:.2f}. New balance: {self.balance:.2f}")

class Save_account(Account):
    def __init__(self, balance, minimum_balance):
        super().__init__(balance)
        self.minimum_balance = minimum_balance
    

    def withdraw_money(self):
        while True:
            try:
                withdraw = float(input("Type how much money you want to withdraw: "))

                if withdraw <= 0:
                    print("The amount must be greater than 0. Please try again.")
                    continue

                if self.balance - withdraw < self.minimum_balance:
                    print("You can't withdraw this amount, it will bring your balance below the minimum.")
                else:
                    self.balance -= withdraw
                    print(f"You've withdrawn {withdraw:.2f}. New balance: {self.balance:.2f}")
                    break

            except ValueError:
                print("Invalid input. Please enter a valid number.")

saving_account = Save_account(10000,100)

saving_account.add_money()
saving_account.withdraw_money()