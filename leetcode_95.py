from collections import Counter
s="aa"
t="ab"
d=dict(Counter(t))
# print(d)
# print(d.get("a"))
for i in s:
    #print(d.get(i))
    count=d.get(i)
    if i not in d or count<=0:
        print(False,i)
    count-=1
    print(count)
print(True)
