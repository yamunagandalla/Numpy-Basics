import numpy as np 
rng= np.random.default_rng(123)
print(rng)
print(rng.integers(low=1,high=5,size=(2,3)))
print(rng.choice(a=10,size=3,replace=False))
print(rng.permutation(np.arange(5)))
print(rng.uniform(low=0.0, high=1.0, size=(2,2)))
print(rng.normal(loc=0.0, scale=1.0, size=(2,2)))
print(rng.binomial(n=10, p=0.5, size=(2,2)))
