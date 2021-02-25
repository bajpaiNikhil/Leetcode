



# n="001011"
#
# n=list(n)
# l=[]
#
# for i in range(len(n)):
#     count=0
#     for j in range(len(n)):
#         if i!=j and n[j]=="1":
#             count+=abs(i-j)
#     l.append(count)
# print(l)


n="110"
n=list(n)

s=set()

for i in range(len(n)):
    if n[i]=="1":
        s.add(i)
print(s)
l=[]
for i in range(len(n)):
    count=0
    for j in s:
        count+=abs(i-j)
    l.append(count)
print(l)