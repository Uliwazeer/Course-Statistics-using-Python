# NUMPY =>it is a datastructre we can use instead of list which exist in python (instead of store data in list you can store it in NUMPY library)
# How to create NDARRAY
import numpy as np 
# when you have data
a = np.array([1,2,3,4,5,6,7,8,9])
print(a)
# shape it know you shape of data in array columns and rows 
print(a.shape())
print(a.type())
b = np.zeros((2,))
b = np.zeros((6,5))
b = np.zeros((4,5,6))
b = np.zeros((3,2,4,9))
b = np.zeros((3,2,4,9,1))
c = np.ones((2,))
c = np.ones((6, 5))
c = np.ones((4, 5, 6))
c = np.ones((3, 2, 4, 9))
c = np.ones((3,2,4,9,1))
d = np.empty((2,5))
e = np.random.rand(4,6)
f = np.arange(2,5,.1)
g = np.linspace(2,8,9)