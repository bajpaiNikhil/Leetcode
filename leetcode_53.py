from collections import Counter
n=[4,1,2,1,2]
d=dict(Counter(n))

for key,value in d.items():
    if value%2!=0:
        print(key)
