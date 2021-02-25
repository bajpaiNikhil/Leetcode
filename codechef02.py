



t=int(input())

for t in range(t):
    m,n=map(int,input().split())
    bmi=m//(n**2)

    if bmi<=18:
        print(1)
    elif 19<=bmi<=24:
        print(2)
    elif 25<=bmi<=29:
        print(3)
    elif bmi>=30:
        print(4)
