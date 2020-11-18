n,k=[1,0,0,0,1],1
count=0
m=len(n)

for i in range(m):
    if n[i]!='1' and( i=='0' and n[i-1]!='1') and (i==m-1 and n[i+1]!='0'):
        print(1)
        n[i]=1
        count+=1
    else:
        continue

print(n)
print(count)