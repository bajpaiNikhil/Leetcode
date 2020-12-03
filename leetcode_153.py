

s="1+(2*3)/(2-1)"
d=0
res=0
for i in s:
    if i =="(":
        d+=1
        res=max(d,res)
    if i==")":
        d-=1
print(res)