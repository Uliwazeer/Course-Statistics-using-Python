import matplotlib.pyplot as plt 
import numpy as np 
import math 
data = np.array([11,22,33,44,55,66,77,88,99,100,12,13,14,15,16,17,18,19,20])
print(data) 
plt.xlim(0,20)
plt.ylim(0,10)
plt.xticks([i for i in range(21)])
plt.yticks([i for i in range(11)])
plt.grid()
plt.hist(data,rwidth=0.5,align='left',bins=[i for i in range(22)])
# Distribution characterstics
sigma = np.std(data)
mu = np.mean(data)
print('sd = ',sigma)
print('mean = ',mu)
X =[ i for i in np.arange(0,21,0.1)]
F =[ len(data)*((1/sigma*math.sqrt(2*3.14))) * math.pow(2.7, (-.5*((X-mu)/sigma)**2)) for x in X]
plt.plot(X,F)
D=((data-mu)**3)
Q=D.sum()
print(Q)
plt.xlim(0, 20)
plt.ylim(0, 10)
plt.grid()
plt.boxplot(data,vert=False)
