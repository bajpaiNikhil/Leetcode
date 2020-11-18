a=9669
l=list(map(int,str(a)))
for i in range(len(l)):
    print(l[i])
    if(l[i]==6):
        l[i]=9
        break
print(l)
b=int("".join(map(str,l)))
print(b)

