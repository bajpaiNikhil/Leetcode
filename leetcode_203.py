
#
# n=[12,17,15,13,10,11,12]
# n_len=len(n)
# max_sum=n[0]
# curr_sum=n[0]
# for i in range(1,n_len):
#     if n[i-1]<n[i]:
#         curr_sum+=n[i]
#         max_sum=max(curr_sum,max_sum)
#     else:
#         max_sum=max(curr_sum,max_sum)
#         curr_sum=n[i]
#
# print(max_sum)



# ll = list(map(int,input().split()))
#
# if len(set(ll))==1 or len(set(ll))== 2:
#     print("YES")
# else:
#     print("NO")


t=int(input())
for t in range(t):
    k1,k2,k3,v  = map(float,input().split())
    print(k1,k2,k3,v)
    d=k1*k2*k3*v
    e=round(d,10)
    print(e)
    x=100/e
    if round(x,2)<9.58:
        print("YES")
    else:
        print("NO")








