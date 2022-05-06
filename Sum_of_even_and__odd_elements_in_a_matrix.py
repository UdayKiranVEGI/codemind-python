n,m=map(int,input().split())
ev=0
od=0
for j in range(n):
    m=list(map(int,input().split()))
    for i in m:
        if i%2:
            od=od+i
        else:
            ev=ev+i
print(ev,od)