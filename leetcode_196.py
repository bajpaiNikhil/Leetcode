

from functools import  reduce
edges = [[1,2],[5,1],[1,3],[1,4]]



res = list(reduce(lambda i, j: i & j, (set(x) for x in edges)))
print(res)