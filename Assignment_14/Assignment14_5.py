class BankAccount:

    def __init__(self,acc_no,name,balance):
        self.Account_number = acc_no
        self.Name = name
        self.Balance = balance

    def Deposit(self,dep_amo):
        self.Balance = self.Balance + dep_amo
        print("Balance after deposit : ",self.Balance)


    def Withdraw(self,with_amo):
        self.Balance = self.Balance - with_amo
        print("Balance after Withdrwal : ",self.Balance)


    def Display(self):
        print("The Final Balance of account : ",self.Balance)

def main():

    Obj = BankAccount(12345677,"Marellous",5400000)
    Obj.Deposit(100000)
    Obj.Withdraw(25000)
    Obj.Display()

if __name__ == "__main__":
    main()

