s="1101"
a=int(s,2)
print(a)
count=0
print(14%2,14//2)
while (a!=1):
    if a%2==0:
        count+=1
        a=a//2
    else:
        count+=1
        a=a+1
print(count)

