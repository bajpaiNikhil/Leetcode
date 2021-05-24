#
# from itertools  import combinations
#
# def Sub_Sequences(STR,ll):
#     combs = []
#     for l in range(1, len(STR ) +1):
#         combs.append(list(combinations(STR, l)))
#     for c in combs:
#         for t in c:
#             si=""
#             #print(''.join(t), end =' ')
#             si="".join(t)
#             #ll.append(si)
#             if si not in ll:
#                 ll.append(int(si,2))
#     return set(ll)
#
# ll=[]
# print(Sub_Sequences("1001011",ll))
# e=Sub_Sequences("1111",ll)
# k=1024
# for i in range(k) :
#     if i not in e:
#         print(bin(i).replace("0b",""))
#         break

# from itertools  import combinations
#
# def Sub_Sequences(STR,ll):
#     combs = []
#     for l in range(1, len(STR ) +1):
#         combs.append(list(combinations(STR, l)))
#     for c in combs:
#         for t in c:
#             si=""
#             #print(''.join(t), end =' ')
#             si="".join(t)
#             #ll.append(si)
#             if si not in ll:
#                 ll.append(int(si,2))
#     return set(ll)


# def findFirstMissing(array, start, end):
#     if (start > end):
#         return end + 1
#
#     if (start != array[start]):
#         return start
#
#     mid = int((start + end) / 2)
#
#     if (array[mid] == mid):
#         return findFirstMissing(array,mid + 1, end)
#
#     return findFirstMissing(array,start, mid)

t=int(input())
for t in range(t):
    bin_string = input()
    aux_list=[]
    e=list(Sub_Sequences(bin_string,aux_list))
    print(e)
    f=min(set(range(0, len(e) + 1)) - set(e))
    print(bin(f).replace("0b",""))

