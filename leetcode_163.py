

s="ab-cd"

a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=list(s)
low=0
high=len(s)-1


while(low<high):
    if s[low] not in a:
        low+=1
    elif s[high] not in a:
        high-=1
    else:
        s[low],s[high]=s[high],s[low]
        low+=1
        high-=1

print("".join(s))
