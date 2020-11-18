n=[1,3,2]
a=sorted(n)
b=sorted(n,reverse=True)
print(b)
if a==n or n==b:
    print(True)
else:
    print(False)