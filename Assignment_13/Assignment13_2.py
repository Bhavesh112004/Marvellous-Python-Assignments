class BankAccount:

    ROI = 10.5
    Years = 5
   
    def __init__(self,N,A):
        self.Name = N
        self.Amount = A

    def Deposit(self,amount):
        self.Amount = self.Amount + amount
        
    def Withdraw(self,withdraw):
        self.Amount = self.Amount - withdraw
        
    def CalculateInterest(self):
        result = (self.Amount * self.Years * self.ROI)/100
        self.Result = result

    def Display(self):
        print("The final amount after deposit and withdrawal is : ",self.Amount)
        print("The Interest Earned on this amount is : ",self.Result)

def main():

    Account_name = str(input("Enter the Name of an Account : "))
    Account_balance =int(input("Enter the initial amount in bank : "))
    Deposit_amount = int(input("Enter the amount to deposit : "))
    Withdraw_amount = int(input("Enter the amount to withdraw : "))

    C= BankAccount(Account_name,Account_balance)

    C.Deposit(Deposit_amount)
    C.Withdraw(Withdraw_amount)
    C.CalculateInterest()
    C.Display()

if __name__ == "__main__":
    main()