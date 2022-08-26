def sum1(n):
    #TC = O(1)
    return (n)*(n+1)//2

def sum2(n):
    #TC=O(n)
    sum=0
    for i in range(1,n+1):  #[1,n]
        sum=sum+i
    return sum



#Code to take multi input and call the function for each value
t=int(input('enter the number of test cases'))
#t is number of test cases to be taken
while t:
    n=int(input())
    print(sum1(n))
    print(sum2(n))
    t=t-1