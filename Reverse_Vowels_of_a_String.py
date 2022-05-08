s=input()
v='aeiouAEIOU'
a=[]
m=''
for i in s:
    if i in v:
        a.append(i)
a=a[::-1]
j=0
for k in range(len(s)):
    if s[k] in v:
        m=m+a[j]
        j+=1
    else:
        m=m+s[k]
print(m)