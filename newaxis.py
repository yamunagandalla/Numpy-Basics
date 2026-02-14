import numpy as np 
a=np.array([1,2,3,4])
print(a)
print(a.shape) # (4,) 
b=a[:,np.newaxis]
print(b)
print(b.shape)# (4,1) this is a column vector
d=a[np.newaxis,:]
print(d)
print(d.shape) #(1,4) this is a row vector

y=np.array([3,11,4,5])
a=np.array([5,0,3])
m=y[:,np.newaxis]-a

print("the y before newaxis is :",y)
print(y.shape)
print("the a before newaxis is :",a)
print(a.shape)

print("the y after newaxis is :",y[:,np.newaxis])
print("the m after newaxis is :",m)
print(m.shape) #(4,3) 

