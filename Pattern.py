n=int(input())
if n>0:
    for i in range(1,n+1):
        a=0
        print(' '*(n-i),end='')
        j=2
        for k in range(1,2*i):
            if k<=i:
                print(k,end='')
            else:
                print(k-j,end='')
                j+=2
        print()