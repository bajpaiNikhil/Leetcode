



# n=[1,2,34,3,4,5,7,23,12]
#
# for i in range(len(n)):
#     if n[i]%2!=0 and n[i+1]%2!=0 and n[i+2]%2!=0:
#         print(True)
#     else:
#         print(False)

#
# from collections import Counter
# n=["hello","world","leetcode"]
# c="welldonehoneyr"
# sum=0
# d=Counter(c)
# for i in n:
#     f=Counter(i)
#     for g in f:
#         if f[g]>d[g]:
#             break
#     else:
#         sum+=len(i)
# print(sum)



# n=[[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# row=len(n)
# col=len(n[0])
# num=0
# for i in range(row):
#     for j in range(col):
#         if n[i][j]==1:
#             if (i == 0 or n[i - 1][j] == 0):
#                 num+=1 # UP
#             if (j == 0 or n[i][j - 1] == 0):
#                 num+=1 # LEFT
#             if (i == row - 1 or n[i + 1][j] == 0):
#                 num+=1 #// DOWN
#             if (j == col - 1 or n[i][j + 1] == 0):
#                 num+=1 #// RIGHT
# print(num)
#

# t=int(input())
#
# for t in range(t):
#     n=int(input())
#     l=list(map(int,input().split()))[:n]
#     l.sort()
#     if l[0]==0:
#         print(len(set(l))-1)
#     else:
#         print(len(set(l)))

# import numpy as np

# [[1, 2, 9, 13],
# [5, 6, 10, 14],
# [3, 7, 11, 15],
# [4, 8, 12, 16]]
#
# import numpy as np
# t=int(input())
# for t in range(t):
#         size=int(input())
#         matrix=[]
#         count=0
#
#         for i in range(size):
#                 matrix.append(list(map(int,input().split())))
#         matrix=np.array(matrix)
#
#         for i in range(size-1,0,-1):
#
#                 if matrix[i][i]!=matrix[i][i-1]+1:
#                         count+=1
#                         matrix[:]=matrix.T
#         print(count)

# from math import *
# n=7
#
#
# def func(n):
#     return (n*(n+1)//2)
# additiion=(n*(n+1)//2)

# print(additiion)



# if len(n)%2==0:
#
#         d=len(n)//2
# else:
#         d=len(n)//2+1
# print(d)
#
# i=0
# j=d
# #print(i,j)
# count=0
# for k in range(d-1):
#         #print(n[i],n[d])
#         n[i],n[j]=n[j],n[i]
#         #print(n)
#         #print(sum(n[:d ]),sum(n[d :len(n)]))
#         if (sum(n[:d])==sum(n[d:len(n)])):
#                 count+=1
#         n[j],n[i]=n[i],n[j]
#         #print(n)
#         i+=1
#         j+=1
# print(count)


# t=int(input())
#
# for t in range(t):
#     n=int(input())
#     suum=n*(n+1)//2
#     # print(suum)
#
#     if suum%2!=0:
#         print("0")
#     else:
#         ans=(-1)+(1+(4*(suum)))**0.5
#         ans//=2
#         ans=int(ans)
#         # print(ans)
#         result=n-ans
#
#         left_wing=(ans*(ans+1))//2
#         right_wing=((n*(n+1))//2)-left_wing
#         if left_wing==right_wing:
#             r=n-ans
#             r-=1
#             ans-=1
#             result+=(ans*(ans+1))//2
#             result+=(r*(r+1))//2
#         print(result)

#n,k,l=4,3,2
# t=int(input())
# for t in range(t):
#     n,k,l=(map(int,input().split()))
#     list=[]
#     if k*l<n:
#         print(-1)
#     else:
#         d=n//k
#         e=n%k
#         #print(e)
#         while d>0:
#             for i in range(1,k+1):
#                 list.append(i)
#             d-=1
#         print(str(list+[i for i in range(1,e+1)])[1:-1].replace(",",""))
#



#
# t=int(input())
# for t in range(t):
#     n=int(input())
#     l= list(map(int,input().split()))[:n]
#     d=[]
#     if sum(l)<0:
#         print("NO")
#     else:
#         print("YES")
    #
    # for i in range(n):
    #     #print(l[i])
    #     if l[i]!=0:
    #         o=l[i]-(i+1)
    #     #print(o)
    #     else:
    #         continue
    #     d.append(o)
    #
    # print(l)
    #
    # print(sum(l))
    # print(d)
    # print(sum(d))
    # if (sum(d)==0 or sum(l)==0):
    #     print("YES")
    # else:
    #     print("NO")
    #





# t = int(input())
# for t in range(t):
#     ni, k = map(int, input().split())
#     n = list(map(int, input().split()))
#
#     if k == 1:
#         print(sum(n) + ni)
#
#     elif (len(set(n)) == 1 and len(n)) != 1:
#         print(sum(n) // k)
#     else:
#         print(sum(n) // k + 1)



# s="hello"
# s=list(s)
#print(s)
#print(vowel)
#
# def vowel(d):
#     return (d=="a" or d=="e" or d=="i" or d=="o" or d=="u")
#
# i=0
# j=len(s)-1
# while i<j:
#
#     if not vowel(s[i]):
#         i+=1
#         continue
#     if not vowel(s[j]):
#         j-=1
#         continue
#     s[i],s[j]=s[j],s[i]
#     i+=1
#     j-=1
# print("".join(s))

#
# n=[1,7,3,6,5,6]
#
#
# for i in range(len(n)):
#     #print(n[i])
#     if(sum(n[:i])==sum(n[i+1:])):
#         print(i)
#         break


# t=int(input())
# for t in range(t):
#
#     n,k,x,y=map(int,input().split())
#     i=0
#     flag=0
#     while i<n:
#         a=(x+k)%n
#         x=a
#         if x==y:
#             flag=1
#             print("YES")
#             break
#         i+=1
#     if flag==0:
#         print("NO")
#
# t=int(input())
# for t in range(t):
#
#     n,k=map(int,input().split())
#     l=list(map(int,input().split()))[:n]
#     o=0
#     count=0


# l=[]
# k=[]
# while True:
#     g=(input())
#     if g=="q":
#         break
#     elif g<str(0):
#         print("Invalid String!")
#         break
#     else:
#         l.append(float(g))
#
# print(l)
#
# for i in l:
#     if i<42.195:
#         k.append(i)
# k.sort(reverse=True)
# print(k)
# print(k[:3])
#
# count=0
# totalCount=-1
# while (True):
#     n=input()
#     totalCount+=1
#     if n=="Q" or n=="q":
#         break
#     if len(n)==10:
#         for i in n:
#             if i not in "0123456789":
#                 break
#         count+=1
# #print(totalCount)
# if totalCount!=5:
#     print("invalid input")
# print(count)
#
#
# sum=0
#
# menu=[80,130,100,80,90,110,120,140,70,80,130,160,70,60,40,50,30,40,160,150]
# while True:
#     n=int(input())
#     q=int(input())
#     sum+=menu[n-1]*q
#     o=input()
#     if o=="y" :
#         continue
#     elif o=="n":
#         break
# print("Total Amount :" +str(float(sum))+ "INR")



from math import *

def printDivisors(n):
    i = 1
    while (i * i < n):
        if (n % i == 0):
            print(i, end=" ")
        i += 1
    for i in range(int(sqrt(n)), 0, -1):
        if (n % i == 0):
            print(n // i, end=" ")

number=int(input())
printDivisors(number)





















