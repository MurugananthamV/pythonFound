
# -------------------------------------functiones------------------------------
# -------------------------------------format()--------------------------
# n=int(input())
# n2=input()
# print("number is {} name is {}".format(n,n2))

# -------------------------------------math functioms()------------------
# import math
# print(math.factorial(5))
# print(math.gcd(23,8))
# print(math.sqrt(45))
# print(math.pow(3,6))
# ---------------------------------------------------------------------------List-----------------------------------------------------------get input
# l=[12,34,3,32,34,67,3,6,78,66]
# # n=int(input())
# for i in range(n):
#     n1=input()
#     l.append(n1)
# print(l)
# l.insert(2,"jhgf") #insert function=-----------------
# l1=[32,"sd",23] 
# l.extend(l1)#for merge the two list------------------
# l.remove(12)#remove by actual value------------------
# l.pop(2)#pop by index value--------------------------
# l.reverse()# for reverse the lis---------------------
# l.sort()#sort the list in assending order------------
# print(max(l))
# print(min(l))
# print(l)
#------------------------------------------------------to print the evn number and odd number in a list------------------------------------------------
# list=[4,324,56,56,33,873,45,345,2,1,2,23,5,6]
# odd=[]
# evn=[]
# for i in list:
#     if i%2==0:
#         odd.append(i)
#     else:
#         evn.append(i)
# print("odd numbers are:",odd)
# print("even numers are:",evn)

#-------------------------------------find common elemnt between two lists-----------------------------------------------------------------------------
# lst1=[1,3,5,7,9,2,2,4,6,8]
# lst2=[2,4,6,8,10,3,5,7,9,9,]
# com=[]
# for i in lst1:
#     found=0
#     for k in com:
#         if i==k:
#             found=1
#             break
#     if found==0:
#          for j in lst2:
#             if i==j:
#                 com.append(i)
# print(com)
# #----------------------------------find all pairs whoes sum eales a given number------------------------------------------------------------------------

# lst=[1,2,3,4,5,6,7,8,9,2,5]
# target=6
# paires=[]
# for i in lst:
#     for j in lst:
#         if i+j==target:
#             paires.append("{} : {}".format(i,j))
# print("the paires are:",paires)

#-----------------------------------write a programm to print the minimum number of swap required to sort the array-----------------------------------------
# lst=[8,5,3,7,9,3,6]
# count=0
# for i in range(len(lst)):
#     min=i
#     for j in range(i+1,len(lst)):#2
#         if lst[j]<lst[min]:#2,1
#             min=j

#     if min!=i:
#         lst[i],lst[min]=lst[min],lst[i]
#         count=count+1
# print(lst)
# print(count)
#
#
#-------------------------------------------------------------list comprehension---------------------------------kis
# list=["beautifull","tamil","ppor","loke"]
# lent=[len(h) for h in list]
# print(lent)
#
#
#
#       
#-----------------------------------set--------------------------------------------------------------------------
#set stors only uniqe element ,it remoeve dublicate elments.
#
# s=set()
# s.add(34)
# s.update([1,23,6,7,67,5,23])
# s.update("Kumaran")
# s.remove(6)
# s.discard(7)
# s.pop()#for remove first element
# print(s)
#
#
#
# s1={1,2,3,4,5,6,7,8,9}
# s2={5,6,7,8,9,10,11,12}
# print(s1.union(s2))
# print(s2|s1)#unione
# print(s1.intersection(s2))
# print(s2&s1)#intersection
# print(s1.difference(s2))
# print(s2-s1)#difference
# print(s1.symmetric_difference(s2))#different elemnts in both sets
# print(s1^s2)#symmetric diference
#
#
#
#================FIND THE COMMEN ELEMNTS BETWEEN THREE LIST=====================
#
#
# s1=[1,2,3,5,6,7,]
# s2=[4,6,8,9,4,2,3]
# s3=[12,43,7,2,4,2,4,2,3]
# l=[]

# for i in s1:
#     if i in s2 and i in s3:
#         l.append(i)
# print(l)
#
#
#

