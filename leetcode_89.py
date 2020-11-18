s="III"
romantoint={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
total=0
for i in range(len(s)-1):
    currentInt=romantoint[s[i]]
    nextInt=romantoint[s[i+1]]
    if nextInt:
        if currentInt >= nextInt:
            total+=currentInt
            #print(total,s[i])
            #continue
        else:
            #print(nextInt-currentInt)
            total+=(nextInt-currentInt)
            i=i+1
            #print(total,s[i])
    else:
        total+=currentInt
        #continue
    #print(currentInt,nextInt)
print(total)