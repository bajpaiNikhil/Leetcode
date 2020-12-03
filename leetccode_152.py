



w1  = ["abc", "d", "defg"]
w2 = ["abcddefg"]

letter=""
letter2=""
for i in w1:
    letter+=i
print(letter)

for i in w2:
    letter2+=i
print(letter2)

if letter==letter2:
    print("True")
else:
    print("False")