s="00111"
left=""
right=""
l_c=[]
r_c=[]

for i in range(1,len(s)):
    left=s[:i]
    right=s[i:]
    print(left,right)
    l_c.append(left.count('0'))
    r_c.append(right.count('1'))

print(l_c,r_c)
e=max([sum(i) for i in zip(l_c,r_c)])
print(e)
# a=[0, 1, 1, 1, 1, 2]
# b=[4, 4, 3, 2, 1, 1]
# e=[sum(i) for i in zip(a,b)]
# print(e)