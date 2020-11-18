n=[2,2]
k,t=3,0
for i in range(len(n)):
    for j in range(len(n)):
        #print(i-j)
        print(abs(n[i]-n[j]),abs(i-j))
        if i-j<=k and abs(n[i]-n[j])<=t and i!=j:
            print(True)
        else:
            continue
print(False)