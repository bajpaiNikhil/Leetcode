




s = "00110110"
k = 3


a=set()

for i in range(len(s)-k+1):
    a.add(s[i:i+k])
    print(a)
print(len(a)== 2**k)