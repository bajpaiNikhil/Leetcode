import math
num=[2,1,2,3]
#print(n)
n=list(set(num))
n.sort()
print(n)
if len(n)<3:
    print(max(n))
else:
    print(n[len(n)-3])
# if len(set(n))<=2:
#     print(max(n))
# first,second,third=n[0],-math.inf,-math.inf
# for i in range(len(n)):
#     if n[i]==first and n[i] == second and n[i]==third:
#         continue
#     if n[i]>first:
#         third=second
#         second=first
#         first=n[i]
#     elif n[i]>second:
#         third=second
#         second=n[i]
#     elif n[i]> third:
#         third=n[i]
# print(first,second,third)