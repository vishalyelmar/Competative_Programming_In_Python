mylist=[]
n=int(input())
sum=0
for i in range(0,n):
  ele=int(int(input()))
  mylist.append(ele)
for i in mylist:
  sum=sum+i
avg =sum/len(mylist)
print(avg)
print(min(mylist, key=lambda mylist:abs(avg-mylist)))


