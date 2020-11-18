n=10

#t=str(n)
count=0
for i in range(0,n+1):
    t=str(i)

    if any([True if x in '347' else False for x in t]):
        continue

    if any([True if x in '018' else False for x in t]):
        continue
    count+=1
print(count)