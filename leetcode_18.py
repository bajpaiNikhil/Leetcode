

s="()()"

#print(s)
l,r=0," "
for i in s:
    if i=="(":
        if l>0:
            r+=i
        l+=1
    else:
        l-=1
        if l>0:
            r+=i
print(r)