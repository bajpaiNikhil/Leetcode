l,r=1,22

l=[num for num in range(1,r+1) if "0" not in str(num) and all(num % int(c)==0 for c in str(num))]
print(l)