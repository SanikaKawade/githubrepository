# Class Definition
class BankAccount:

    # Class variable
    ROI = 10.5   # Rate of Interest

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display account details
    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Current Balance: {self.Amount}")
        print("---------------------------")

    # Deposit amount
    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Amount += deposit_amount
        print("Amount deposited successfully.")

    # Withdraw amount
    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance. Withdrawal not allowed.")

    # Calculate Interest
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


# Creating multiple objects
obj1 = BankAccount("Sanika", 5000)
obj2 = BankAccount("Rahul", 10000)

# For first account
print("Operations for First Account")
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1