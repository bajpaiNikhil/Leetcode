




t=int(input())
for t in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))[:m]
    for i in range(n):
        s=list(map(int,input()))
        p=[]
        for a,b in zip(l,s):
            p.append(a*b)
        print(sum(p))

