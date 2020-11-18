s="PPAA"
countA=0
countL=0

for i in range(len(s)-2):

    if s[i]=="A":
        countA+=1
    if s[i]=="L" and s[i+1]=="L" and s[i+2]=="L":
        countL+=3
print(countA,countL)

print(countA>1,countL>0)

if countA > 1 or  countL > 1:
    print(False)
else:
    print(True)
