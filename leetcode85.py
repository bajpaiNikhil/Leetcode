from collections import Counter
s="aa"
t="a"
d=dict(Counter(s))
e=dict(Counter(t))
print(d)
print(e)
print(d==e)
# if len(s)>=len(t):
#     print(2)
#     g=[i for i in s if i not in t]
#     print(g)
#     print(True if len(g) is 0 else False)
#
# else:
#     print(3)
#     h=[i for i in t if i not in s ]
#     print(True if len(h) is 0 else False)
# if len(s)==len(t):
#     g = [i for i in s if i not in t]
#     print(g)
#     print(True if len(g) == 0 else False)
# else:
#     print(False)



# print(g)
# print(len(g))
# print(True if len(g) is 0 else False)