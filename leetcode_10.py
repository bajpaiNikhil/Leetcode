

def mims(A):
    return sum(max(abs(i[0]-j[0]),abs(i[1]-j[1])) for i,j in zip(A,A[1:]))
A=[[1,1],[3,4],[-1,0]]
print(mims(A))