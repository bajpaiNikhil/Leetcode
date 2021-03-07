



#from collections import  Counter
#t="01011011011110"
#t='101'
#
# s=t.split("0")
#
# print(list(filter(str.strip, s)))
#
# print(s)

t=int(input())
for t in range(t):
    l=str(input())
    s=l.split("0")
    print(len(list(filter(str.strip,s))))