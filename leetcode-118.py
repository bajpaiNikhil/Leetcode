# nums=[1,3,2,1]
# count=0
# for i in range(len(nums)-1):
#     if nums[i]>nums[i+1]:
#         count+=1
#         if count>2:
#             print(True)
#         elif (i - 1) >= 0 and nums[i + 1] < nums[i - 1]:
#             nums[i + 1] = nums[i]
# print(False)


n=7463847412

s=""
l=(str(abs(n))[::-1])
d=0
#print(type(l))

for i in range(len(l)-1):
    #print(l[i])
    if l[i]=="0":
        d+=1
    elif int(l[i])-int(l[i+1])<0 or int(l[i])-int(l[i+1])>0:
        break

l=list(str(n))
print(l)
if n>0:
    if n > (2 ** 31 - 1) or int(str(n)[::-1]) < -(2 ** 31):
          print(0)
    if  l[-1]=="0":

        s=s.join(l[::-1])
        print(s[d:])
    else:
        print(s.join(l[::-1]))
print(s)

if n<0:

    if n > (2 ** 31 - 1) or int(str(n)[:0:-1]) < -(2 ** 31):
          print(0)
    n=abs(n)
    if  l[-1]=="0":
        s=s.join(l[:0:-1])
        print("-"+s[d:])
    else:
        print("-"+s.join(l[:0:-1]))

else:
    print(0)

