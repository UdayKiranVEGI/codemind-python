n=int(input())
if n>0:
    for i in range(1,n+1):
        print(' '*(n-i),end='')
        for k in range(1,2*i):
            print(i,end='')
        print()