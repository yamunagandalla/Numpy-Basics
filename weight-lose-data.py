import numpy as np 
dailywts = 185- np.arange(5*7)/5
print(dailywts)

a=dailywts[5::7] # all sarturday weights
print("Saturday weights:", a)
b=dailywts[6::7] # all sunday weights
print("Sunday weights:", b)
c= (a+b)/2 # average of saturday and sunday weights weekend weights
print("Weekend average weights:", c)