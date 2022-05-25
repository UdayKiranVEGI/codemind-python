s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=[]
for i in s1:
    if i.isalpha():
        if i in s2 and i not in a:
            a.append(i)
a.sort()
if len(a)==0:
    print(-1)
else:
    print(''.join(a))