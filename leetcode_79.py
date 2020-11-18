n=[1,1,0,1,1,1]
count=max_count=0
for i in range(len(n)):
    #print(n[i])
    if n[i]==1:
        count+=1
        max_count=max(count,max_count)
    else:
        count=0
print(max_count)

