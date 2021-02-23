


h= [1,8,6,2,5,4,8,3,7]

a_pointer=0
b_pointer=len(h)-1
max_area=0
while(a_pointer<b_pointer):

    if (h[a_pointer]<h[b_pointer]):
        max_area=max(max_area,h[a_pointer]*(b_pointer-a_pointer))
        a_pointer+=1
    else:
        max_area=max(max_area,h[b_pointer]*(b_pointer-a_pointer))
        b_pointer-=1
print(max_area)