#==================FIND THE COMMONE ELEMENTS BETWEEN THREE SETS=====================
# s1=[1,2,3,5,6,7,]
# s2=[4,6,8,9,4,2,3]
# s3=[12,43,7,2,4,2,4,2,3]
# R=set(s1)&set(s2)&set(s3)
# print(R)

#==================FUNCTIONES IN SET=================================================

# s={1,2,3,4,5,6,7,8}
# print(len(s))
# print(max(s))
# print(min(s))
# print(sum(s))
# print(sorted(s))
#
#
#
#
# s=["abc","bac","cab","xyz","yzx","xzy"]
# v=set()
# for i in range(len(s)):
#     if s[i] in v:
#         continue
    
#===========================================Dictionary=====================================================
# dic={"key":"value} ===one key have only one value
# d={"name":"kumaran","age":21,"place":"tnj"}
# #for print the values
# for i in d.values():
#     print(i,end="-")
# print()
# #for print the key's only
# for i in d:
#     print(i,end="_")
# print()
# #for print the both key and value
# for i,j in d.items():
#     print(i,":",j,end=" ")
# print()

#=====================FUNCTIONS=================================
#dict.fromkeys(key,valuse)
# d=["age","name","city"]
# d1=dict.fromkeys(d)
# print(d1)
# #string to dictionary
# s="ABCD"
# d2=dict.fromkeys(s,1)
# print(d2)
# # Set as a dictionary
# set={"age","name","city"}
# val="nothing"
# d3=dict.fromkeys(set,val)
# print(d3)
# val1=[1,2]
# d4=dict.fromkeys(set,val1)
# print(d4)
# newdic=d.copy()# for copy the dictionary
# print(newdic)
# print(d.keys())#fro printkeys only in the dictionary
#=============================PRINT THE FREQUENCY OF THE EACH WORD===================================
# s="python language is easy and pyhton is powerfull programming language"
# l=s.split()
# dic={}
# for i in l:
#     if i in dic:
#         dic[i]=dic[i]+1
#     else:
#         dic[i]=1
# print(dic)
# d["age"]=d["age"]+1
# print(d)
#=======================REMOVE THE DUBLICATE VALUES IN THE DICTIONARY===============================

# d={"name":"kumaran","age":21,"age":21,"name":"kumaran","place":"tnj"}
# dub={}
# org={}
# for i,j in d.items():
#     a=i,":",j
#     if a in dub:
#         continue
#     else:
#         print(a,end=" ")
#===========================REMOVE THE DUBLICATE VALUES IN THE DICTIONARY 2=========================

# d={"a":10,"b":10,"c":20,"d":20,"e":30,"f":30}
# v=[]
# org={}
# for i in d:#i=a,b,c,d,,,
#     if d[i] not in v:#d[i]means =10
#         org[i]=d[i]#means org[a]=10 so org become {"a":10}
#         v.append(d[i])#it add the reapeated value to list===v[10,20,30]
# print(org)

#==========================PRINT KEYS ,THAT TO GET THE TRAGET FORM THE SUM OF KEYS==================================
# d={"a":10,"b":20,"c":30,"d":40,"e":50,"f":60}
# t=50
# keys=list(d.keys())
# for i in range(len(keys)):
#     for j in range(i+1,len(keys)):
#         if d[keys[i]]+d[keys[j]]==t:
#             print(keys[i],"+",keys[j])

#==========================NEED TO CORRECT SOME ERRORES============


# lst=int(input())
# l=lst.split()
# frq={}
# for i in lst:
#     if i in frq:
#         frq[i]=frq[i]+1
#     else:
#         frq[i]=1
# print(frq)
# items=list(frq.items())
# print(items)
# for i in range(len(items)):
#     for j in range(i+1,len(items)):
#         if items[i][1]<items[j][1]:
#             items[i],items[j]=items[j],items[i]
# for i,j in items:
#     print(i,j)

