#
# arr=[0,2,3,3,4,5,2,1]
#
# i,j,k=0,len(arr)-1,len(arr)
#
#
# while(i+1<k and arr[i]-arr[i+1]<0):
#     i+=1
# while(j>0 and arr[j-1]-arr[j]>0):
#     j-=1
# print(0<i==j<k-1)

n=[3,1,2,4]
j = 0
for i in range(len(n)):

    if n[i]%2==0:
        print(n[i],j)
        n[j],n[i]=n[i],n[j]
        j+=1
print(n)