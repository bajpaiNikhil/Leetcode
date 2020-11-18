n="Let's take LeetCode contest"
s=list(n.split(" "))
a=[]
d=" "
print(s[0][::-1])
print(s[1][::-1])
for i in range(len(s)):
    a.append(s[i][::-1])
print(a)
print(d.join(a))
