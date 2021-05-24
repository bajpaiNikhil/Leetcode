







#n="*a**b"
# n="abcde"
# num=""
# for i in range(len(n)):
#     if n[i].isalpha()== True:
#         num+="0"
#     else:
#         num+="1"
# print(n)
# print(num)
#
# d=max(map(len,num.split('0')))
# print(d)





t=int(input())
for t in range(t):
    strlength, K = map(int,input().split())
    InputString=str(input())
    InputString=list(InputString)
    emptyString=""
    for i in range(len(InputString)):
        if InputString[i].isalpha() ==True:
            emptyString+="0"
        else:
            emptyString+="1"
    count=max(map(len,emptyString.split("0")))
    if count>=K:
        print("YES")
    else:
        print("NO")







