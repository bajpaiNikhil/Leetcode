


a=16
c="0b1111"
print(type(int(str(c).replace("0b",""))))
for i in range(a):
    for j in range(16):
        #print(bin(i),bin(j),i,j)
        r=int(bin(i).replace("0b",""))
        s=int(bin(j).replace("0b",""))
        e=r^s
        print(int(str(e),2))
        # if r^s==int(bin(13).replace("0b","")):
        #     print(i,j)