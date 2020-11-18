n="Leetcode"
f=n.upper()
g=n.lower()
print(f)
if n==f:
    print(1)
elif(n[0]==f[0] and n[1::] ==g[1::]):
    print(1)
elif n==g:
    print(1)
else:
    print(False)

