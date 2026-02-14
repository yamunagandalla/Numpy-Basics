import numpy as np 
y=np.array([[1,2,3],[4,5,6]])
print(y)
print("shape of y is :",y.shape)#(2,3)
#method 1
a=y.T
print(a)
print("shape of a is :",a.shape) #(3,2) transpose converts rows into columns and columns into rows
# method 2
m=y.transpose()
print(m)
print("shape of m is :",m.shape)# (3,2) both gives the same result

# using transpose to 1D array
u=np.array([1,2,3,4])
print(u)
print("shape of u is :", u.shape) #(4,)
n=u.T
print ("transpose of u is :",n)# NO CHANGE in 1D array
print("shape of n is :",n.shape) #(4,) no change in shape as well

# if you want to transpose a 1D , make it 2D 1 st and then transpose
a=u.reshape(1,4)
print("reshaped a is :",a)
print("shape of reshaped a is :",a.shape) #(1,4)
print("transpose of a is : ", a.T)
print(a.T.shape) 

