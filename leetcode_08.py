s = "RLRRLLRLRL"

left_cnt=0
right_cnt=0
out=0
for char in s:
    if char=="L":
        left_cnt+=1
    else:
        right_cnt+=1
    if left_cnt==right_cnt:
        out+=1
print(out)