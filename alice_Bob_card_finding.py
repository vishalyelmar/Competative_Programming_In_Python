
n=int(input())
lst=[]
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
#print(lst)
lst1=sorted(lst)
print(lst1)
card=int(input())
if card in lst1:
    print(lst1.index(card))

     
