#========================================OOPS-CLASS&OBJECTS======================================
#
#
#
#
# class Roomates:
#     def __init__(self,name,age,balance):
#         self.name=name
#         self.balance=balance
#         self.age=age
#     def deposite(self,amount):
#         self.balance+=amount
# priyan=Roomates("priyan",20,450)
# hari=Roomates("hari",19,4000)
# priyan.deposite(300)
# hari.deposite(1000)
# hari.deposite(300)
#
# print(hari.balance)
# print(priyan.balance)
#
#===================================CLASS ATRIBUTE and INSTANCE ATTRIBUTE==========================
class Student():
    dep="BE Computer Science and Enigineering"
    def __init__(self,name,reg,dob):
        self.name=name
        self.reg=reg
        self.dob=dob    
while True:
    name=input("ENTER YOUR NAME:")
    slc=input(f"hi {name},Do you wan to creat your object(yes/no):")
    if slc.lower()=="yes":
        name=input("ENTER YOUR NAME:")
        reg=input("ENTER YOU REG NO:")
        dob=input("ENTER YOUR DOB:")
        st=Student(name,reg,dob)
        print(f"HI DEAR {name},YOUR DETAILES WILL SUCCESFULLY SAVED")
        sc=input("Do you want to see your deatils(yes/no):")
        if sc.lower()=="yes":
            print(f"Student Name:{st.name}\nRegister No:{st.reg}\nDate of Birth:{st.dob}")
        else:
            print(f"THANK YOU! {name}")
            break
    elif slc.lower()=="no":
        print(f"THANK YOU! {name}")
        break
    else:
        print("PLEAS ENTER VALID OPTION(yes/no):")

        
    

