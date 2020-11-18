



n="10111"

status='0'
flip=0
for i in n:
    if i!=status:
        flip+=1
        status='0' if status =='1' else '1'
print(flip)
