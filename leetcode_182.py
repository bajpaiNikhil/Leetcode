




mat = [[0,1,1,0],
       [0,1,1,1],
       [1,1,1,0]]

countOnes=0

rows=len(mat)
cols=len(mat[0])

for r in range(rows):
    for c in range(1,cols):
        if mat[r][c]:
            mat[r][c]=mat[r][c-1]+1

print(mat)

submatrices = 0
for r in range( rows ):
    for c in range( cols ):
        if mat[r][c]:
            row = r
            submatrix_width = mat[r][c]
            print(submatrices)
            while row < rows and mat[row][c]:
                submatrix_width = min( submatrix_width, mat[row][c] )
                submatrices += submatrix_width
                row += 1
print(submatrices)
#https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/725108/Python-3-Dynamic-Programming
