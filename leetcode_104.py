s="covid2019"
l=list(s)
res=[]
f=""
i_str=[]
s_str=[]
o=['0','1','2','3','4','5','6','7','8','9']
for i in s:
    if i in o:
        i_str.append(i)
        #print(i_str)
    else:
        s_str.append(i)
        #
        # print(s_str)
d=(abs(len(i_str)-len(s_str)))
if d<=1:
    res=[i+j for i,j in zip(i_str,s_str)]
else:
    print("''")
print(res)
print(f.join(res))
