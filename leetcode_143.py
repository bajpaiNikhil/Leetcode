



A=[3,2,4,1]
solution = []
a=len(A)
for i in range(len(A)):
    current=max(A[0:a-i])
    #print(current)
    j=0
    while A[j]!=current:
        j+=1
    A[:j+1]=reversed(A[:j+1])
    solution.append(j+1)
    A[:a-i]=reversed(A[:a-i])
    solution.append(a-i)
print(solution)