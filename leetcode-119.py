a = "aaaaaaabc"
b = "aaaaaaacb"
count=0

print(sorted(a))
print(sorted(b))

if  len(a)!=len(b):
    print(False)
elif sorted(a)!=sorted(b):
    print(False)

for i,j in zip(a,b):
    if i!=j:
        count+=1
if count>=3:
    print(False)
else:
    print(True)


