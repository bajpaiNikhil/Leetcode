from collections import Counter
s = "aba"
t = "abba"

t_sum=0

for i in t:
    t_sum+=ord(i)
for i in s:
    t_sum-=ord(i)
print(chr(t_sum))