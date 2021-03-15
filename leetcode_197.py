



word1 = "ab"
word2 = "pqr"

n1=len(word1)
n2=len(word2)

n=min(n1,n2)
s=""
for i in range(n):
    s+=word1[i]+word2[i]

print(s + word1[n:] + word2[n:])