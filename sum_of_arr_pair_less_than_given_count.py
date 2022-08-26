n,k=map(int,input().split())
arr=[int(input()) for r in range(n)]
print(n,k)
print(*arr)
count=0
for i in range(n-1):
    if arr[i]+arr[i+1]<k:
        count+=1
        print(arr[i],arr[i+1])
print(count)