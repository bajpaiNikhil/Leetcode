



s = "aba"
t = "baba"

ans=0
n=len(s)
m=len(t)
for i in range(n):
    for j in range(m):
        count=0
        x=i
        y=j
        while (x<n and y<m):
            if s[x]!=t[y]:
                count+=1
            if count==1:
                ans+=1
            if count==2:
                break
            x+=1
            y+=1
print(ans)
