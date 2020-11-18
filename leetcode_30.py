n,m=3,1
l=bin(n).replace("0b", "")
c=list(l)
print(l)
print(c)
k=bin(m).replace("0b", "")
d=list(k)
print(k)
print(d)
e=[value for value in c+d if value not in c or value not in d]
print(e)
print(len(e))

print(bin(n^m).count('1'))