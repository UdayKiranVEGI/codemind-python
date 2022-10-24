n=int(input())
k=0
for i in range(n):
    s=input()
    if '++'==s[:2] or '++'==s[1:]:
        k+=1
    elif '--'==s[:2] or '--'==s[1:]:
        k-=1
print(k)