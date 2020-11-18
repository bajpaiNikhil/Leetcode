n=[6]
a=sorted(n,reverse=True)
print(a)
#n.pop(0)
#print(n)
#l=[]
for i in range(1,len(a)+1):
    # print(a[:i],sum(a[:i]))
    # print(a[i:],sum(a[i:]))
    if sum(a[:i])>sum(a[i:]):
        print(a[:i])
        break
    else:
        continue