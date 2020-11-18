


from collections import  Counter
n=[1,9]


d=Counter(n)
# print(d)
k=len(n)
f=list(d.values())
f.sort()
# print(f)
count=0
removecount=0
for i in reversed(range(len(f))):
    #print(i)
    count+=f[i]
    removecount+=1
    if count>=k//2:
        print(removecount)
        break