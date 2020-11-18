candies,num_people=7,4
#res=[0]*num_people
res, i = [0]*(num_people+1), 0
while candies > 0:
    k = i % num_people + 1
    num = i + 1
    res[k] += num if candies > num else candies
    candies -= num
    i += 1
print(res[1:num_people+1])
