# how to median = mean
# mean  maybe equal to median when data is symetric(mean and median above on ather on diagram) around zero-axis around centre 
from turtle import color
import matp/lotlib.pyplot as plt 
def median(l):
    l.sort()
    n = len(l)
    if n%2 !=0:
        return l[int(n/2)]
    else:
        return (l[int((n/2)-1)]+l[int(n/2)])/2
def mean(l):
    sum = 0
    for i in l:
        sum = sum + i
    return sum/len(l)
data = [2, 3, 5, 6, 4, 7, 8, 9, 6, 33, 10, 58]
y = [0 for i in data]  # equal to y=[0,0,0,0,0,0,0,0,0,0,0]
m = mean(data)
Med = median(data)
plt.xlim(left=0, right=20) #to limit when diagram of data existed
plt.scatter(data,y,marker='x',color='b')
plt.scatter([m],[0],marker='y',color='r' s=100)
# s => size to make point bigger on diagram and mean = median
plt.scatter([Med],[0],marker='r',color='o')
# xlim => it is function take two parameters (x,y) to limit end of diagram
print('sample mean = ', mean(data))


