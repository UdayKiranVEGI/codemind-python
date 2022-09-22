n=int(input())
arr=list(map(int,input().split()))
a=sum(arr)
if a%2==0 and n%2==0:
    c=0
    b=0
    for i in arr:
        if i%2:
            c+=1
        else:
            b+=1
    if c%2==0 and b%2==0:
        print(1)
    else:
        print(0)
else:
    print(0)