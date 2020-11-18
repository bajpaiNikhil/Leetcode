from collections import Counter

n=[0,1,0,1,0,1,99]
d=dict(Counter(n))
for key , value in d.items():
    if value%3!=0:
        print(key)