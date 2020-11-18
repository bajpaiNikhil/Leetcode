n=11
#print(2,9)
for i in range (n):
    if not '0' in f'{i}{n-i}':
        print([i,n-i])