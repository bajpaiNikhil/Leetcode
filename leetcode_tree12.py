
# n=[0,1,2,3,4]
# b=3
# m=[0,3,4]
# x=[n[i:i+3] for i in range(0,len(n),b)]
# print(x)
#print(x[1])
# count=0
# for i in x:
#     #print(i)
#     if len([j for j in i if j in m ]) :
#         count+=1
# print(count)


t=int(input())
for t in range(t):
    a,b,c=map(int,input().split())
    m=list(map(int,input().split()))[:c]
    count=1
    l=[]
    for i in m:
        e=i//b
        l.append(e)
    print(l)
    for i in range(len(l)-1) :
        if l[i]!=l[i+1]:
            count+=1
    print(count)

