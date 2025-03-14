class bank:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"current balance{self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"current balance{self.balance}")
        else:
            print("insufficient balance")
obj1=bank()
obj1.deposit(1000)
obj1.withdraw(500)
