numRows=5
#trinagle=[]

# if numrows==0:
#     print(trinagle)
#
# trinagle.append([1])
# for i in range(1,numrows):
#     prevrow=trinagle[i-1]
#     nextrow=[]
#     nextrow.append(1)
#
#     for j in range(1,len(prevrow)):
#         nextrow.append(prevrow[j-1]+prevrow[j])
#     nextrow.append(1)
#
#     trinagle.append(nextrow)
# print(trinagle)
triangle = []

if numRows == 0:
    print(triangle)

triangle.append([1])
for i in range(1, numRows):
    prevrows = triangle[i - 1]
    nextrow = []
    nextrow.append(1)

    for j in range(1, len(prevrows)):
        nextrow.append(prevrows[j - 1] + prevrows[j])
    nextrow.append(1)
    triangle.append(nextrow)
print(triangle)