


n=[-1,0,1,2,-1,-4]


n.sort()
m,r=len(n),[]

for i in range(m-2):
    if i==0 or (i>0 and n[i]!=n[i-1]):
        low=i+1
        high=m-1
        sum=0-n[i]
        while (low<high):
            if n[low]+n[high]==sum:
                r.append([n[low],n[high],n[i]])
                while(low<high and n[low]==n[low+1]):
                    low+=1
                while(low<high and n[high]==n[high-1]):
                    high-=1
                low+=1
                high-=1
            elif (n[low]+n[high]>sum):
                high-=1
            else:
                low+=1
print(r)


