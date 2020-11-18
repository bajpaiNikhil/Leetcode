n=[1]
def maxiimum(n):
    max_current=max_global=n[0]
    for i in range(1,len(n)):
        max_current=max(n[i],max_current+n[i])
        if max_current>max_global:
            max_global=max_current
    return max_global
print(maxiimum(n))