#===============================
# str="apple car ball ant bus banana cat dog duc"
# st=str.split()
# group={}
# for i in st:
#     fst=i[0]
#     if fst in group:
#         group[fst].append(i)
#     else:
#         group[fst]=[i]
# print(group)
#
#
#
#=========================================FUNCTIONS================================
#
#
#FUNTION IS THE SET OF CODE THAT IS REUSABLE
#DEVIDING THE JOB INTO MANAGABLE STEPS
#
#=======SYNTEX
# def function_name(parameters):#multiple parameters separated by {,}
#   statement....
#
#========HOW TO CALL FUNION
#function_name()
#
#
#=======================================EXAMPLE FUNCTION PROGRAMM===============================
# def name():
#     n=input()
#     print("Hello!",n)
# name()
#=======================
# def add(a,b):
#     print(a+b)
# add(29,876)
#========================Check weather the number is odd or evne============================
#
#
# def check(num):
#     if num%2==0:
#         print("the number {} is even".format(num))
#     else:
#         print("the number {} is odd".format(num))
# check(23)
# check(2)
# check(4)
#
#
#======================FIND THE LARGEST NUMBER IN THE GIVEN TWO NUMBERS =======================
# def lar():
#     a=int(input())
#     b=int(input())
#     if a>b:
#         print("{} is largest Number".format(a))
#     else:
#         print("{} is largest Number".format(b))
# lar()
#
#==================FIND THE FACTORIUAL OF A GIVEN NUMBER=============================
# def fact(num):
#     n=1
#     for i in range(1,num+1):
#         n=n*i
#     print(n)
# fact(6)
# fact(5)
#
#
#====================DEFFERENCE BETWEEN PRINT AND RETURN STATEMENT===================
#
#
#
#
# def find_max(a):
#     largest=a[0]
#     for i in a:
#         if i>largest:
#             largest=i 
#     return largest
# a=[1,2,3,44,55,666,87]
# result=find_max(a)
# print(result)
#
#
#======================SUM OF DIGITE=====================
#
# def digit(num):
#     string=str(num)
#     maxi=0
#     for i in string:
#         maxi=maxi+int(i)
#     return maxi
# n=int(input())
# print(digit(n))
#===============
# def cus_det(cus_id,cus_name):
#     print("Customer Name:",cus_name)
#     print("Customer ID:",cus_id)
#     return

# cus_det(cus_id="066",cus_name="Kumaran")
#
#
#
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(4))
#
#
#
#==========================================================Collections in Python=======================================
#==========================================Tuples in python=====================================
a=(1,2,3,[1,2,3,4],4,5,6,7,3,2,5,2,4,2)
# print(a.count(2))
# print(a.index(4))
# a[3].append(5)
# z,b,c,*d=a   #Unpacking in Tuples

#============================================Named Tuples=======================================
# data=("Kumaran",21,"CSE")
# from collections import namedtuple
# st=namedtuple("st",["Name","Age","Department"])
# student=st("Kumaran",21,"CSE")
# makedata=st._make(data)#Make As a Data
# dic=student._asdict()#For converting the tuple to dictionary
# rep=student._replace(Age=22)#Replace the value By Field
# print(student._fields)
# print(rep)
# print(dic)
# print(student)
# print(student.Name)
# print(student.Age)
# print(student.Department)

#===========================================Sets In python======================================
#set dont have dublicate values-it delete dublicate values automatically
# set={2,3,4,5,6}
# set2={1,2,3,0,9,7,8}
# set.add(8)
# set.update([1,9])#it store the valuse in accending order
# set.remove(9)
# set.discard(8)
# set.pop()#it remove the first value
# set.clear()#it empty the set
# print(set)

#=====================================Dictionay in Python==========================================
dic={"name":"kumaran","age":21,"dep":"CSE"}
# print(dic.get("name"))#Accessing the dictionary safe method
# dic["age"]=22#change the value
# dic.update({"name":"Tamil","age":"23"})#change the bulk value
#===============================removing=================
# del dic["age"]
# dic.pop("name")
# dic.clear()#empty dictionary
#==============================itration in dictionay===========
# for keys in dic:
#     print(keys,end=" ")#For print the keys in the Dictionary
# print()

# for value in dic.values():#for print the values onyly
#     print(value,end=" ")
# print()
#=================iterate using index=====================
# for index,(key,value) in enumerate(dic.items()):
#     print(index,key,value)
#==================iterate reverse order==================
# for key in reversed(list(dic.keys())):
#     print(key,":",dic[key])
#=================access values usng keys===================
for key in dic:
    print(f"{key}->{dic[key]}")

