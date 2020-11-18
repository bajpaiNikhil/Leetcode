n=[5,1,2,3,4]
print(n)
N=sorted(n)
print(n)
count=0
for i in range(len(n)):
    if n[i]!=N[i]:
        count+=1

print(count)
