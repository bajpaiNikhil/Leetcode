




n,m,x=list(map(int,input().split()))
l=list(map(int,input().split()))[:n]

if max(l)+x>=m:
    print("YES")
else:
    print("NO")
