


s="([]{}"
stack=["a"]
d = {
    ')':'('
    ,']':'['
    ,'}':'{'
}

for i in s:
    if i in d.keys():
        if stack.pop()!=d[i]:

            print("False")
    else:
        stack.append(i)
print(len(stack)==1)

