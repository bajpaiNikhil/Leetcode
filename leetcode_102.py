dividend=-2147483648
divisor=-1

sign = -1 if ((dividend<0) ^ (divisor <0)) else 1

dividend=abs(dividend)
divisor=abs(divisor)
count=0
quotient=0
for i in range(31,-1,-1):
    if (count+(divisor << i)<= dividend):
        count+=divisor<<i
        quotient |= 1<<i

print(quotient*sign)