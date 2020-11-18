a=[0,1,2,3,4,5,6,7,8]
b=[]

for i in range(len(a)):
    b.append(bin(a[i]).count('1'))
#print(b)
res=dict(zip(b,a))
print(res)

# c=sorted(res.values())
# print(c)
# for key,value in sorted(res.items()):
#     print(key)

# inv_map = {v: k for k, v in res.items()}
# print(inv_map)
# d=sorted(inv_map.values())
# print(d)
# e=sorted((res.keys()))
# print(e)
# f=sorted(res.items())
# print(f)
