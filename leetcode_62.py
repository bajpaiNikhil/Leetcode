n=5
a=bin(n).replace("0b"," ")
print(a)
n1=((1 << a )-1)^n
print(a)

print(n1)
print(~n)

