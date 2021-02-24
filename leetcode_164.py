




n="00110011"

l=[]
for i in n.replace("10","1 0").replace("01","0 1").split(" "):
    l.append(len(i))
sum=0
for a,b, in zip(l,l[1:]):
    sum+=min(a,b)
print(sum)
