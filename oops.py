#========================================OOPS-CLASS&OBJECTS======================================
class Roomates:
    def __init__(self,name,age,balance):
        self.name=name
        self.balance=balance
        self.age=age
    def deposite(self,amount):
        self.balance+=amount
priyan=Roomates("priyan",20,450)
hari=Roomates("hari",19,4000)

hari.deposite(1000)

    