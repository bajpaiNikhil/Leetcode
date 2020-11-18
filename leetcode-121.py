n=[3,2,3,2,4]
print(n)
d=sorted(n)
print(d)
start,end=len(n),0

for i , j in zip(n,d):
    if i!=j:
        start=min(start,i)
        end=max(end,i)
print(end,start)


if end-start>=0:
    st = d.index(start)
    print(st)
    ed = d.index(end)
    print("len",len(d[st:ed])+1)
else:
    print(0)
print(len(n[start:end]))
#print(start-end >=0 ? end - start +1:0)






