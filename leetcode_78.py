n=[1,3,2,3,5,0]
l=[]
#print(l)
for i in range(len(n)):
    l.append(n[i]+1)

print(n)
print(l)
s=[i for i in l if i in n ]
print(s)
print(len(s))

