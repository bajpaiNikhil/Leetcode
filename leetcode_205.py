





t=int(input())
for t in range(t):
    n=int(input())
    ans=0
    pile_sum=0
    remainder=0
    pile_sum = (n//4)*44
    remainder = n%4

    if n>=4:
        if remainder == 0:
            pile_sum+=16
            print(pile_sum)
        elif remainder == 1:
            pile_sum+=32
            print(pile_sum)
        elif remainder == 2:
            pile_sum+= 44
            print(pile_sum)
        elif remainder == 3:
            pile_sum+= 55
            print(pile_sum)
    else:
        if n==1:
            print(20)
        if n==2:
            print(36)
        if n==3:
            print(51)



