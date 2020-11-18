



n=[7,5,5,8,3]
m=8
p=[i for i in range(1,m+1)]

l=[]
for i in range(len(n)):
    e=p.index(n[i])
    f=p[e]

    #print(p.index(n[i]),n[i])
    l.append(p.index(n[i]))
    p.remove(n[i])
    p.insert(0,f)
    #print(p)
print(l)