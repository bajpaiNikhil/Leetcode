
def prime(n):

    if n==1: return False

    if n<=3: return True

    if (n%2==0 or n%3==0):
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

def bits(l,r):
    count=0

    for i in range(l,r+1):
        n=bin(i).replace("0b",'').count("1")
        if prime(n):
            count+=1
    return count

l,r=10,15
print(bits(l,r))