s=input()
a=s.split()
a.sort()
b,c=[],[]
for i in a:
    b.append(len(i))
b.sort()
for j in b:
    for k in range(len(b)):
        if len(a[k])==j:
            c.append(a[k])
            a.pop(k)
            break
print(*c)