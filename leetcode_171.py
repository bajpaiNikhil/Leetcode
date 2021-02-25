


n=[2,4,1,2,7,8]


n.sort(reverse=True)
print(n)
m=len(n)//3
ans=0
count=0
for i in range(1,len(n),2):
    if count<m:
        ans+=n[i]
        count+=1
    else:
        break
print(ans)

