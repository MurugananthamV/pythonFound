#=========================== return multiple values in function
#
# def kumaran(numbers):
#     return min(numbers),max(numbers)
# mn,mx=kumaran([3,24,4,7,8,3,7,8,4])
# print(f"minimum value is:{mn}",f"\nmaximum value is:{mx}")
#
#
#==========================use multiple returns
#
#
# def kumaran(a,b):
#     if b==0:
#         return None
#     return a/b
# print(kumaran(12,0))
# print(kumaran(12,3))
#
#
#==========================TYPES OF SCOPE IN PYRHON(LOCAL,GLOBAL,BUILT IN,ENCLOSING)-==============================
#
# k="Global Scobe Variable"
# def outer_function():
#     k="Outer function scope"
#     def inner_function():
#         k="inner Local scoe"
#         print(k)
#     inner_function()
#     print(k)
# outer_function()
# print(k)
#
#
# def add_item(item, items=None):
#     if items is None:
#         items=[]
#     items.append(item)
#     return items
#
#
#=================================Force caller to use parameter name
#
#use"/" after variables it for ce to give the value without keword for the "/"before accuring variables 
#use "*"before variable start it force to give value with keyword after * variables
#
#
#
# def student_db(name,/,dob,*,mark1,mark2):
#     t=mark1+mark2
#     return {"Name":name,"DOB":dob,"Total mark":t}
# print(student_db("kumaran","21-10-2005",mark1=98,mark2=78))
#
#
#
#=======*args and **kwargs=========
#
#
#
# def kumaran(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# kumaran(name="kumaran",age=21,ed="BE")
# def kumaran(*args):
#     print("sum of tuple:",sum(args))
# kumaran(1,2,3,4,5)
#
#==============PACKING AND UPACKING
# #
# def add3(a, b, c):
#     return a + b + c

# nums = [1, 2, 3]
# print(add3(*nums))

# data = {"a": 1, "b": 2, "c": 3}
# print(add3(**data))
#
#
#==================LMBDA FUNCTION
#
# age=lambda dob:2026-dob
# print(age(2005))
#
#
#================================HIGHER ORDER FUNCTION+=================================
#==========USE FUNCTIONS AS A ARGUMENT==================================================
# def add(a):
#     a=a+a
#     return a
# def new(add,value):
#     return add(value)
# print(new(add,20))
#
#
#============BUILT IN HIGHER ORDER FUNCTION==============
#
#
#
# lis=[1,2,3,4,5,6,7,8,9,10]
# #       
# sq=list(map(lambda x:x**2,lis))
# #
# ev=list(filter(lambda x:x%2==0,lis))
# #
# from functools import reduce
# total = reduce(lambda a,b:a+b,lis)
# print(sq)
# print(ev)
# print(total)
#
#
#==================Return function==============
# def outer(mul):
#     def inner(num):
#         return num*mul
#     return inner
# a=outer(2)
# b=outer(5)
# print(a(5))
# print(b(5))
#
#
#========================BANK BALANCE MANAGEMENT SMALL ROGRAMM ========================
#USING nonlocal to mofdify enclosing function variable
#Using Closure.
# def bank(balance):
#     def dep(amount):
#         nonlocal balance
#         balance=amount+balance
#         return balance
#     def wit(amount):
#         nonlocal balance
#         if balance<amount:
#             return "innuficient balance"
#         balance=balance-amount
#         return balance
#     return dep,wit
# deposite,withdraw=bank(1500)
# print(deposite(240))
# print(withdraw(570))
#
#==========================DECORATORS==================================================
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)
        print("After the function runs")
        return result
    return wrapper
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Ravi")