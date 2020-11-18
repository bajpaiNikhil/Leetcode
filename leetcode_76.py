n=[7,1,5,3,6,4]
a=len(n)
p=0
# if n==0 or len(n)==0:
#     print(0)
for i in range(len(n)-1):
    if (n[i+1]>n[i]):
        p+=n[i+1]-n[i]
print(p)

