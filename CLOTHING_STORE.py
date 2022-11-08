n=int(input())
a=list(map(int,input().split()))
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
c=0
for i in dic:
    c+=dic[i]//2
print(c)