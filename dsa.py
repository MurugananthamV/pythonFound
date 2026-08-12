#===============Patern 1===============
# def pat(n):

    # ========pattern one=====
    # for i in range(1,n+1):
    #     for j in range(i):
    #         print("*",end="")
    #     print()
    # =========pattern two=====
    # for i in range(1,n+1):
    #     for j in range(1,i+1):
    #         print(j,end="")
    #     print()
    # =======pattern 3========
    # printval=0
    # for i in range(1,n+1):
    #     if i%2==0:
    #         printval=0
    #     else:
    #         printval=1
    #     for j in range(1,i+1):
    #         print(printval,end="")
    #         printval=1-printval
    #     print()
    #========pattern four========



# pat(5)

def anagram(st,st1):
    # if sorted(st)==sorted(st1):
    #     print("True")
    # else:
    #     print("false")
    if Counter(st)==Counter(st1):
        print("True")
    else:
        print("false")
    
anagram("listen","silentt")