n=1
# if n==1:
#     print("a")
ans=''
if n%2==0:
    ans+="a"*(n-1)
    ans+="b"
else:
    ans+="a"*n
print(ans)