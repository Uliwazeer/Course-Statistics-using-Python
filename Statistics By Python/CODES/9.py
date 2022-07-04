import matplotlib.pyplot as plt

y2018=[1,2,3,6,6,9,9,9,9,9,9,9,7,8,9,7,8,7,4,1,2,3,6,5,8,9,4,2,8]
y2019=[9,6,3,2,5,8,7,4,1,2,3,6,5,4,7,8,9,9,6,3,1,5,7,8,2,7,8,1,2]
plt.xlim(0,20)
plt.boxplot([y2018,y2019],vert=False)

# Histogram=(hist) =>draw diagrams for data by using arrays by repeat values in list or arrays

data=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,9,7,8,1,5,7,48,15,6]
# to give you range or limits for number on horizental line 0->20
plt.xlim(0,20)
# xticks => to make every plot above number to generate list from 0 to 20
plt.xticks([i for i in range(21)])
plt.yticks([i/10 for i in range(11)])
plt.grid()
# align=> it take 3 values left or right or mid
# rwidth =relative width=> default value it equal to 1
# bins =>to generate list from0 to 21
# cumulative => it take boolean value it use to repeat data and organize it on diagram 
# density=> it take boolean value as 0 and 1 and make date normlization with value percentage
plt.hist([y2018,y2019],color='skyblue',density=True,rwidth=0.5,align='left',bins=[i for i in range(22)],cumulative=True)

# Draw
sigma = sd(data)
mu = mean(data) 
print('sd = ',sigma)
print('mean = ',mu)

X = [i for i in range(21)]
F = [((1/sigma*math.sqrt(2*3.14))) * math.pow(2.7,(-.5*((X-mu)/sigma)**2))) for x in X]
plt.plot(X,F)