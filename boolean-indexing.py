import numpy as np 

foo =np.array([
      [3,9,7],
      [2,0,3],
      [3,3,1]
])
print(foo)
mask = foo==3
print(mask)
print(foo[mask])
foo[mask]=0
print(foo)

#logical operaitions on boolean arrays
b1=np.array([False,True,False,True])
b2=np.array([False,False,True,True])
print("b1 and b2 is :",b1&b2)
print("b1 or b2 is : ", b1|b2)
print("b1 xor b2 is :", b1^b2)

c= ~np.array([False,True]) #NOT operatior
print(c)

#NaN 

bot = np.ones((3,4))
print (bot)
bot[[0,2],[1,2]]=np.nan
print(bot)
print (bot == np.nan)#False because NaN is not equal to anything, even itself
print(bot != np.nan) #True because NaN is not equal to anything, even itself
print(np.isnan(bot)) #True for NaN values and False for non-NaN values

# infinity
a = np.array([np.inf, -np.inf])
print(a)
print(np.isinf(a)) #True for inf and -inf values and False for non-inf

m= np.array([-1,1])/0
print(m)
print(np.isinf(m)) 
