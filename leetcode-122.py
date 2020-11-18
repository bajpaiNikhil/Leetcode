n=3

prime=[True for i in range(n)]

p=2
count=0
while (p*p < n ):

    if prime[p]==True:

        for i in range(p*p,n+1,p):
            prime[i]=False
    p+=1

for i in range(2,n):
    print(prime[i])
    if prime[i]:
       count+=1
print(count)
