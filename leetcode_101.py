import math
x=100
prime=[2,3,5]
count=0
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
#x=5
#print(factorial(x))
for i in prime:
    if i<=x:
        count+=1
    else:
        break
print(factorial(x-count)*factorial(count)%int(math.pow(10,9)+7))

