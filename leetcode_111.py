from collections import Counter
s = "leetcode"
t = "practice"
# d=defaultdict(int)
# for i in s:
#     d[i]+=1
# print(d)
d=dict(Counter(s))
print(d)
count=0
for i in t :
    if  i not in d:
        count+=1
    else:
        if d[i]:
            d[i]-=1
        else:
            count+=1

print(count)
