# indexing => where site of element
# slicing =>range of sequances
import numpy as np

y = np.random.rand(5, 3, 2)
print(y)
t = 7*np.random.rand(5, 3, 2)
print(y)
# round=> remove the partial
o = np.round(5*np.random.rand(4, 2, 3))
print(y)
print(o)
print(t)
print(o+t+y)
print(o-t-y)
print(o-t**y)
print(o-t/y)

