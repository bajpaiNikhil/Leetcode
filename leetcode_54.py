s="I speak Goat Latin"

n='abcd'
m=n.split()
print(n[1:]+n[0]+'ma')
l=s.split(' ')
print(l)
print(l[0])
print(l[1][0])
print(len(l))
print(len(l[0]))
vowel=['a','e','i','o','u','A','E','I','O','U']
g=[]
for i,k in enumerate(l):
    print(i)
    if k[0] in vowel:
        k+='ma'
        print(k)
    else:
        k=k[1:]+k[0]+'ma'
    k+='a'*(i+1)
    g.append(k)
print(' '.join(g))



