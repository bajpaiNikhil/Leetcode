







s1 = "kelb"
s2 = "kelb"

a=[]
b=[]
flag=0


n= len(s1)

for i in range(n):
    if s1[i]!=s2[i]:
        a.append(s1[i])
        b.append(s2[i])
print(a)
print(b)
if len(a)==len(b)==0:
    print(True)
if len(a)==len(b)==2:
    if a[0]==b[1] and b[0]==a[1]:
        print(True)
print(False)