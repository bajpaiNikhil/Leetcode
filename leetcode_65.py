
a=[40,10,20,30]

d={index:i+1 for i, index in enumerate(sorted(set(a)))}

print(d)
print([d[i] for i in a])

