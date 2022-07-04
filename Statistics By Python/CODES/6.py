from turtle import right
import matplotlib.pyplot as plt
import math
# how to


def sd(l):
    N = len(l)

    mu = mean(l)
    sum = 0
    for xi in l:
        sum += (xi-mu)**2
    var = sum/N
    return math.sqrt(var)


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


data = [10, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16, 17, 20, 20]
y = [0 for i in data]
m = mean(data)
print(m)
sigma = sd(data)
print(sigma)
plt.xlim(left=0, right=0)
plt.scatter(data, y, marker='x', color='g')
plt.scatter([m], [0], marker='o', color='b', s=100)
plt.errorbar(m, 0.1, xerr=sigma, fmt='o')

k = 1
for i in data:
    plt.errorbar(i+(m-i)/2, k, xerr=(m-i)/2, fmt='o')
    k += .1
plt.xlim(0,20) 
plt.boxplot(data,vert=False)
plt.boxplot(data,horizt=False)






y2018=[1,2,3,6,6,9,9,9,9,9,9,9,7,8,9,7,8,7,4,1,2,3,6,5,8,9,4,2,8]
y2019=[9,6,3,2,5,8,7,4,1,2,3,6,5,4,7,8,9,9,6,3,1,5,7,8,2,7,8,1,2]
plt.xlim(0,20)
plt.boxplot([y2018,y2019],vert=False)