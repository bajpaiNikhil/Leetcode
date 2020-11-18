# from collections import defaultdict
#
# m=["eat", "tea", "tan", "ate", "nat", "bat"]
# s=defaultdict(list)
#
# for i in m:
#     s[str(sorted(i))].append(i)
# res=list(s.values())
# print(str(res))

from itertools import groupby

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print([list(g) for k, g in groupby(sorted(words, key=sorted), sorted)])