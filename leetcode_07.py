a=[555,901,482,1771]
count=0
for i in range(len(a)):
    a[i]=str(a[i])
#print(a)
for i in a:
    c=len(i)
    #print(c)
    if c%2==0:
        count=count+1
print(count)


