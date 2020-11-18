n=[100,40,17,9,73,75]

k=3

l=[]
c = 0
a = 0
b = len(n)-1
for i in range(len(n)):

    while(c<k):
        #print(n[a],n[b])
        if n[a]>=n[b]:
            #print(1)
            l.append(n[a])
            a=a+1
        else:
            l.append(n[b])
            b=b-1
        c=c+1
print(l)
print(sum(l))

# cardPoints=[1,2,3,4,5,6,1]
# k=3
# l = []
# a = 0
# b = len(cardPoints) - 1
# c = 0
# for i in range(len(cardPoints)):
#
#     while (c < k):
#         if cardPoints[a] > cardPoints[b]:
#             l.append(cardPoints[a])
#             a=a+ 1
#         elif cardPoints[a]==cardPoints[b]:
#             l.append(cardPoints[a])
#             a=a+1
#             b=b-1
#         else:
#             l.append(cardPoints[b])
#             b=b-1
#         c=c+1
# print(l)
# print(sum(l))
