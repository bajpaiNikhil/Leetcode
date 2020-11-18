l=[1,2,2,6,6,6,6,7,10]
a=l.count(6)
print(a)
print(0.25*len(l))
for i in l:
    if (l.count(i)>.25*len(l)):
      print(i)
      break