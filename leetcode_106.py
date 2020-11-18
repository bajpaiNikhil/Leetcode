n=[2,5,3,4,1]
count=0
for  i in range(len(n)):
    for j in range(i,len(n)):
        for k in range(j, len(n)):
            if ((n[i]<n[j] and n[j]<n[k]) or  (n[i]>n[j] and n[j]>n[k])):
                count+=1
print(count)