# from collections import  Counter
#
# n=[2,3,1,3,2,4,6,7,9,2,19]
# m=[2,1,4,3,9,6]
# d=dict(Counter(n))
# print(d)
# l=[]
#
# for i in m:
#     l.extend([i]*d[i])
# print(l)
#
#
# d,f,tar=2,6,7
# mod=1000000007
# print(mod)
# def diceSum(d,f,tar):
#     if tar<d or tar>d*f:
#         return 0
#     if d==1:
#         return 1 if tar<=f else 0
#     sum=0
#     for i in range(1,f+1):
#         sum+=diceSum(d-1,f,tar-i)
#     return sum%mod
# print(diceSum(d,f,tar))



# n,m=0,1
# k=2939
# d=m+k
# #print(m+k)
#
# #print((m+k)%60)
# if (m+k)>60:
#     n+=d//60
#     #print(n)
#     while n>24:
#         if n>24:
#             n-=24
#         #n-=24
#     m=d%60
#
# print(n,":",m)
#


# t=int(input())
# for t in range(t):
#     ts=int(input())
#
#     if ts%2==0:
#         #print(ts)
#         print(ts//8)
#     else:
#         print(ts//2)
#


#n=[1,2,1,3,5,6,4]

# left=0
# right=len(n)-1
#
# while(left<right):
#     mid=left+(right-left)//2
#     if n[mid]<n[mid+1]:
#         left=mid+1
#     else:
#         right=mid
# print(left)

# from collections import defaultdict
#
# s="cba"
# t="abcd"
#
# prefix=""
# postfix=""
# map=defaultdict(int)
# print(map)
# for i in t:
#     if i in s:
#         map[i]+=1
#     else:
#         postfix+=i
# print(map,postfix)
#
#
# for i in s:
#     prefix+=i*map[i]
# print(prefix+postfix)
#
#

# from collections import  defaultdict
# s="abcabcabcabc"
# sl=len(s)
# d,f="",0
# for i in range(1,len(s)):
#    d=s[:i]
#    print(d)
#    if sl%len(d)==0:
#        f=sl//len(d)
#        if s==(d*f):
#            print(True)
#        else:
#            print(False)
# print(d)


# n=24
#
# while n%2!=1:
#     n=n//2

#     print(n)
#     if n%2==1:
#         print(n//2)


# t=int(input())
# for t in range(t):
#     n=int(input())
#
#     if n%2==0:
#         while(n%2!=1):
#             n=n//2
#             print(n)
#             if n%2==1:
#                 print(n//2)
#                 break
#     else:
#         print(n//2)



 # n=[[1 , 2 ,3   , 4
 #     8 , 7 , 6 , 5,
 #    9 , 10, 11, 12,
 #    16, 15 ,14 ,13 ]]


#
# import  numpy as np
# t=int(input())
# for t in range(t):
#     n=int(input())
#     l=[i for i in range(1,n**2+1)]
#     mat=np.array(l).reshape(n,n)
#     if n%2==0:
#         for i in range(len(mat)):
#             if i%2!=0:
#                 mat[i]=mat[i][::-1]
#     for i in range(n):
#         for j in range(n):
#             print(mat[i][j],end= " ")
#         print()

# t=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#
# for i , j in enumerate(t):
#     print(i,j)
#     a=j.find("@")
#     if "+" in j:
#         k=j.find("+")
#     else:
#         k=a
#     t[i]=j[:k].replace(".","")+j[a:]
# print(len(set(t)))

#from collections import defaultdict

# from collections import  Counter
# n=[2,1,1,3,3,3]
# k=3
# a=Counter(n).most_common()
# print(a)
# print(a[-1][1])
# while a and k >=a[-1][1]:
#     k-=a.pop()[1]
# print(a)
# print(len(a))




# maap={
#     "I":             1,
#     "IV":            4,
#     "V":             5,
#     "IX":            9,
#     "X":             10,
#     "XL":            40,
#     "L":             50,
#     "90":            90,
#     "C":             100,
#     "CD":            400,
#     "D":             500,
#     "CM":            900,
#     "M":             1000
# }
# inv_map = {v: k for k, v in maap.items()}
# print(inv_map)
#
# roman="MCMXCIV"
# total=0
# for i in range(len(roman)-1):
#     current =maap[roman[i]]
#     next_roman=maap[roman[i+1]]
#
#     if current<next_roman:
#         total-=current
#     else:
#         total+=current
# total+=maap[roman[-1]]
# print(total)



# integer=1994
#
# int=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# roman=['M', 'CM', 'D', 'CD', 'C','XC' ,'L', 'XL','X' ,'IX', 'V', 'IV', 'I']
# s=[]
# for i in range(len(int)):
#     while(integer-int[i]>=0):
#         #print(int[i])
#         #print(roman[i])
#         s.append(roman[i])
#         integer=integer-int[i]
# print("".join(s))



# n="2*3-4*5"
# dict={}
# def compute(n):
#     if n.isdigit():
#         return [int(n)]
#
#     if n in dict:
#         return dict[n]
#     res=[]
#     for i in range(len(n)):
#         if n[i] in "-+*":
#             res1=compute(n[:i])
#             res2=compute(n[i+1:])
#             for j in res1:
#                 for k in res2:
#                     res.append(helper(j,k,n[i]))
#     dict[n]=res
#     return res
# def helper(m,n,op):
#     if op=="+":
#         return m+n
#     elif op=="*":
#         return m*n
#     elif op=="-":
#         return m-n
#
# print(compute(n))










