m=[1,2,3,4]
# d=[(x,y) for x,y in zip(myList, myList[1:])]
# print(d[0])
# print(str(d[0][1])*d[0][0])
# print(str(d[1][1])*d[1][0])
# print(d)
# print(len(d))

a=0
l=[]
while a<len(m)-1:
    l.extend([m[a+1]]*m[a])
    print(l)
    a+=2
print(l)


