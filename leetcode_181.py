

s=["h","e","l","l","o"]
print(s[::-1])

i=0
j=len(s)-1

while i<=j:
    s[i],s[j]=s[j],s[i]
    i+=1
    j-=1
print(s)