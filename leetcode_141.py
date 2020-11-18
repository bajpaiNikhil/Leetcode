

from collections import Counter
s="aacaba"
res=0
leftcounter=Counter()
rightcounter=dict(Counter(s))
print(leftcounter,rightcounter)

for i in s:
    leftcounter[i]+=1
    rightcounter[i]-=1
    if rightcounter[i]==0:
        del rightcounter[i]
    if len(leftcounter)==len(rightcounter):
        res+=1
print(leftcounter,rightcounter)
print(res)