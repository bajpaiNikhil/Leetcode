
import numpy as np
n,start=10,5
l=[]
for i in range(n):
    l.append(start+2*i)
print(l)
print(3^5^7^9)
xor=0
for i in l:
    xor^=i
print(xor)