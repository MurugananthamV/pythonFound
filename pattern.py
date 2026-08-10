
num=5
def pin(a):
    if a%2==0:
        return 1
    else:
        return 0
for i in range(num+1):
    n=print(pin(i))
    # for j in range(1,i):
    #     if j%2==0:
    #         print(0,end=" ")
    #     else:
    #         print(1,end=" ")
    #     print()