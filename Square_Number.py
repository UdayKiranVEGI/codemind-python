def square(n):
    a=int(n*0.5)
    for i in range(1,a+1):
        if (i*i)==n:
            return True
    return False
n=int(input())
res=square(n)
print(res)