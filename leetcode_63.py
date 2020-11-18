n=5
# a=bin(n).replace("0b","")
# l=list()
# for i in range(len(a)):
#     l.append(a[i])
# print(l)
# for i in range(0,len(l)-1):
#     print(l[i],l[i+1])
#     #print(l[i+1])
#
a=bin(n)[2:]
print(a)
print(all(a[i]+a[i+1] ==1 for i in range(len(a)-1) ))
