n,m=map(int,input().split())
k=[-10000]*m
for i in range(n):
    a=list(map(int,input().split()))
    for i in range(m):
        if a[i]>k[i]:
            k[i]=a[i]
for i in k:
    print(i)