n=[5,10]
fives=0
tens=0
for i in n:
    if i==5:
        fives+=1
    elif i==10:
        tens+=1
        fives-=1
    elif tens>0:
        tens-=1
        fives-=1
    else:
        fives-=3
    if fives<0:
        print(False)

print(True)