


n=int(input())
for t in range(n):
    l=list(map(str,input()))
    if "P" in l and "C" in l and "M" in l:
        print("YES")
    else:
        print("NO")
