s="hellohello hellohellohello"
k="ell"
d=0
l=len(k)
f=s.split(" ")
for i in f:
    if k in i[0:l]:
        d=1+f.index(i)
        #print(d)
if d!=0:
    print(d)
else:
    print(-1)