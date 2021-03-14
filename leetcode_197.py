



classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
l=[]
for i in range(len(classes)):
    l.append(classes[i][0]/classes[i][1])
print(l)
d={}
for key,val in zip(l,classes):
    d[key]=val
print(d)