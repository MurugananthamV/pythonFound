#===============Patern 1===============

class Solution:
    def pat(n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            print()
s1=Solution
s1.pat(5)