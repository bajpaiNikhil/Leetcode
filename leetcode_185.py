


from math import ceil
seats=[1,0,0,0]

prev,max_len=0,0

for cur,seat in enumerate(seats):
    if seat:
        if seats[prev]:
            max_len=max(max_len,(cur-prev)//2)
        else:
            max_len=max(max_len,cur-prev)
        prev=cur

if seats[prev]:
    max_len=max(max_len,len(seats)-1-prev)
print(max_len)

#https://leetcode.com/problems/maximize-distance-to-closest-person/discuss/915477/PythonOne-pass-O(n)-solution-with-explanation

