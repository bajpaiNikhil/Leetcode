from collections import Counter
t="nlaebolko"
l=[]
count=0
d=dict(Counter(t))

print(d)
#print(d['l']//2)
if len(t)<7:
    print('0')
for i in d:
    if "b" in d:
        l.append(d['b'])
    if "a" in d:
        l.append(d['a'])
    if "l" in d:
        l.append(d['l']//2)
    if 'o' in d:
        l.append(d['o']//2)
    if 'n' in d:
        l.append(d['n'])
    else:
        break
print(min(l))



