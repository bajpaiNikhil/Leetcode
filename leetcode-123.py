from collections import Counter
n,k=[1, 3, 1, 5, 4],0
l=[]
count=0
d=dict(Counter(n))
print(d)

for key,val in d.items():
    if k>0:
        if k+key in d.keys():
            count+=1
    elif k==0:
        if val >=2:
            count+=1
    else:
        print(0)

print(count)

