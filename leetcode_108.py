num=7

ans = []
for i in range(num + 1):
    ones = bin(i).split("0b")[1].count("1")
    ans.append(ones)
print(ans)