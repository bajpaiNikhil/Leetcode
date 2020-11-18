import numpy as np
a=np.array([[1,2],[3,4]])
print(a)

try:
    ar=a.reshape(2,4)
except ValueError:
    print(a)