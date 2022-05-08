s=input()
v='aeiouAEIOU'
n='0123456789'
vow=0
con=0
dig=0
sp=0
for i in s:
    if i in v:
        vow+=1
    elif i in n:
        dig+=1
    elif ' ' in i:
        sp+=1
    else:
        con+=1
print('Vowels:',vow)
print('Consonants:',con)
print('Digits:',dig)
print('White spaces:',sp)