a=["h","e","l","l","o"]
print(len(a))
print(a)
print(a[::-1])
n=len(a)
for i in range(0,len(a)//2):
    temp=a[i]
    a[i]=a[n-1-i]
    a[n-1-i]=temp
print(a)