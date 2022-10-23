s=input()
vow='aeiou'
k='k'
for i in s:
    if i in vow:
        if k[-1]!='V':
            k+='V'
    else:
        if k[-1]!='C':
            k+='C'
print(k[1:])