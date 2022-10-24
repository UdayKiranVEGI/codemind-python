s=input()
h=int(s[:2])
p=s[6:]
if p=='PM':
    if s[:2]=='12':
        print('12:'+s[3:5])
    else:
        print(str(12+h)+':'+s[3:5])
else:
    if s[:5]=='12:00':
        print('00:00')
    else:
        print(s[:5])