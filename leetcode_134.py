from collections import Counter
s = "())"
count=0

left,right=0,0

for i in s:
    if right==0 and  i==")":
        left+=1
    else:
        right+=1 if i =="(" else -1

print(left+right)

