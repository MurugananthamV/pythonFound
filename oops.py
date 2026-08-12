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
# class Student:
#     dep="BE Computer Science and Enigineering"
#     def __init__(self,name,reg,dob):
#         self.name=name
#         self.reg=reg
#         self.dob=dob    
# while True:
#     name=input("ENTER YOUR NAME:")
#     slc=input(f"hi {name},Do you wan to creat your object(yes/no):")
#     if slc.lower()=="yes":
#         name=input("ENTER YOUR NAME:")
#         reg=input("ENTER YOU REG NO:")
#         dob=input("ENTER YOUR DOB:")
#         st=Student(name,reg,dob)
#         print(f"HI DEAR {name},YOUR DETAILES WILL SUCCESFULLY SAVED")
#         sc=input("Do you want to see your deatils(yes/no):")
#         if sc.lower()=="yes":
#             print(f"Student Name:{st.name}\nRegister No:{st.reg}\nDate of Birth:{st.dob}")
#         else:
#             print(f"THANK YOU! {name}")
#             break
#     elif slc.lower()=="no":
#         print(f"THANK YOU! {name}")
#         break
#     else:
#         print("PLEAS ENTER VALID OPTION(yes/no):")
#
#
#======================CLASS ATRiBUte AND INSTANCE ATTRIBUTE===================
# class uk:
#     nam="uk"# class atribute
#     def __init__(self,name):
#         self.name=name#instance attribute
# a=uk("kumaran")
# b=uk("ananth")
# c=uk("murugan")
# uk.nam="london"#instamce attribute specifically for a object
# a.nam="Edinburg"#class attribute common for all object
# print(a.nam)
# print(b.nam)
# print(c.nam)
#
#
#=====================INSTANTIATION===========================================
#process of creating object from a clas


# class cars:
#     def __init__(self,name,model,power):
#         self.name=name
#         self.model=model
#         self.power=power
#         self.odometer=0
#     def drive(self,miles):
#         self.odometer=self.odometer+miles
#         print(f"you drove {miles} miles. so total: {self.odometer} miles.")

# #creating a obeject frm class

# car1=cars("toyota","corolla",800)#object one
# car2=cars("honda","civic",1000)#object 2
# car3=cars("porch","8090",1300)#object 3

# #access attributes and methods

# car1.drive(300)
# car2.drive(125)
# car3.drive(1200)

# print(car1.odometer)
# print(car2.odometer)
# print(car3.odometer)

# print(car1)
# print(car2)
# print(car3)

# #

# =====================PRINT THE OBJECT==========================
# =======STRING REPRESENTATION __srt__,__repr__===================
# class cars:
#     def __init__(self,name,model,power,id):
#         self.name=name
#         self.model=model
#         self.power=power
#         self.id=id
#     def drive(self,miles):
#         self.odometer=self.odometer+miles
#         print(f"you drove {miles} miles. so total: {self.odometer} miles.")
#     def __str__(self):#to represent the object to user
#         return f"{self.name} {self.model} {self.power} {self.id}"
#     def __repr__(self):
#         return f"name : '{self.name}','{self.model}','{self.power}',{self.id}"
# #__repr__--used to rpresent data to user and goive the data to developer to debugg and 
# #'{}'--is only show for user but if we use {}--is on;ly show for developers
# car1=cars("toyota","corolla",800,345678)#object one
# car2=cars("honda","civic",1000,456783)#object 2
# car3=cars("porch","8090",1300,456783)#object 3

# print(car1)
# print(repr(car3))

#
#
#
#======================CREATING WETHOD INSIDE THE CLASS===============
#======INSTANCE(self)
#======CLASS (@classmethod)(cls)
#======STATIC
#
#
#Alternative Constructor
# class student:
#     def __init__(self,name,id,dep):
#         self.name=name
#         self.id=id
#         self.dep=dep
#     @classmethod#CLASS METHOD
#     def string(cls,data):
#         name,id,dep=data.split("-")
#         return cls(name,id,dep)
#     def changename(self):#INSTANCE METHOD
#         self.name=input("Enter name:")
#         self.id=input("enter your id:")
#         self.dep=input("enter your dep:")
#     def __str__(self):
#         return f"""
#         Student Name : {self.name}
#         ID No        : {self.id}
#         Department   : {self.dep}
# """
#     @staticmethod
#     def result(a,b,c,d,e):
#         t=a+b+c+d+e
#         r=t/5
#         return r


# s=student.string("Muruganantham-066-CSE")
# # s.changename()
# print(student.result(87,67,90,80,60))
# print(s)

#
#
#
#