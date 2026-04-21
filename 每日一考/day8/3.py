class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,val):
        self.__balance+=val
        print(f"充值成功，目前余额{self.__balance}")
    def withdraw(self,val):
        if self.__balance<val:
            print(f"余额不足！目前余额{self.__balance}")
        else :
            self.__balance-=val
            print(f"取款成功，目前剩余{self.__balance}元")
p1=BankAccount()
p1.deposit(15)
p1.withdraw(10)
p1.withdraw(10)