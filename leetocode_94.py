from collections import Counter
n="dddccdbba"
d=dict(Counter(n))
print(d)
count=0
for key,val in d.items():
    if val==1:
        #print(list(d.keys()).index(key))
        print(n.index(key))
        count+=1
        break
    else:
        pass
#print(count)
if count!=0:
    pass
else:
    print(-1)