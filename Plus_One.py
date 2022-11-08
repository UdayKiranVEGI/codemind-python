n=int(input())
a=list(map(int,input().split()))
#n=5
#a=[0,9,9,9,9]
c=0
a[n-1]=a[n-1]+1
for i in range(n):
    a[n-1-i]=a[n-1-i]+c
    c=0
    if a[n-1-i]>9:
        c=a[n-1-i]//10
        a[n-1-i]=a[n-1-i]%10
    if c==0:
        break
if c!=0:
    a.insert(0,c)
print(*a)