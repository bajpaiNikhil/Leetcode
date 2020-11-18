import math
n=5
s=len(bin(n).replace("0b",' '))-1
print(s)
print(bin(5))

a=((1<<int(s))-1) ^ n
print(a)

number_of_bits = (int)(math.floor(math.log(n) /
                                math.log(2))) + 1

print(number_of_bits)