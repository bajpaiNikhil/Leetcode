A,k =[0,10],2
M,n=max(A),min(A)
print(M,n)

dif,ext=M-n,2*k
s=dif-ext
if dif<=ext:
    print(0)
else:
    print(s)