# how to count sample mean 
# mean = average for data
# mean => sum all data / number of data
# mean always near to more data on diagram
def mean(l):
    sum  = 0 
    for i in l:
        sum = sum + i
    return sum/len(l)
data = [2,3,5,6,4,7,8,9,6,33,10,58]
y = [0 for i in data] # equal to y=[0,0,0,0,0,0,0,0,0,0,0]
m = mean(data)
print('sample mean = ',mean(data))

# how to make data visualization using matpoltlib
# plot => take (x-axis , y-axis) in 2Dand use to arrive points together
# scatter use to put points not arrive points together
import matplotlib.pyplot as plt  
plt.plot([1,2,3,4,5],[5,4,3,2,1])
plt.scatter([1,2,3,4,5],[5,4,3,2,1])
plt.scatter(data , y,marker='x',color='b')
plt.scatter([m],[0],color='g')
