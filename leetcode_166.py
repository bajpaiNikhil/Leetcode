
p = ["mobile" ,"mouse" ,"moneypot" ,"monitor" ,"mousepad"]
s = "mouse"

p.sort()
print(p)

left=0
right=len(p)-1
result=[]
for i in range(len(s)):

    while left<=right and (len(p[left])<=i or p[left][i]!=s[i]):
        left+=1
    while left<=right and (len(p[right])<=i or p[right][i]!=s[i]):
        right-=1
    if left+3<=right:
        result.append(p[left:left+3])
    else:
        result.append(p[left:right+1])
print(result)
