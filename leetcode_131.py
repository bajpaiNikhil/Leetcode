


s = "ababcbacadefegdehijhklij"

right,left=0,0
count=0
l=[]
c={a:i for i,a in enumerate(s)}
print(c)
for i,j in enumerate(s):
    right=max(right,c[j])
    #print(right)
    if i==right:
        count+=1
        l+=[right-left+1]
        left=i+1
print(count)
print(l)
