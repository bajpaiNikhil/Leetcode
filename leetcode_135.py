#
#
# from collections import Counter
# n=["badc","abab","dddd","dede","yyxx"]
# p="baba"
#
# dp=dict(Counter(p))
# # print(list(dp.values()))
# l=[]
# for i in n:
#     #print(i)
#     e=dict(Counter(i))
#     #print(e)
#     #print(list(dp.values()),list(e.values()))
#     if list(dp.values())==list(e.values()):
#         l.append(i)
# print(l)
#
#
#

# def findAndReplacePattern(words, pattern):
#     return [w for w in words if len(set(w)) == len(set(pattern)) == len(set(zip(w, pattern)))]
words=["badc","abab","dddd","dede","yyxx"]
patterns="baba"
# print(findAndReplacePattern(words,patterns))

