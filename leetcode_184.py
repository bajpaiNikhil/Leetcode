


from collections import Counter
A = ["amazon","apple","facebook","google","leetcode"]
B = ["ec","oc","ceo"]
count=Counter()
for b in B:
    count|=(Counter(b))
print(count)
l=[]
for a in A:
    #f=Counter(a)
    #print(not count - Counter(a),a)
    if not count - Counter(a):
        l.append(a)
print(l)
#https://stackoverflow.com/questions/3929278/what-does-ior-do-in-python

