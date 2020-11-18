n=4421
#b=list(map(int,str(a)))
b = list(map(int, str(n)))
mul = 1
for x in b:
    mul = mul * x
product = mul
add = sum(b)
diff = product - add
print(diff)