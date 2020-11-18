a=[-1,0,3,5,9,12]
x=9
n=len(a)
def bsearch(a,n,x):
    low=0
    high=n-1
    while(low<=high):
        mid=low+(high-low)//2
        if x==a[mid]:
            return True
        elif(x<a[mid]):
            high=mid-1
        else:
            low=mid+1
    return False

print(bsearch(a,n,x))

