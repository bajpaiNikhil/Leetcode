a=moves="LL"
#l=list(a)
#b=[]
#print(l)
# l = list(moves)
# b = []
# d = {"U": 1, "D": -1, "R": 1, "L": -1}
# for i in range(len(l)):
#     search = l[i]
#     result = [val for keys, val in d.items() if search in keys]
#     b.extend(result)
#     print(b)
# if sum(b) == "0":
#     print("true")
# else:
#     print("false")
from collections import Counter
c=Counter(moves)
print(c)
if c['L']==c['R'] and c['U']==c['D']:
    print("True")
else:
    print("False")