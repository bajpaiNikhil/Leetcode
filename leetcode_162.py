


a = "cad"
w = ["cc","acd","b","ba","bac","bad","ac","d"]
count=0
s=""
for i in w:
    count+=1
    for j in i:

        if j not in a:
            print(j)
            count-=1
            break
print(count)