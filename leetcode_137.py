
"""[
[1,1,1,1],
[1,0,0,1],
[1,1,1,1]]
"""


m=[
    [0,0,1,1],
    [1,0,1,0],
    [1,1,0,0]
]
#copied

class Sol(object):

    def matrixScore(self,a):
        for i in range(len(a)):
            if a[i][0] == 0:
                self.flip_row(a, i)
        return self.dfs(a, 1)

    def dfs(self, a, j):
        if j == len(a[0]):
            return sum([int(''.join(map(str, a[i])), 2) for i in range(len(a))])
        count = sum([1 for i in range(len(a)) if a[i][j]])

        if count < (len(a)+1)//2:
            self.flip_col(a, j)
        return self.dfs(a, j + 1)

    def flip_row(self, a, i):
        for j in range(len(a[0])):
            a[i][j] = int(not a[i][j])

    def flip_col(self, a, j):
        for i in range(len(a)):
            a[i][j] = int(not a[i][j])


choti=Sol()
print(choti.matrixScore(m))


