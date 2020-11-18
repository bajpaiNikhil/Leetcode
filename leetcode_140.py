




n=[7,11,12,9,5,2,7,17,22]

count=0
for i in range(len(n)):
    xor=n[i]
    for j in range(i+1,len(n)):
        xor^=n[j]
        if xor==0:
            count+=j-i
print(count)