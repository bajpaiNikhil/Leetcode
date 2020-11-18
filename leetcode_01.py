n=[3,2,4]
target=6

for i in range(len(n)):
    for j in range(i+1,len(n)):
        value=n[i]+n[j]
        #print(value)

        if value==target:
            print(i,j)
            break