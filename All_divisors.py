
from math import *
def div1(n):#TC =O(root(n))
    sett=set()
    for i in range(1,int(sqrt(n))+1): #[1,root(n)]
        if n%i == 0:
            sett.add(i)
            sett.add(n//i)
    return list(sett)

#basic logic TC=O(n)
def div(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    return lst

t=int(input())
while t:
    n=int(input())
    print(div(n))# return the list 
    print(*div(n)) # it returns only values
    print(div1(n))
    t=t-1