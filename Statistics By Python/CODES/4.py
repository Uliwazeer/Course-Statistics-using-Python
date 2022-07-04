from turtle import right
import matplotlib.pyplot as plt
import math 
# how to 
def sd(l):
    mu = mean(l)
    sum = 0 
    for xi in l:
        sum += (xi-mu)**2 
        var = sum/len(l)
        return math.sqrt(l)


def mode(l):
    s = set(l)
    if len(s) == len(l):
        return False
    ss = list(s)
    print(ss)
    freq = [data.count(i) for i in ss]
    print(freq)
    maxIndx = freq.index(max(freq))
    return ss[maxIndx]


def median(l):
    l.sort()
    n = len(l)
    if n % 2 != 0:
        return l[int(n/2)]
    else:
        return (l[int((n/2)-1)]+l[int(n/2)])/2


def mean(l):
    sum = 0
    for i in l:
        sum = sum + i
    return sum/len(l)


data = [2, 3, 5, 6, 4, 7, 8, 9, 6, 33, 10, 58,13,14,14,14,14,16]
y = [0 for i in data]
m = mean(data)
print(m)
sigma = sd(data) 
print(sigma) 
plt.xlim(left=0, right=0) 
plt.scatter(data, y, marker='x', color='g')
plt.scatter([m], [0], marker='u', color='b',s=100)
# errorbar => it take points x and y (xerr=> in direction x)
# errorbar => it take points x and y (yerr=> in direction y)
# fmt = marker=> it refer to format it make shape circle or x....
plt.errorbar(m, 0.1,xerr=sigma, fmt='o')

k=1
for i  in data:
    plt.errorbar(i+(m-i)/2,k,xerr=(m-i)/2,fmt='o')
    
    k+=.1
    
plt.errorbar(1,2,xerr=0.5, fmt='y')
            
