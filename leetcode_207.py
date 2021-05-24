




s = "a1b2c3d4e"
t=""

for i in range(len(s)):
    if s[i].isalpha():
        t+=s[i]
    else:
        t+= chr(ord(s[i-1]) + int(s[i]))
print(t)