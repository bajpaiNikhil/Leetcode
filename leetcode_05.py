
def jewels(j,s):
    my_set=set(j)
    return sum(1 for char in s if char in my_set)
j="aA"
s="aAAbbbb"

print(jewels(j,s))