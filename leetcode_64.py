n=19
def square(n):
    sq=0
    sq= sum(int(i) ** 2 for i in str(n))
    return sq
#n=19
print(square(n))

res=n

while(res!=1 and res!=4):
    res=square(res)

if res==1:
    print(True)
else:
    print(False)

