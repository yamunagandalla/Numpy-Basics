import numpy as np  
a=np.arange(1,7)
print(a)
print(a.shape) #(6,)
c= a.reshape(2,3)
print(c)
print(c.shape) #(2,3)

# using -1 in reshape
n= np.arange(12)
print(n)
u=n.reshape(3,-1)
print(u)
print(u.shape) #(3,4) the -1 automatically calculates the number of columns needed
v=n.reshape(-1,3)
print(v)
print(v.shape) #(4,3)

