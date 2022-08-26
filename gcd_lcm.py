#eclid algo for gcd calculation
#TC= O(log(min(n,m)))

#for lcm  : product=lcm*gcd
#lcm=product//gcd

from math import prod


def gcd(n,m):
    if n==0:
        return m
    return gcd(m%n,n) #function calls recursively

def lcm(n,m):
    prod=n*m
    hcf=gcd(n,m)#called upper function in below function
    return prod//hcf


t=int(input())#to take number of test cases
while t:
    n,m=map(int,input().split())
    #Using map we can call a single function many times
    print(gcd(n,m))
    print(lcm(n,m))
    t=t-1