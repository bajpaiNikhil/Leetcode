l="we will we will rock you"
f,s='we', 'will'
a=l.split(" ")

d=[a[i+2] for i in range(len(a)) if a[i]==f and a[i+1]==s]
print(d)