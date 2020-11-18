
import string
print(string.ascii_lowercase)

from collections import Counter

def checker(n,m):
    a, b = Counter(n), Counter(m)
    return check(a,b)|check(b,a)

def check(a,b):
    s=0
    for c in string.ascii_lowercase:
        s+=a[c]-b[c]
        #print(s)
        print(a[c],b[c])
        if s<0:
            return False
    return True
n,m=s1 = "leetcodee", "interview"
print(checker(n,m))
