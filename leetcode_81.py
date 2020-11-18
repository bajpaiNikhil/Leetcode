S = "a##c"
T = "#a#c"

def convert(words):
    stack=[]
    for c in words:
        if c=="#":
            if len(stack)>0:
                stack.pop()
        else:
            stack.append(c)
    return " ".join(stack)
if convert(S)==convert(T):
    print(True)
else:
    print(False)