


# n,k=[1,2,3,4,4,3,2,1],4
#
# h=len(n)//2
# print(h)
# l=[]
# print(n[:h])
# for j in zip(n[:h],n[h:]):
#     l.extend(j)
# print(l)


import argparse
parser=argparse.ArgumentParser(
    description="This is working",
    epilog="yes its working:::"
)
parser.print_help()
