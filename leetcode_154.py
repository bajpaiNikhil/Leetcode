
m=[1,4,2,5,3]

summ=0
n=len(m)
for i in range(1, n+1, 2):
    for j in range(n-i+1):
        #print(j)
        #print(m[j],j,m[j:j+i])
        summ+= sum(m[j:j+i])
        #print(summ)
print(summ)
