class BankAccount:
     def __init__(self,name,balance):
          self.name = name # public 
          self.__balance = balance # private - data mangling
     def get_balance(self):
          return self.__balance
     
     def set_balance(self,newBalance): # setter
          self.__balance = newBalance
     
     
acc1 = BankAccount("Abhishek Singh",100_000)
acc1.set_balance(20_000)
print(acc1.name,acc1.get_balance())
# we can get the private in another way too 
print(acc1.name,acc1._BankAccount__balance)
